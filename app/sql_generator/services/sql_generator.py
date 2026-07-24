from app.prompt.interfaces.prompt_builder import ISqlPromptBuilder
from app.metadata.ai_enricher.llm_client import ILLMClient
from app.intent.models.query_intent import QueryIntent

from app.sql_generator.interfaces.sql_generator import ISqlGenerator


class SqlGenerator(ISqlGenerator):

    def __init__(
        self,
        prompt_builder: ISqlPromptBuilder,
        llm_client: ILLMClient,
    ):
        self._prompt_builder = prompt_builder
        self._llm_client = llm_client
        

    def generate(
        self,
        intent: QueryIntent,
    ) -> str:

        prompt = self._prompt_builder.build(intent)

        messages =  [

             {
               "role": "system",
               "content": prompt.system_prompt,
             },
             {
               "role": "user",
               "content": prompt.user_prompt,
             },

            ]

        sql = self._llm_client.generate(messages)

        return sql 