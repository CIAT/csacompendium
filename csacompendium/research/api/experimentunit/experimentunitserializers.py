from csacompendium.research.models import (
    ExperimentUnit,
    ExperimentUnitCategory,
)
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    FieldMethodSerializer,
    get_related_content,
    get_related_content_url,
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.researchexperimentunit.researchexperimentunitserializers \
    import research_experiment_unit_serializers

research_experiment_unit_serializers = research_experiment_unit_serializers()


def experiment_unit_serializers():
    """
    Experiment unit serializers
    :return: All experiment unit serializers
    :rtype: Object
    """

    class ExperimentUnitBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ExperimentUnit
            fields = [
                'id',
                'exp_unit_code',
                'experimentunitcategory',
                'common_name',
                'latin_name',
            ]

    class ExperimentUnitFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_experiment_unit_category_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(ExperimentUnitCategory, obj.experimentunitcategory.id)

        def get_research_relation(self, obj):
            """
            Gets control/treatment research record
            :param obj: Current record object
            :return: Related research object/record
            :rtype: Object/record
            """
            request = self.context['request']
            ResearchExperimentUnitContentTypeSerializer = research_experiment_unit_serializers[
                'ResearchExperimentUnitContentTypeSerializer'
            ]
            related_content = get_related_content(
                obj, ResearchExperimentUnitContentTypeSerializer, obj.research_experiment_unit_relation, request
            )
            return related_content

    class ExperimentUnitListSerializer(ExperimentUnitBaseSerializer, ExperimentUnitFieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        experiment_unit_category_url = SerializerMethodField()
        research_relation = SerializerMethodField()
        url = hyperlinked_identity('research_api:experiment_unit_detail', 'slug')

        class Meta:
            model = ExperimentUnit
            fields = ExperimentUnitBaseSerializer.Meta.fields + [
                'experiment_unit_category_url',
                'url',
                'research_relation',
            ]

    class ExperimentUnitDetailSerializer(
        ExperimentUnitBaseSerializer, FieldMethodSerializer, ExperimentUnitFieldMethodSerializer
    ):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        experiment_unit_category_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        research_relation = SerializerMethodField()

        class Meta:
            common_fields = [
                'experiment_unit_category_url',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'research_relation',
            ]
            model = ExperimentUnit
            fields = ExperimentUnitBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'ExperimentUnitListSerializer': ExperimentUnitListSerializer,
        'ExperimentUnitDetailSerializer': ExperimentUnitDetailSerializer
    }
