class LLMClient:
    """
    Wrapper around an LLM provider.
    """

    def __init__(
        self,
        client,
        model: str,
    ):
        self._client = client
        self._model = model



    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Sends the prompt to the configured LLM and
        returns the raw response.
        """
        
        response = self._client.chat.completions.create(
            model=self._model,
            temperature=0.0,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content