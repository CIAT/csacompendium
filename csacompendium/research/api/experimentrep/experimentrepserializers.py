from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from csacompendium.research.api.controlresearch.controlresearchserializers import control_research_serializers
from csacompendium.research.api.treatmentresearch.treatmentresearchserializers import treatment_research_serializers
from csacompendium.research.models import ExperimentRep
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content

control_research_serializers = control_research_serializers()
treatment_research_serializers = treatment_research_serializers()


def experiment_rep_serializers():
    """
    Experiment replication serializers
    :return: All experiment replication  serializers
    :rtype: Object
    """

    class ExperimentRepBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        class Meta:
            model = ExperimentRep
            fields = [
                'id',
                'no_replication',
            ]

    class ExperimentRepRelationBaseSerializer(ModelSerializer):
        """
        Base serializer for DRY implementation.
        """
        control_research = SerializerMethodField()
        treatment_research = SerializerMethodField()

        class Meta:
            model = ExperimentRep
            fields = [
                'control_research',
                'treatment_research',
            ]

    class ExperimentRepFieldMethodSerializer:
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

        def get_treatment_research(self, obj):
            """
            :param obj: Current record object
            :return: Treatment research object
            :rtype: Object/record
            """
            request = self.context['request']
            TreatmentResearchListSerializer = treatment_research_serializers['TreatmentResearchListSerializer']
            related_content = get_related_content(
                obj, TreatmentResearchListSerializer, obj.treatment_research_relation, request
            )
            return related_content

    class ExperimentRepListSerializer(
        ExperimentRepBaseSerializer,
        ExperimentRepRelationBaseSerializer,
        ExperimentRepFieldMethodSerializer
    ):
        """
        Serialize all records in given fields into an API
        """
        url = hyperlinked_identity('research_api:experiment_rep_detail', 'pk')

        class Meta:
            model = ExperimentRep
            fields = ExperimentRepBaseSerializer.Meta.fields + ['url', ] + \
                     ExperimentRepRelationBaseSerializer.Meta.fields

    class ExperimentRepDetailSerializer(
        ExperimentRepBaseSerializer, ExperimentRepRelationBaseSerializer,
        FieldMethodSerializer, ExperimentRepFieldMethodSerializer
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
            ] + ExperimentRepRelationBaseSerializer.Meta.fields
            model = ExperimentRep
            fields = ExperimentRepBaseSerializer.Meta.fields + common_fields
            read_only_fields = ['id', ] + common_fields
    return {
        'ExperimentRepListSerializer': ExperimentRepListSerializer,
        'ExperimentRepDetailSerializer': ExperimentRepDetailSerializer
    }
