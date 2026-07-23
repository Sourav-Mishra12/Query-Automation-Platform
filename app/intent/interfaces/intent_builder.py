from abc import ABC, abstractmethod

from app.understanding.models.metadata_search_result import MetadataSearchResult
from app.business.models.business_resolution_result import BusinessResolutionResult
from app.intent.models.query_intent import QueryIntent


class IIntentBuilder(ABC):

    @abstractmethod
    def build(
        self,
        normalized_query: str,
        metadata: MetadataSearchResult,
        business: BusinessResolutionResult
    ) -> QueryIntent:
        pass