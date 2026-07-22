"""
Integration Test for MetadataGenerator

Flow:
Database
    ↓
SchemaScanner
    ↓
MetadataGenerator
"""

from pprint import pprint

from app.core.database import engine
from app.metadata.scanner import SchemaScanner
from app.metadata.generator import MetadataGenerator


def test_generator():

    print("=" * 80)
    print("Running Metadata Generator Test")
    print("=" * 80)

    # Step 1: Scan the database
    scanner = SchemaScanner(engine)
    schema = scanner.scan()

    # Step 2: Generate metadata
    generator = MetadataGenerator()
    metadata = generator.generate(schema)

    # -----------------------------
    # Basic Validation
    # -----------------------------

    assert metadata is not None
    assert metadata["database"] == schema.database_name
    assert len(metadata["tables"]) == len(schema.tables)

    print(f"\nDatabase : {metadata['database']}")
    print(f"Tables   : {len(metadata['tables'])}")

    # -----------------------------
    # Table Validation
    # -----------------------------

    for table in metadata["tables"]:

        print("\n" + "=" * 80)
        print(f"TABLE : {table['name']}")
        print("=" * 80)

        assert table["name"] != ""
        assert isinstance(table["columns"], list)
        assert isinstance(table["relationships"], list)

        print(f"Columns       : {len(table['columns'])}")
        print(f"Relationships : {len(table['relationships'])}")

        print("\nColumns")

        for column in table["columns"]:

            assert column["name"] != ""
            assert column["data_type"] != ""

            print(
                f"  {column['name']:<30}"
                f"{column['data_type']:<20}"
                f"PK={column['primary_key']} "
                f"FK={column['foreign_key']}"
            )

        if table["relationships"]:

            print("\nRelationships")

            for relation in table["relationships"]:

                print(
                    f"  {relation['column']} -> "
                    f"{relation['references']}"
                )

    print("\n")
    print("=" * 80)
    print("Metadata Generator Test Passed")
    print("=" * 80)

    # Optional: Print the entire generated metadata
    print("\nGenerated Metadata:\n")
    pprint(metadata)


if __name__ == "__main__":
    test_generator()