from .outcomeindicator.outcomeindicatorserializers import outcome_indicator_serializers
from .researchoutcomeindicator.researchoutcomeindicatorserializers import research_outcome_indicator_serializers
from .soilmeasurement.soilmeasurementserializers import soil_measurement_serializers
from .experimentoutcome.experimentoutcomeserializers import experiment_outcome_serializers
from .indicatortype.indicatortypeserializers import indicator_type_serializers
from .indicator.indicatorserializers import indicator_serializers
from .subpillar.subpillarserializers import subpillar_serializers


outcome_indicator_serializers = outcome_indicator_serializers()
research_outcome_indicator_serializers = research_outcome_indicator_serializers()
soil_measurement_serializers = soil_measurement_serializers()
experiment_outcome_serializers = experiment_outcome_serializers()
indicator_type_serializers = indicator_type_serializers()
indicator_serializers = indicator_serializers()
subpillar_serializers = subpillar_serializers()
