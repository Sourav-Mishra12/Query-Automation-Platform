from groq import Groq 

from app.core.config import settings 
from app.metadata.ai_enricher.enricher import AIEnricher 
from app.metadata.ai_enricher.llm_client import LLMClient 
from app.metadata.ai_enricher.prompt_builder import PromptBuilder 
from app.metadata.ai_enricher.response_parser import ResponseParser 
from app.metadata.repository import MetadataRepository



def test_ai_enricher():

    repository = MetadataRepository()

    metadata = repository.load("RMS_DEV")

    groq_client = Groq(
        api_key=settings.LLM_API_KEY,
    )

    llm_client = LLMClient(
        client=groq_client,
        model=settings.LLM_MODEL,
    )

    prompt_builder = PromptBuilder()

    table = metadata["tables"][0]

    prompt = prompt_builder.build_table_prompt(table)

    print("===== PROMPT =====")
    print(prompt)

    response = llm_client.generate(prompt)

    print("\n===== RESPONSE =====")
    print(response)


if __name__ == "__main__":
    test_ai_enricher()