from abc import ABC, abstractmethod

from app.understanding.models import MetadataSearchResult
from app.understanding.models import BusinessResolutionResult
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