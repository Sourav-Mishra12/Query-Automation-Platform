"""
Integration Test for SchemaScanner

This test connects to the actual RMS_DEV database and verifies that
the scanner correctly discovers the database schema.
"""

from app.core.database import engine
from app.metadata.scanner import SchemaScanner


def test_schema_scanner():

    print("\n========== Starting Schema Scanner Test ==========\n")

    # Create scanner
    scanner = SchemaScanner(engine)

    # Execute scan
    schema = scanner.scan()

    # ------------------------
    # Database Level Validation
    # ------------------------

    assert schema is not None, "Schema should not be None"

    assert schema.database_name is not None, \
        "Database name should not be None"

    assert len(schema.tables) > 0, \
        "No tables were discovered."

    print(f"Database : {schema.database_name}")
    print(f"Tables Found : {len(schema.tables)}")

    # ------------------------
    # Table Validation
    # ------------------------

    for table in schema.tables:

        print(f"\nTable : {table.name}")

        assert table.name != "", \
            "Table name cannot be empty"

        assert table.columns is not None, \
            f"{table.name} has no column collection"

        assert len(table.columns) > 0, \
            f"{table.name} contains no columns"

        print(f"Columns : {len(table.columns)}")

        # ------------------------
        # Column Validation
        # ------------------------

        for column in table.columns:

            assert column.name != "", \
                f"Column name missing in table {table.name}"

            assert column.data_type != "", \
                f"{column.name} has no datatype"

            print(
                f"    {column.name:<30}"
                f"{column.data_type:<20}"
                f"PK={column.is_primary_key}"
                f"  FK={column.is_foreign_key}"
                f"  Nullable={column.nullable}"
            )

        # ------------------------
        # Foreign Key Validation
        # ------------------------

        if table.foreign_keys:

            print("\n    Foreign Keys")

            for fk in table.foreign_keys:

                assert fk.column != ""
                assert fk.referenced_table != ""
                assert fk.referenced_column != ""

                print(
                    f"    {fk.column}"
                    f" -> "
                    f"{fk.referenced_table}.{fk.referenced_column}"
                )

    print("\n========== Scanner Test Passed ==========")


if __name__ == "__main__":
    test_schema_scanner()