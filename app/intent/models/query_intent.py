from dataclasses import dataclass

from .aggregation import Aggregation
from .query_filter import QueryFilter
from .sort_field import SortField
from .time_range import TimeRange
from app.models import BusinessEntity


@dataclass
class QueryIntent:

    target_table: str |None

    entities: list[BusinessEntity]

    filters: list[QueryFilter]

    aggregations: list[Aggregation]

    sort: list[SortField]

    time_range: TimeRange | None

    limit: int | None