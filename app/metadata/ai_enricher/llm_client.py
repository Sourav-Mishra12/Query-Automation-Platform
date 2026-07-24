from typing import List, Dict


class LLMClient:
    """
    Generic wrapper around an LLM provider.

    This client is shared across the application for:
    - AI Enrichment
    - SQL Generation
    - Response Generation
    - Future AI features
    """

    def __init__(
        self,
        client,
        model: str,
        temperature: float = 0.0,
    ):
        self._client = client
        self._model = model
        self._temperature = temperature

    def generate(
        self,
        messages: List[Dict[str, str]],
    ) -> str:
        """
        Sends chat messages to the configured LLM
        and returns the generated response.
        """

        response = self._client.chat.completions.create(
            model=self._model,
            temperature=self._temperature,
            messages=messages,
        )

        if not response.choices:
            raise Exception("LLM returned no response.")

        return response.choices[0].message.content.strip()