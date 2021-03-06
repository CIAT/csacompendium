from csacompendium.research.models import (
    Research,
)
from csacompendium.research.api.researchnitrogenapplied.researchnitrogenappliedserializers import \
    research_nitrogen_applied_serializers
from csacompendium.research.api.researchmeasurementyear.researchmeasurementyearserializers import \
    research_measurement_year_serializers
from csacompendium.research.api.researchdiversity.researchdiversityserializers import \
    research_diversity_serializers
from csacompendium.research.api.researchexperimentdescription.researchexperimentdescriptionserializers import \
    research_experiment_description_serializers
from csacompendium.research.api.researchexperimentreplicate.researchexperimentreplicateserializers import \
    research_experiment_replicate_serializers
from csacompendium.research.api.researchauthor.researchauthorserializer import research_author_serializers
from csacompendium.indicators.api.researchoutcomeindicator.researchoutcomeindicatorserializers import \
    research_outcome_indicator_serializers
from csacompendium.csa_practice.api.researchcsapractice.researchcsapracticeserializers import \
    research_csa_practice_serializers
from csacompendium.research.api.researchexperimentunit.researchexperimentunitserializers import \
    research_experiment_unit_serializers
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    get_related_content,
    get_related_content_url,
    valid_integer,
    CreateSerializerUtil,
    FieldMethodSerializer,
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

research_nitrogen_applied_serializers = research_nitrogen_applied_serializers()
research_measurement_year_serializers = research_measurement_year_serializers()
research_diversity_serializers = research_diversity_serializers()
research_experiment_description_serializers = research_experiment_description_serializers()
research_experiment_replicate_serializers = research_experiment_replicate_serializers()
research_author_serializers = research_author_serializers()
research_outcome_indicator_serializers = research_outcome_indicator_serializers()
research_csa_practice_serializers = research_csa_practice_serializers()
research_experiment_unit_serializers = research_experiment_unit_serializers()


def research_serializers():
    """
    Research serializers
    :return: All research serializers
    :rtype: Object
    """

    class ResearchBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = Research
            fields = ['id', 'research_code', 'experiment_design', ]

    class ResearchRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        content_type_url = SerializerMethodField()
        authors = SerializerMethodField()
        experiment_replicate = SerializerMethodField()
        experiment_description = SerializerMethodField()
        csa_practice = SerializerMethodField()
        nitrogen_applied = SerializerMethodField()
        diversity = SerializerMethodField()
        experiment_unit = SerializerMethodField()
        measurement_year = SerializerMethodField()
        outcome_indicator = SerializerMethodField()

        class Meta:
            model = Research
            fields = [
                'content_type_url',
                'authors',
                'experiment_replicate',
                'experiment_description',
                'csa_practice',
                'nitrogen_applied',
                'diversity',
                'experiment_unit',
                'measurement_year',
                'outcome_indicator',
            ]

    class ResearchFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_authors(self, obj):
            """
            :param obj: Current record object
            :return: Related author details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchAuthorSerializer = research_author_serializers['ResearchAuthorSerializer']
            related_content = get_related_content(obj, ResearchAuthorSerializer, obj.research_author, request)
            return related_content

        def get_experiment_replicate(self, obj):
            """
            :param obj: Current record object
            :return: Related experiment replicate details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchExperimentReplicateSerializer = research_experiment_replicate_serializers[
                'ResearchExperimentReplicateSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchExperimentReplicateSerializer, obj.research_experiment_replicate, request
            )
            return related_content

        def get_experiment_description(self, obj):
            """
            :param obj: Current record object
            :return: Related experiment description details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchExperimentDescriptionSerializer = research_experiment_description_serializers[
                'ResearchExperimentDescriptionSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchExperimentDescriptionSerializer, obj.research_experiment_description, request
            )
            return related_content

        def get_csa_practice(self, obj):
            """
            :param obj: Current record object
            :return: Related CSA practice details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchCsaPracticeSerializer = research_csa_practice_serializers[
                'ResearchCsaPracticeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchCsaPracticeSerializer, obj.research_csa_practice, request
            )
            return related_content

        def get_nitrogen_applied(self, obj):
            """
            :param obj: Current record object
            :return: Related nitrogen applied details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchNitrogenAppliedSerializer = research_nitrogen_applied_serializers[
                'ResearchNitrogenAppliedSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchNitrogenAppliedSerializer, obj.research_nitrogen_applied, request
            )
            return related_content

        def get_diversity(self, obj):
            """
            :param obj: Current record object
            :return: Related diversity details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchDiversitySerializer = research_diversity_serializers[
                'ResearchDiversitySerializer'
            ]
            related_content = get_related_content(
                obj, ResearchDiversitySerializer, obj.research_diversity, request
            )
            return related_content

        def get_measurement_year(self, obj):
            """
            :param obj: Current record object
            :return: Related measurement year details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchMeasurementYearSerializer = research_measurement_year_serializers[
                'ResearchMeasurementYearSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchMeasurementYearSerializer, obj.research_measurement_year, request
            )
            return related_content

        def get_experiment_unit(self, obj):
            """
            :param obj: Current record object
            :return: Related experiment unit details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchExperimentUnitSerializer = research_experiment_unit_serializers[
                'ResearchExperimentUnitSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchExperimentUnitSerializer, obj.research_experiment_unit, request
            )
            return related_content

        def get_outcome_indicator(self, obj):
            """
            :param obj: Current record object
            :return: Related outcome indicator details
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchOutcomeIndicatorSerializer = research_outcome_indicator_serializers[
                'ResearchOutcomeIndicatorSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchOutcomeIndicatorSerializer, obj.research_outcome_indicator, request
            )
            return related_content

    def create_research_serializer(model_type=None, request_key=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param request_key: A slug or primary key depending on what is passed
        :param user: Record owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchCreateSerializer(ModelSerializer, CreateSerializerUtil):
            """
            Create a record
            """
            class Meta:
                model = Research
                fields = [
                    'id', 'research_code', 'experiment_design',
                    'last_update', 'time_created',
                ]

            def __init__(self, *args, **kwargs):
                super(ResearchCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = request_key
                self.user = user
                if valid_integer(request_key):
                    self.slugify = False
                else:
                    self.slugify = True
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research object
                :rtype: Object
                """
                research_code = validated_data.get('research_code')
                experiment_design = validated_data.get('experiment_design')
                research = Research.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    research_code=research_code,
                    experiment_design=experiment_design,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if research:
                    return research
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchCreateSerializer

    class ResearchListSerializer(
        ResearchBaseSerializer, ResearchRelationBaseSerializer,
        FieldMethodSerializer, ResearchFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:research_detail', 'pk')

        class Meta:
            model = Research
            fields = ResearchBaseSerializer.Meta.fields + ['url', ] + \
                     ResearchRelationBaseSerializer.Meta.fields

    class ResearchDetailSerializer(
        ResearchBaseSerializer, ResearchRelationBaseSerializer,
        FieldMethodSerializer, ResearchFieldMethodSerializer
    ):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        user = SerializerMethodField()
        modified_by = SerializerMethodField()

        class Meta:
            common_fields = [
                'user',
                'modified_by',
                'last_update',
                'time_created',
            ] + ResearchRelationBaseSerializer.Meta.fields
            model = Research
            fields = ResearchBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'create_research_serializer': create_research_serializer,
        'ResearchListSerializer': ResearchListSerializer,
        'ResearchDetailSerializer': ResearchDetailSerializer
    }
