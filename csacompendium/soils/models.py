# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from csacompendium.utils.abstractmodels import (
    AuthUserDetail,
    CreateUpdateTime,
)
from csacompendium.utils.createslug import create_slug
from csacompendium.utils.modelmanagers import (
    model_instance_filter,
    model_foreign_key_qs,
    model_type_filter,
    create_model_type,
    get_year_choices,
    get_datetime_now,
)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from decimal import Decimal


class SoilType(AuthUserDetail, CreateUpdateTime):
    """
    Soil type model.  Creates soil type entity.
    """
    slug = models.SlugField(unique=True, blank=True)
    soil_type = models.CharField(max_length=80, unique=True)
    classification = models.CharField(max_length=80, blank=True, null=True)

    def __unicode__(self):
        return self.soil_type

    def __str__(self):
        return self.soil_type

    def get_api_url(self):
        """
        Get soil type URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('soil_api:soil_type_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Soil Types'

    @property
    def soil_relation(self):
        """
        Get related soil properties
        :return: Query result from the soil model
        :rtype: object/record
        """
        instance = self
        qs = Soil.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=SoilType)
def pre_save_soil_type_receiver(sender, instance, *args, **kwargs):
    """
    Create a slug before save.
    :param sender: Signal sending object
    :param instance: Object instance
    :param args: Any other argument
    :param kwargs: Keyword arguments
    :return: None
    :rtype: None
    """
    if not instance.slug:
        instance.slug = create_slug(instance, SoilType, instance.soil_type)


class SoilTexture(AuthUserDetail, CreateUpdateTime):
    """
    Soil texture model. Creates soil type entity.
    """
    slug = models.SlugField(unique=True, blank=True)
    soil_texture = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.soil_texture

    def __str__(self):
        return self.soil_texture

    def get_api_url(self):
        """
        Get soil texture URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('soil_api:soil_texture_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Soil Textures'

    @property
    def soil_relation(self):
        """
        Get related soil properties
        :return: Query result from the soil model
        :rtye: object/record
        """
        instance = self
        qs = Soil.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=SoilTexture)
def pre_save_soil_texture_receiver(sender, instance, *args, **kwargs):
    """
    Create a slug before save.
    :param sender: Signal sending object
    :param instance: Object instance
    :param args: Any other argument
    :param kwargs: Keyword arguments
    :return: None
    :rtype: None
    """
    if not instance.slug:
        instance.slug = create_slug(instance, SoilTexture, instance.soil_texture)


class SoilManager(models.Manager):
    """
    Soil model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related soil object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, SoilManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, SoilManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, SoilManager)

    def create_by_model_type(self, model_type, slug, **kwargs):
        """
        Create object by model type
        :param model_type: Content/model type
        :param slug: Slug
        :param kwargs: Fields to be created
        :return: Data object
        :rtype: Object
        """
        return create_model_type(self, model_type, slug, slugify=True, **kwargs)


class Soil(AuthUserDetail, CreateUpdateTime):
    """
    Soil model.  Creates soil entity.
    """
    limit = models.Q(app_label='locations', model='location')
    soiltype = models.ForeignKey(SoilType, on_delete=models.PROTECT, verbose_name='Soil Type')
    soiltexture = models.ForeignKey(SoilTexture, on_delete=models.PROTECT, verbose_name='Soil Texture')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    som = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        blank=True,
        null=True,
        default=Decimal('0.0'),
        verbose_name='Soil Organic Matter-SOM'
    )
    som_uom = models.CharField(max_length=6, blank=True, null=True, default='%', verbose_name='SOM UOM')
    initial_soc = models.DecimalField(
        max_digits=6, decimal_places=4, blank=True, null=True, default=Decimal('0.0'), verbose_name='Initial SOM'
    )
    soil_ph = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, default=Decimal('0.0'))
    soil_years = models.SmallIntegerField(
        choices=get_year_choices(), blank=True, null=True, default=get_datetime_now()
    )
    objects = SoilManager()

    def __unicode__(self):
        return str(self.som)

    def __str__(self):
        return str(self.som)

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Soils'
