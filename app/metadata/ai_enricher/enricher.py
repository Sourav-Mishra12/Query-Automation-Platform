from app.metadata.ai_enricher.llm_client import LLMClient
from app.metadata.ai_enricher.prompt_builder import PromptBuilder
from app.metadata.ai_enricher.response_parser import ResponseParser


class AIEnricher:

    def __init__(
        self,
        llm_client,
        prompt_builder,
        response_parser,
    ):
        self._llm_client = llm_client
        self._prompt_builder = prompt_builder
        self._response_parser = response_parser

    def enrich(
        self,
        metadata: dict,
    ) -> dict:
        """
        Enrich metadata using AI.
        """
        self._enrich_database(metadata)
        self._enrich_tables(metadata)
        self._enrich_columns(metadata)

        return metadata

    def _enrich_database(
        self,
        metadata: dict,
    ) -> None:
        pass

    def _enrich_tables(
        self,
        metadata: dict,
    ) -> None:

        tables = metadata.get("tables", [])

        for table in tables:

            prompt = self._prompt_builder.build_table_prompt(table)

            response = self._llm_client.generate(prompt)

            enrichment = self._response_parser.parse_table(response)

            table["ai_metadata"] = {
                "description": enrichment.description,
                "synonyms": enrichment.synonyms,
                "tags": enrichment.tags,
            }

    def _enrich_columns(
        self,
        metadata: dict,
    ) -> None:

        tables = metadata.get("tables", [])

        for table in tables:

            table_name = table["name"]

            for column in table.get("columns", []):

                prompt = self._prompt_builder.build_column_prompt(
                    table_name=table_name,
                    column=column,
                )

                response = self._llm_client.generate(prompt)

                enrichment = self._response_parser.parse_column(response)

                column["description"] = enrichment.description
                column["synonyms"] = enrichment.synonyms
                column["tags"] = enrichment.tags