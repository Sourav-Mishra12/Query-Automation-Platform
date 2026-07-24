import re

from app.models import BusinessResolutionResult
from app.metadata.models import MetadataSearchResult

from app.intent.interfaces.intent_builder import IIntentBuilder
from app.intent.models import (
    Aggregation,
    QueryIntent,
    SortField,
    TimeRange
)


class IntentBuilder(IIntentBuilder):

    def build(
        self,
        normalized_query: str,
        metadata: MetadataSearchResult,
        business: BusinessResolutionResult
    ) -> QueryIntent:

        return QueryIntent(

            target_table=self._build_target_table(metadata),

            entities=business.entities,

            filters=[],

            aggregations=self._build_aggregations(
                normalized_query
            ),

            sort=self._build_sort(
                normalized_query
            ),

            time_range=self._build_time_range(
                normalized_query
            ),

            limit=self._build_limit(
                normalized_query
            )
        )

    # -------------------------------------

    def _build_target_table(
        self,
        metadata: MetadataSearchResult
    ) -> str | None:

        if len(metadata.tables) == 1:
            return metadata.tables[0]

        return None

    # -------------------------------------

    def _build_aggregations(
        self,
        query: str
    ) -> list[Aggregation]:

        query = query.lower()

        aggregations = []

        if "count" in query:
            aggregations.append(
                Aggregation(
                    function="COUNT",
                    target="*"
                )
            )

        if "sum" in query:
            aggregations.append(
                Aggregation(
                    function="SUM",
                    target="UNKNOWN"
                )
            )

        if "average" in query or "avg" in query:
            aggregations.append(
                Aggregation(
                    function="AVG",
                    target="UNKNOWN"
                )
            )

        if "maximum" in query or "max" in query:
            aggregations.append(
                Aggregation(
                    function="MAX",
                    target="UNKNOWN"
                )
            )

        if "minimum" in query or "min" in query:
            aggregations.append(
                Aggregation(
                    function="MIN",
                    target="UNKNOWN"
                )
            )

        return aggregations

    # -------------------------------------

    def _build_sort(
        self,
        query: str
    ) -> list[SortField]:

        query = query.lower()

        sort = []

        if "highest" in query:

            sort.append(
                SortField(
                    target="UNKNOWN",
                    descending=True
                )
            )

        elif "lowest" in query:

            sort.append(
                SortField(
                    target="UNKNOWN",
                    descending=False
                )
            )

        return sort

    # -------------------------------------

    def _build_time_range(
        self,
        query: str
    ) -> TimeRange | None:

        query = query.lower()

        if "today" in query:

            return TimeRange(
                today=True
            )

        match = re.search(
            r"last\s+(\d+)\s+days",
            query
        )

        if match:

            return TimeRange(
                last_n_days=int(
                    match.group(1)
                )
            )

        return None

    # -------------------------------------

    def _build_limit(
        self,
        query: str
    ) -> int | None:

        query = query.lower()

        match = re.search(
            r"top\s+(\d+)",
            query
        )

        if match:
            return int(
                match.group(1)
            )

        return None