from django.conf.urls import url
from .views import (
    research_nitrogen_applied_views,
    nitrogen_applied_views,
    research_measurement_year_views,
    measurement_duration_views,
    measurement_season_views,
    measurement_year_views,
    research_diversity_views,
    diversity_views,
    research_experiment_description_views,
    experiment_description_views,
    research_experiment_replicate_views,
    experiment_replicate_views,
    research_author_views,
    journal_views,
    author_views,
    experiment_unit_views,
    research_experiment_unit_views,
    breed_views,
    experiment_unit_category_views,
    research_views,
)

# Research nitrogen applied URLs
urlpatterns = [
    url(
        r'^researchnitrogenapplied/$',
        research_nitrogen_applied_views['ResearchNitrogenAppliedListAPIView'].as_view(),
        name='research_nitrogen_applied_list'
    ),
    url(
        r'^researchnitrogenapplied/create/$',
        research_nitrogen_applied_views['ResearchNitrogenAppliedCreateAPIView'].as_view(),
        name='research_nitrogen_applied_create'
    ),
    url(
        r'^researchnitrogenapplied/(?P<pk>[\w-]+)/$',
        research_nitrogen_applied_views['ResearchNitrogenAppliedDetailAPIView'].as_view(),
        name='research_nitrogen_applied_detail'
    ),
]

# Nitrogen applied URLs
urlpatterns += [
    url(
        r'^nitrogenapplied/$',
        nitrogen_applied_views['NitrogenAppliedListAPIView'].as_view(),
        name='nitrogen_applied_list'
    ),
    url(
        r'^nitrogenapplied/create/$',
        nitrogen_applied_views['NitrogenAppliedCreateAPIView'].as_view(),
        name='nitrogen_applied_create'
    ),
    url(
        r'^nitrogenapplied/(?P<pk>[\w-]+)/$',
        nitrogen_applied_views['NitrogenAppliedDetailAPIView'].as_view(),
        name='nitrogen_applied_detail'
    ),
]

# Research measurement year URLs
urlpatterns += [
    url(
        r'^researchmeasurementyear/$',
        research_measurement_year_views['ResearchMeasurementYearListAPIView'].as_view(),
        name='research_measurement_year_list'
    ),
    url(
        r'^researchmeasurementyear/create/$',
        research_measurement_year_views['ResearchMeasurementYearCreateAPIView'].as_view(),
        name='research_measurement_year_create'
    ),
    url(
        r'^researchmeasurementyear/(?P<pk>[\w-]+)/$',
        research_measurement_year_views['ResearchMeasurementYearDetailAPIView'].as_view(),
        name='research_measurement_year_detail'
    ),
]

# Measurement duration URLs
urlpatterns += [
    url(
        r'^measurementduration/$',
        measurement_duration_views['MeasurementDurationListAPIView'].as_view(),
        name='measurement_duration_list'
    ),
    url(
        r'^measurementduration/create/$',
        measurement_duration_views['MeasurementDurationCreateAPIView'].as_view(),
        name='measurement_duration_create'
    ),
    url(
        r'^measurementduration/(?P<pk>[\w-]+)/$',
        measurement_duration_views['MeasurementDurationDetailAPIView'].as_view(),
        name='measurement_duration_detail'
    ),
]

# Measurement season URLs
urlpatterns += [
    url(
        r'^measurementseason/$',
        measurement_season_views['MeasurementSeasonListAPIView'].as_view(),
        name='measurement_season_list'
    ),
    url(
        r'^measurementseason/create/$',
        measurement_season_views['MeasurementSeasonCreateAPIView'].as_view(),
        name='measurement_season_create'
    ),
    url(
        r'^measurementseason/(?P<slug>[\w-]+)/$',
        measurement_season_views['MeasurementSeasonDetailAPIView'].as_view(),
        name='measurement_season_detail'
    ),
]

# Measurement year URLs
urlpatterns += [
    url(
        r'^measurementyear/$',
        measurement_year_views['MeasurementYearListAPIView'].as_view(),
        name='measurement_year_list'
    ),
    url(
        r'^measurementyear/create/$',
        measurement_year_views['MeasurementYearCreateAPIView'].as_view(),
        name='measurement_year_create'
    ),
    url(
        r'^measurementyear/(?P<slug>[\w-]+)/$',
        measurement_year_views['MeasurementYearDetailAPIView'].as_view(),
        name='measurement_year_detail'
    ),
]

