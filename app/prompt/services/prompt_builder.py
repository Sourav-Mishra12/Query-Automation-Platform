from app.prompt.interfaces.prompt_builder import ISqlPromptBuilder
from app.prompt.models.sql_prompt import SqlPrompt
from app.intent.models.query_intent import QueryIntent


class SqlPromptBuilder(ISqlPromptBuilder):

    def build(
        self,
        intent: QueryIntent
    ) -> SqlPrompt:

        system_prompt = self._build_system_prompt()
        user_prompt = self._build_user_prompt(intent)

        return SqlPrompt(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

    def _build_system_prompt(self) -> str:
        return """
You are an expert Microsoft SQL Server assistant.

Generate ONLY valid SQL Server SELECT queries.

Rules:
- Return ONLY SQL.
- Never generate INSERT.
- Never generate UPDATE.
- Never generate DELETE.
- Never generate DROP.
- Never generate ALTER.
- Never generate TRUNCATE.
- Never generate EXEC.
- Use only the information provided in the user prompt.
"""

    def _build_user_prompt(
        self,
        intent: QueryIntent
    ) -> str:

        sections = []

        # Target Table
        if intent.target_table:
            sections.append("Target Table:")
            sections.append(intent.target_table)
            sections.append("")

        # Entities
        if intent.entities:
            sections.append("Entities:")

            for entity in intent.entities:
                sections.append(
                    f"- {entity.entity_type}: {entity.value}"
                )

            sections.append("")

        # Filters
        if intent.filters:
            sections.append("Filters:")

            for query_filter in intent.filters:
                sections.append(
                    f"- {filter.field} {filter.operator} {filter.value}"
                )

            sections.append("")

        # Aggregations
        if intent.aggregations:
            sections.append("Aggregations:")

            for aggregation in intent.aggregations:
                sections.append(
                    f"- {aggregation.function}({aggregation.target})"
                )

            sections.append("")

        # Sorting
        if intent.sort:
            sections.append("Sorting:")

            for query_sort in intent.sort:
                direction = "DESC" if query_sort.descending else "ASC"

                sections.append(
                    f"- {query_sort.target} {direction}"
                )

            sections.append("")

        # Time Range
        if intent.time_range:
            sections.append("Time Range:")
            sections.append(str(intent.time_range))
            sections.append("")

        return "\n".join(sections)