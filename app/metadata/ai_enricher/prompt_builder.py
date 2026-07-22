from app.metadata.ai_enricher.prompts import (
    TABLE_ENRICHMENT_PROMPT,
    COLUMN_ENRICHMENT_PROMPT,
)
import json 


class PromptBuilder:

    def build_table_prompt(
        self,
        table: dict,
    ) -> str:
        
        return TABLE_ENRICHMENT_PROMPT.format(
            table=json.dumps(table , indent=4)
        )

    def build_column_prompt(
        self,
        table_name: str,
        column: dict,
    ) -> str:
        
        return COLUMN_ENRICHMENT_PROMPT.format(
            table_name=table_name,
            column=json.dumps(column , indent=4),
        )