from abc import ABC, abstractmethod

from app.intent.models.query_intent import QueryIntent


class ISqlGenerator(ABC):

    @abstractmethod
    def generate(
        self,
        intent: QueryIntent,
    ) -> str:
        pass