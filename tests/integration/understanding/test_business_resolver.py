# from app.understanding.business_resolver import BusinessResolver
# from app.understanding.models import (
#     BusinessEntity,
#     BusinessResolutionResult,
#     MetadataSearchResult,
#     NormalizedQuery,
# )


# def test_resolves_company_symbol():
#     query = NormalizedQuery(
#         original="Show TCS trades",
#         normalized="show tcs trades",
#         tokens=["show", "tcs", "trades"],
#     )

#     metadata = MetadataSearchResult(
#         matched_terms=["trades"],
#         unmatched_terms=["show", "tcs"],
#     )

#     resolver = BusinessResolver()

#     result = resolver.resolve(query, metadata)

#     assert len(result.entities) == 1
#     assert result.entities[0].entity_type == "Company"
#     assert result.entities[0].value == "TCS"
#     assert result.entities[0].matched_column == "Symbol"


# if __name__ == "__main__":
#     test_resolves_company_symbol()



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models.company import Company
from app.models.dealer import Dealer
from app.understanding.business_resolver import BusinessResolver
from app.understanding.models import (
    MetadataSearchResult,
    NormalizedQuery,
)


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def test_resolves_company_symbol():

    session = SessionLocal()

    try:
        # Arrange
        query = NormalizedQuery(
            original="Show TCS trades",
            normalized="show tcs trades",
            tokens=["show", "tcs", "trades"],
        )

        metadata = MetadataSearchResult(
            matched_terms=["trades"],
            unmatched_terms=["tcs"],
        )

        resolver = BusinessResolver(session)

        print("Before resolving")

        # Act
        result = resolver.resolve(query, metadata)

        print("After resolving")

        print("Entities:", result.entities)
        print("Unresolved:", result.unresolved_terms)

        if result.entities:
                print(result.entities[0])
                print(result.entities[0].entity_type)
                print(result.entities[0].value)
                print(result.entities[0].matched_column)

        # Assert
        assert len(result.entities) == 1

        entity = result.entities[0]

        assert entity.entity_type == "Company"
        assert entity.value == "tcs"
        assert entity.matched_column == "Symbol"

        assert len(result.unresolved_terms) == 0

    finally:
        session.close()

#  dealer tests

def test_resolves_dealer():

    session = SessionLocal()

    try:
        query = NormalizedQuery(
            original="Show Rahul Sharma trades",
            normalized="show rahul sharma trades",
            tokens=["show", "rahul", "sharma" , "trades"],
        )

        metadata = MetadataSearchResult(
            matched_terms=["trades"],
            unmatched_terms=["Rahul Sharma"],
        )

        resolver = BusinessResolver(session)

        print("Before resolving")

        result = resolver.resolve(query, metadata)

        print("After resolving")

        print("Entities:", result.entities)
        print("Unresolved:", result.unresolved_terms)

        if result.entities:
                print(result.entities[0])
                print(result.entities[0].entity_type)
                print(result.entities[0].value)
                print(result.entities[0].matched_column)


        assert len(result.entities) == 1

        entity = result.entities[0]

        assert entity.entity_type == "Dealer"
        assert entity.value == "Rahul Sharma"
        assert entity.matched_column == "DealerName"

        assert len(result.unresolved_terms) == 0

    finally:
        session.close()


# unknown entity test 

def test_unresolved_term():

    session = SessionLocal()

    try:
        query = NormalizedQuery(
            original="Show Batman trades",
            normalized="show batman trades",
            tokens=["show", "batman", "trades"],
        )

        metadata = MetadataSearchResult(
            matched_terms=["trades"],
            unmatched_terms=["doomsday"],
        )

        resolver = BusinessResolver(session)

        print("before resolving")

        result = resolver.resolve(query, metadata)

        print("after resolving")

        print("Entities:", result.entities)
        print("Unresolved:", result.unresolved_terms)

        if result.entities:
                print(result.entities[0])
                print(result.entities[0].entity_type)
                print(result.entities[0].value)
                print(result.entities[0].matched_column)

        assert len(result.entities) == 0
        assert result.unresolved_terms == ["doomsday"]

    finally:
        session.close()


if __name__ == "__main__":

    # test_resolves_company_symbol()
    # test_resolves_dealer()
    test_unresolved_term()