# Research diversity URLs
urlpatterns += [
    url(
        r'^researchdiversity/$',
        research_diversity_views['ResearchDiversityListAPIView'].as_view(),
        name='research_diversity_list'
    ),
    url(
        r'^researchdiversity/create/$',
        research_diversity_views['ResearchDiversityCreateAPIView'].as_view(),
        name='research_diversity_create'
    ),
    url(
        r'^researchdiversity/(?P<pk>[\w-]+)/$',
        research_diversity_views['ResearchDiversityDetailAPIView'].as_view(),
        name='research_diversity_detail'
    ),
]

# Diversity URLs
urlpatterns += [
    url(
        r'^diversity/$',
        diversity_views['DiversityListAPIView'].as_view(),
        name='diversity_list'
    ),
    url(
        r'^diversity/create/$',
        diversity_views['DiversityCreateAPIView'].as_view(),
        name='diversity_create'
    ),
    url(
        r'^diversity/(?P<slug>[\w-]+)/$',
        diversity_views['DiversityDetailAPIView'].as_view(),
        name='diversity_detail'
    ),
]

# Research experiment description URLs
urlpatterns += [
    url(
        r'^researchexperimentdescription/$',
        research_experiment_description_views['ResearchExperimentDescriptionListAPIView'].as_view(),
        name='research_experiment_description_list'
    ),
    url(
        r'^researchexperimentdescription/create/$',
        research_experiment_description_views['ResearchExperimentDescriptionCreateAPIView'].as_view(),
        name='research_experiment_description_create'
    ),
    url(
        r'^researchexperimentdescription/(?P<pk>[\w-]+)/$',
        research_experiment_description_views['ResearchExperimentDescriptionDetailAPIView'].as_view(),
        name='research_experiment_description_detail'
    ),
]

# Experiment description URLs
urlpatterns += [
    url(
        r'^experimentdescription/$',
        experiment_description_views['ExperimentDescriptionListAPIView'].as_view(),
        name='experiment_description_list'
    ),
    url(
        r'^experimentdescription/create/$',
        experiment_description_views['ExperimentDescriptionCreateAPIView'].as_view(),
        name='experiment_description_create'
    ),
    url(
        r'^experimentdescription/(?P<slug>[\w-]+)/$',
        experiment_description_views['ExperimentDescriptionDetailAPIView'].as_view(),
        name='experiment_description_detail'
    ),
]

# Research experiment replicate URLs
urlpatterns += [
    url(
        r'^researchexperimentreplicate/$',
        research_experiment_replicate_views['ResearchExperimentReplicateListAPIView'].as_view(),
        name='research_experiment_replicate_list'
    ),
    url(
        r'^researchexperimentreplicate/create/$',
        research_experiment_replicate_views['ResearchExperimentReplicateCreateAPIView'].as_view(),
        name='research_experiment_replicate_create'
    ),
    url(
        r'^researchexperimentreplicate/(?P<pk>[\w-]+)/$',
        research_experiment_replicate_views['ResearchExperimentReplicateDetailAPIView'].as_view(),
        name='research_experiment_replicate_detail'
    ),
]

# Experiment replicate URLs
urlpatterns += [
    url(
        r'^experimentreplicate/$',
        experiment_replicate_views['ExperimentReplicateListAPIView'].as_view(),
        name='experiment_replicate_list'
    ),
    url(
        r'^experimentreplicate/create/$',
        experiment_replicate_views['ExperimentReplicateCreateAPIView'].as_view(),
        name='experiment_replicate_create'
    ),
    url(
        r'^experimentreplicate/(?P<pk>[\w-]+)/$',
        experiment_replicate_views['ExperimentReplicateDetailAPIView'].as_view(),
        name='experiment_replicate_detail'
    ),
]

