from rest_framework.filters import (
    FilterSet
)
from csacompendium.research_type.models import MeasurementSeason


class MeasurementSeasonListFilter(FilterSet):
    """
    Filter query list from measurement season type database table
    """
    class Meta:
        model = MeasurementSeason
        fields = {'meas_season': ['iexact', 'icontains'], }
        order_by = ['meas_season']
