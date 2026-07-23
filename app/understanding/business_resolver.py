from abc import ABC, abstractmethod

from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.models.company import Company
from app.models.dealer import Dealer

from .models import (
    NormalizedQuery,
    MetadataSearchResult,
    BusinessEntity,
    BusinessResolutionResult,
)


class IBusinessResolver(ABC):

    @abstractmethod
    def resolve(
        self,
        query: NormalizedQuery,
        metadata: MetadataSearchResult,
    ) -> BusinessResolutionResult:
        raise NotImplementedError


class BusinessResolver(IBusinessResolver):

    def __init__(self, db: Session):
        self._db = db

    def resolve(
        self,
        query: NormalizedQuery,
        metadata: MetadataSearchResult,
    ) -> BusinessResolutionResult:

        result = BusinessResolutionResult()

        for term in metadata.unmatched_terms:

            entity = self._find_company(term)

            if entity:
                result.entities.append(entity)
                continue

            entity = self._find_dealer(term)

            if entity:
                result.entities.append(entity)
                continue

            result.unresolved_terms.append(term)

        return result

    def _find_company(self, term: str) -> BusinessEntity | None:

        company = self._db.scalar(
            select(Company).where(
                or_(
                    Company.Symbol == term,
                    Company.CompanyName == term,
                )
            )
        )

        if not company:
            return None

        matched_column = (
            "Symbol"
            if company.Symbol.lower() == term.lower()
            else "CompanyName"
        )

        return BusinessEntity(
            entity_type="Company",
            value=term,
            matched_column=matched_column,
        )

    def _find_dealer(self, term: str) -> BusinessEntity | None:

        dealer = self._db.scalar(
            select(Dealer).where(
                Dealer.DealerName == term
            )
        )

        if not dealer:
            return None

        return BusinessEntity(
            entity_type="Dealer",
            value=term,
            matched_column="DealerName",
        )