# Research author URLs
urlpatterns += [
    url(
        r'^researchauthor/$',
        research_author_views['ResearchAuthorListAPIView'].as_view(),
        name='research_author_list'
    ),
    url(
        r'^researchauthor/create/$',
        research_author_views['ResearchAuthorCreateAPIView'].as_view(),
        name='research_author_create'
    ),
    url(
        r'^researchauthor/(?P<pk>[\w-]+)/$',
        research_author_views['ResearchAuthorDetailAPIView'].as_view(),
        name='research_author_detail'
    ),
]

# Journal URLs
urlpatterns += [
    url(
        r'^journal/$',
        journal_views['JournalListAPIView'].as_view(),
        name='journal_list'
    ),
    url(
        r'^journal/create/$',
        journal_views['JournalCreateAPIView'].as_view(),
        name='journal_create'
    ),
    url(
        r'^journal/(?P<slug>[\w-]+)/$',
        journal_views['JournalDetailAPIView'].as_view(),
        name='journal_detail'
    ),

]

# Author URLs
urlpatterns += [
    url(
        r'^author/$',
        author_views['AuthorListAPIView'].as_view(),
        name='author_list'
    ),
    url(
        r'^author/create/$',
        author_views['AuthorCreateAPIView'].as_view(),
        name='author_create'
    ),
    url(
        r'^author/(?P<slug>[\w-]+)/$',
        author_views['AuthorDetailAPIView'].as_view(),
        name='author_detail'
    ),
]

# Experiment unit category URLs
urlpatterns += [
    url(
        r'^experimentunitcategory/$',
        experiment_unit_category_views['ExperimentUnitCategoryListAPIView'].as_view(),
        name='experiment_unit_category_list'
    ),
    url(
        r'^experimentunitcategory/create/$',
        experiment_unit_category_views['ExperimentUnitCategoryCreateAPIView'].as_view(),
        name='experiment_unit_category_create'
    ),
    url(
        r'^experimentunitcategory/(?P<slug>[\w-]+)/$',
        experiment_unit_category_views['ExperimentUnitCategoryDetailAPIView'].as_view(),
        name='experiment_unit_category_detail'
    ),
]

# Research experiment unit  URLs
urlpatterns += [
    url(
        r'^researchexperimentunit/$',
        research_experiment_unit_views['ResearchExperimentUnitListAPIView'].as_view(),
        name='research_experiment_unit_list'
    ),
    url(
        r'^researchexperimentunit/create/$',
        research_experiment_unit_views['ResearchExperimentUnitCreateAPIView'].as_view(),
        name='research_experiment_unit_create'
    ),
    url(
        r'^researchexperimentunit/(?P<pk>[\w-]+)/$',
        research_experiment_unit_views['ResearchExperimentUnitDetailAPIView'].as_view(),
        name='research_experiment_unit_detail'
    ),
]

#Breed URLs
urlpatterns += [
    url(
        r'^breed/$',
        breed_views['BreedListAPIView'].as_view(),
        name='breed_list'
    ),
    url(
        r'^breed/create/$',
        breed_views['BreedCreateAPIView'].as_view(),
        name='breed_create'
    ),
    url(
        r'^breed/(?P<slug>[\w-]+)/$',
        breed_views['BreedDetailAPIView'].as_view(),
        name='breed_detail'
    ),
]

# Experiment unit  URLs
urlpatterns += [
    url(
        r'^experimentunit/$',
        experiment_unit_views['ExperimentUnitListAPIView'].as_view(),
        name='experiment_unit_list'
    ),
    url(
        r'^experimentunit/create/$',
        experiment_unit_views['ExperimentUnitCreateAPIView'].as_view(),
        name='experiment_unit_create'
    ),
    url(
        r'^experimentunit/(?P<slug>[\w-]+)/$',
        experiment_unit_views['ExperimentUnitDetailAPIView'].as_view(),
        name='experiment_unit_detail'
    ),
]


# Research URLs
urlpatterns += [
    url(r'^$', research_views['ResearchListAPIView'].as_view(), name='research_list'),
    url(r'^create/$', research_views['ResearchCreateAPIView'].as_view(), name='research_create'),
    url(r'^(?P<pk>[\w-]+)/$', research_views['ResearchDetailAPIView'].as_view(), name='research_detail'),
]