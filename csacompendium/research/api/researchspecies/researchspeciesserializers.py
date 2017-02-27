from csacompendium.research.models import (
    Species,
    ResearchSpecies,
)
from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
from csacompendium.utils.serializersutils import (
    CreateSerializerUtil,
    get_related_content_url,
    FieldMethodSerializer
)
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)


def research_species_serializers():
    """
    Research species serializers
    :return: All research species serializers
    :rtype: Object
    """

    def create_research_species_serializer(model_type=None, pk=None, user=None):
        """
        Creates a model serializer
        :param model_type: Model
        :param pk: Primary key
        :param user: Object owner
        :return: Serializer class
        :rtype: Object
        """

        class ResearchSpeciesCreateSerializer(ModelSerializer, CreateSerializerUtil):
            """
            Create a record
            """
            class Meta:
                model = ResearchSpecies
                fields = [
                    'id',
                    'species',
                    'last_update',
                    'time_created',
                ]

            def __init__(self, *args, **kwargs):
                super(ResearchSpeciesCreateSerializer, self).__init__(*args, **kwargs)
                self.model_type = model_type
                self.key = pk
                self.user = user
                self.slugify = False
                self.auth_user = self.get_authenticated_user(self.user)

            def create(self, validated_data):
                """
                Created record from validated data
                :param validated_data: Validated data
                :return: Research species object
                :rtype: Object
                """
                species = validated_data.get('species')
                species_relation = ResearchSpecies.objects.create_by_model_type(
                    self.model_type,
                    self.key,
                    species=species,
                    user=self.auth_user,
                    modified_by=self.auth_user
                )
                if species_relation:
                    return species_relation
                else:
                    raise ValidationError({"non_field_errors": ["This is not a valid content type"]})

        return ResearchSpeciesCreateSerializer

    class ResearchSpeciesListSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        species_url = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_species_url = hyperlinked_identity('research_api:research_species_detail', 'pk')

        class Meta:
            model = ResearchSpecies
            fields = [
                'id',
                'species',
                'species_url',
                'content_type_url',
                'research_species_url',
            ]

        def get_species_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(Species, obj.species.id)

    class ResearchSpeciesSerializer(ModelSerializer):
        """
        Serialize all records in given fields into an API
        """
        species_url = SerializerMethodField()
        relation_id = SerializerMethodField()
        research_species_url = hyperlinked_identity('research_api:research_species_detail', 'pk')

        class Meta:
            model = ResearchSpecies
            fields = [
                'relation_id',
                'species_id',
                'species_url',
                'research_species_url',
            ]

        def get_species_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(Species, obj.species.id)

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research species id
            :rtype: Integer
            """
            return obj.id

    class ResearchSpeciesContentTypeSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize all records in given fields into an API
        """
        relation_id = SerializerMethodField()
        content_type_url = SerializerMethodField()
        research_species_url = hyperlinked_identity('research_api:research_species_detail', 'pk')

        class Meta:
            model = ResearchSpecies
            fields = [
                'relation_id',
                'object_id',
                'content_type_url',
                'research_species_url',
            ]

        def get_relation_id (self, obj):
            """
            :param obj: Current record object
            :return: Research species id
            :rtype: String
            """
            return obj.id

    class ResearchSpeciesDetailSerializer(ModelSerializer, FieldMethodSerializer):
        """
        Serialize single record into an API. This is dependent on fields given.
        """
        species_url = SerializerMethodField()
        user = SerializerMethodField()
        modified_by = SerializerMethodField()
        content_type_url = SerializerMethodField()

        class Meta:
            model = ResearchSpecies
            fields = [
                'id',
                'species',
                'species_url',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'content_type_url',
            ]
            read_only_fields = [
                'id',
                'user',
                'modified_by',
                'last_update',
                'time_created',
                'species_url',
                'content_type_url',
            ]

        def get_species_url(self, obj):
            """
            Get related content type/object url
            :param obj: Current record object
            :return: URL to related object
            :rtype: String
            """
            return get_related_content_url(Species, obj.species.id)

    return {
        'create_research_species_serializer': create_research_species_serializer,
        'ResearchSpeciesListSerializer': ResearchSpeciesListSerializer,
        'ResearchSpeciesSerializer': ResearchSpeciesSerializer,
        'ResearchSpeciesContentTypeSerializer': ResearchSpeciesContentTypeSerializer,
        'ResearchSpeciesDetailSerializer': ResearchSpeciesDetailSerializer
    }