from .controlresearch.controlresearchserializers import control_research_serializers
from .treatmentresearch.treatmentresearchserializers import treatment_research_serializers
from .experimentrep.experimentrepserializers import experiment_rep_serializers
from .nitrogenapplied.nitrogenappliedserializers import nitrogen_applied_serializers
from .experimentdetails.experimentdetailsserializers import experiment_details_serializers
from .experimentduration.experimentdurationserializers import experiment_duration_serializers
from .measurementyear.measurementyearserializers import measurement_year_serializers
from .measurementseason.measurementseasonserializers import measurement_season_serializers
from .researchauthor.researchauthorserializer import research_author_serializers
from .author.authorserializers import author_serializers
from .researchspecies.researchspeciesserializers import research_species_serializers
from .species.speciesserializers import species_serializers


treatment_research_serializers = treatment_research_serializers()
control_research_serializers = control_research_serializers()
experiment_rep_serializers = experiment_rep_serializers()
nitrogen_applied_serializers = nitrogen_applied_serializers()
experiment_details_serializers = experiment_details_serializers()
experiment_duration_serializers = experiment_duration_serializers()
measurement_year_serializers = measurement_year_serializers()
measurement_season_serializers = measurement_season_serializers()
research_author_serializers = research_author_serializers()
author_serializers = author_serializers()
research_species_serializers = research_species_serializers()
species_serializers = species_serializers()
