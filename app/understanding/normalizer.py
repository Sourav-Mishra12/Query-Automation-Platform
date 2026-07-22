# used for normalizng the data which is coming in as it can be dangerous not to do so

from abc import ABC, abstractmethod

from .models import NormalizedQuery
import re 

class IQueryNormalizer(ABC):

    @abstractmethod
    def normalize(self, query: str) -> NormalizedQuery:
        """Normalize a raw user query."""
        def normalize(self,query : str) -> NormalizedQuery:

            pass 
         
    

class QueryNormalizer(IQueryNormalizer):

    def normalize(self, query: str) -> NormalizedQuery:
        original = query
        normalized = query.lower().strip()
        normalized = re.sub(r"[^\w\s]", " ", normalized)
        normalized = re.sub(r"\s+", " ", normalized)
        tokens = normalized.split()

        return NormalizedQuery(
            original=original,
            normalized=normalized,
            tokens=tokens,
        )