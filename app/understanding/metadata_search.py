from abc import ABC, abstractmethod

from app.metadata.repository import MetadataRepository
from .models import MetadataSearchResult, NormalizedQuery


class IMetadataSearch(ABC):

    @abstractmethod
    def search(self, query: NormalizedQuery) -> MetadataSearchResult:
        raise NotImplementedError


class MetadataSearch:

    def __init__(
        self,
        repository: MetadataRepository,
        database_name: str,
             ):
        self._repository = repository
        self._database_name = database_name

        

    def search(self, query: NormalizedQuery):

        metadata = self._repository.load(self._database_name)

        result = MetadataSearchResult()

        for token in query.tokens:

            found = False

            # Tables
            for table in metadata["tables"]:

                if token == table["name"].lower():

                    result.matched_tables.append(table)
                    result.matched_terms.append(token)
                    found = True

                # Columns

                for column in table["columns"]:

                    if token == column["name"].lower():

                        result.matched_columns.append(column)
                        result.matched_terms.append(token)
                        found = True

            if not found:
                result.unmatched_terms.append(token)

        return result