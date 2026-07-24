from abc import ABC, abstractmethod

from app.intent.models import QueryIntent
from app.prompt.models import SqlPrompt


class ISqlPromptBuilder(ABC):

    @abstractmethod
    def build(
        self,
        intent: QueryIntent
    ) -> SqlPrompt:
        pass