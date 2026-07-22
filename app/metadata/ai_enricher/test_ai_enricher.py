from groq import Groq

from app.core.config import settings
from app.metadata.ai_enricher.enricher import AIEnricher
from app.metadata.ai_enricher.llm_client import LLMClient
from app.metadata.ai_enricher.prompt_builder import PromptBuilder
from app.metadata.ai_enricher.response_parser import ResponseParser
from app.metadata.repository import MetadataRepository


def create_llm_client() -> LLMClient:
    """
    Creates and returns an LLM client.
    """

    groq_client = Groq(
        api_key=settings.LLM_API_KEY,
    )

    return LLMClient(
        client=groq_client,
        model=settings.LLM_MODEL,
    )


def test_ai_enricher():
    """
    End-to-end test for the AI enrichment pipeline.
    """

    # Dependencies
    repository = MetadataRepository()
    prompt_builder = PromptBuilder()
    response_parser = ResponseParser()
    llm_client = create_llm_client()

    enricher = AIEnricher(
        llm_client=llm_client,
        prompt_builder=prompt_builder,
        response_parser=response_parser,
    )

    # Load metadata
    metadata = repository.load("RMS_DEV")

    print("========== ORIGINAL METADATA ==========")
    print(metadata)

    # Enrich metadata
    enriched_metadata = enricher.enrich(metadata)

    print("\n========== ENRICHED METADATA ==========")
    print(enriched_metadata)

    # Persist enriched metadata
    repository.save(
        database_name="RMS_DEV",
        metadata=enriched_metadata,
    )

    print("\nMetadata successfully saved.")


if __name__ == "__main__":
    test_ai_enricher()