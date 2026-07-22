import json

from app.metadata.ai_enricher.models import TableEnrichment


class ResponseParser:

    def parse_table(
        self,
        response: str,
    ) -> TableEnrichment:

        try:

            data = json.loads(response)

        except json.JSONDecodeError as ex:

            raise ValueError(
                "LLM returned invalid JSON."
            ) from ex

        return TableEnrichment(
            description=data.get("description", ""),
            synonyms=data.get("synonyms", []),
            tags=data.get("tags", []),
        )
    

    def parse_column(
        self,
        response: str,
                    ) -> TableEnrichment:

        data = json.loads(response)

        return TableEnrichment(
            description=data.get("description", ""),
            synonyms=data.get("synonyms", []),
            tags=data.get("tags", []),
        )