from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.controlresearch.controlresearchserializers import control_research_serializers
from csacompendium.research.models import NitrogenApplied
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

control_research_serializers = control_research_serializers()


def nitrogen_applied_serializers():
    """
    Nitrogen applied serializers
    :return: All nitrogen applied serializers
    :rtype: Object
    """

    class NitrogenAppliedBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = NitrogenApplied
            fields = [
                'id',
                'nitrogen_amount',
                'amount_uom',
            ]

    class NitrogenAppliedRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        control_research = SerializerMethodField()

        class Meta:
            model = NitrogenApplied
            fields = [
                'control_research',
            ]

    class NitrogenAppliedFieldMethodSerializer:
        """
        Serialize an object based on a provided field
        """
        def get_control_research(self, obj):
            """
            :param obj: Current record object
            :return: Control research object
            :rtype: Object/record
            """
            request = self.context['request']
            ControlResearchListSerializer = control_research_serializers['ControlResearchListSerializer']
            related_content = get_related_content(
                obj, ControlResearchListSerializer, obj.control_research_relation, request
            )
            return related_content

    class NitrogenAppliedListSerializer(
        NitrogenAppliedBaseSerializer,
        NitrogenAppliedRelationBaseSerializer,
        NitrogenAppliedFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:nitrogen_applied_detail', 'pk')

        class Meta:
            model = NitrogenApplied
            fields = NitrogenAppliedBaseSerializer.Meta.fields + ['url', ] + \
                     NitrogenAppliedRelationBaseSerializer.Meta.fields

    class NitrogenAppliedDetailSerializer(
        NitrogenAppliedBaseSerializer, NitrogenAppliedRelationBaseSerializer,
        FieldMethodSerializer, NitrogenAppliedFieldMethodSerializer
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
            ] + NitrogenAppliedRelationBaseSerializer.Meta.fields
            model = NitrogenApplied
            fields = NitrogenAppliedBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'NitrogenAppliedListSerializer': NitrogenAppliedListSerializer,
        'NitrogenAppliedDetailSerializer': NitrogenAppliedDetailSerializer
    }
