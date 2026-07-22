# from app.understanding.metadata_search import MetadataSearch
# from app.understanding.normalizer import QueryNormalizer

# executing this just to check if the output structure is correct or not 


# def test_metadata_search():
#     normalizer = QueryNormalizer()
#     search = MetadataSearch()

#     query = normalizer.normalize("Show all TCS trades")
#     result = search.search(query)

#     assert result.matched_tables == []
#     assert result.matched_columns == []
#     assert result.matched_terms == []


# if __name__ == "__main__":
#     normalizer = QueryNormalizer()
#     search = MetadataSearch()

#     query = normalizer.normalize("Show all TCS trades")
#     result = search.search(query)

#     print(result)




#  checking the whole pipeline 




# repository = MetadataRepository()

# search = MetadataSearch(
#     repository=repository,
#     database_name="RMS_DEV"
# )

# normalizer = QueryNormalizer()

# query = normalizer.normalize("Show all TCS trades")

# result = search.search(query)

# print(result)


#  again testing but this time for query understanding component 

from app.understanding.metadata_search import MetadataSearch
from app.understanding.normalizer import NormalizedQuery


from app.understanding.metadata_search import MetadataSearch
from app.understanding.normalizer import NormalizedQuery


class FakeMetadataRepository:

    def load(self, database_name: str):
        return {
            "tables": [
                {
                    "name": "Company",
                    "columns": [
                        {
                            "name": "CompanyName"
                        }
                    ]
                }
            ]
        }


def test_company_table_is_found():

    repository = FakeMetadataRepository()

    search = MetadataSearch(
        repository=repository,
        database_name="RMS_DEV"
    )

    query = NormalizedQuery(
        original="Company",
        normalized="company",
        tokens=["company"]
    )

    result = search.search(query)

    assert len(result.matched_tables) == 1
    assert result.matched_tables[0]["name"] == "Company"


def test_company_name_column_is_found():
    repository = FakeMetadataRepository()

    search = MetadataSearch(
        repository=repository,
        database_name="RMS_DEV"
    )

    query = NormalizedQuery(
        original="CompanyName",
        normalized="companyname",
        tokens=["companyname"]
    )

    result = search.search(query)

    assert len(result.matched_columns) == 1
    assert result.matched_columns[0]["name"] == "CompanyName"


def test_unknown_word_is_unmatched():
    repository = FakeMetadataRepository()

    search = MetadataSearch(
        repository=repository,
        database_name="RMS_DEV"
    )

    query = NormalizedQuery(
        original="Banana",
        normalized="banana",
        tokens=["banana"]
    )

    result = search.search(query)

    assert result.matched_tables == []
    assert result.matched_columns == []
    assert result.unmatched_terms == ["banana"]



def test_company_and_unknown():
    repository = FakeMetadataRepository()

    search = MetadataSearch(
        repository=repository,
        database_name="RMS_DEV"
    )

    query = NormalizedQuery(
        original="Company Banana",
        normalized="company banana",
        tokens=["company", "banana"]
    )

    result = search.search(query)

    assert len(result.matched_tables) == 1
    assert result.unmatched_terms == ["banana"]


def test_synonym_matches_table():
    repository = FakeMetadataRepository()

    search = MetadataSearch(
        repository=repository,
        database_name="RMS_DEV"
    )

    query = NormalizedQuery(
        original="firm",
        normalized="firm",
        tokens=["firm"]
    )

    result = search.search(query)

    assert len(result.matched_tables) == 1
    assert result.matched_tables[0]["name"] == "Company"

if __name__ == "__main__":
    print("Running testtt")
    # test_company_table_is_found()
    # test_company_name_column_is_found()
    # test_unknown_word_is_unmatched()
    # test_company_and_unknown()
    test_synonym_matches_table()

    print("Test Passed ✅")


# python -m tests.integration.understanding.test_metadata_search 
#  copy the line above and paste in terminal to run it , thank me later 