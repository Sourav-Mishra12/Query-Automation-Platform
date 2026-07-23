from abc import ABC, abstractmethod

from app.metadata.repository import MetadataRepository
from .models import MetadataSearchResult, NormalizedQuery


class IMetadataSearch(ABC):

    @abstractmethod
    def search(self, query: NormalizedQuery) -> MetadataSearchResult:
        raise NotImplementedError


class MetadataSearch(IMetadataSearch):

    def __init__(
        self,
        repository: MetadataRepository,
        database_name: str,
    ):
        self._repository = repository
        self._database_name = database_name

    @staticmethod
    def _matches_table(token: str, table: dict) -> bool:
        if token == table["name"].lower():
            return True

        synonyms = [
            synonym.lower()
            for synonym in table.get("ai_metadata", {}).get("synonyms", [])
        ]

        return token in synonyms

    @staticmethod
    def _matches_column(token: str, column: dict) -> bool:
        if token == column["name"].lower():
            return True

        synonyms = [
            synonym.lower()
            for synonym in column.get("synonyms", [])
        ]

        return token in synonyms

    def search(self, query: NormalizedQuery) -> MetadataSearchResult:

        metadata = self._repository.load(self._database_name)

        result = MetadataSearchResult()

        for token in query.tokens:

            found = False

            # Tables
            for table in metadata["tables"]:

                if self._matches_table(token, table):

                    result.matched_tables.append(table)
                    result.matched_terms.append(token)
                    found = True

                # Columns
                for column in table["columns"]:

                    if self._matches_column(token, column):

                        result.matched_columns.append(column)
                        result.matched_terms.append(token)
                        found = True

            if not found:
                result.unmatched_terms.append(token)

        return result