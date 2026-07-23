from abc import ABC, abstractmethod

from .models import (
    NormalizedQuery,
    MetadataSearchResult,
    BusinessResolutionResult
)


class IBusinessResolver(ABC):

    @abstractmethod
    def resolve(
        self,
        query: NormalizedQuery,
        metadata: MetadataSearchResult
    ) -> BusinessResolutionResult:
        
        raise NotImplementedError


class BusinessResolver(IBusinessResolver):

    def resolve(
        self,
        query: NormalizedQuery,
        metadata: MetadataSearchResult
    ) -> BusinessResolutionResult:
        ...