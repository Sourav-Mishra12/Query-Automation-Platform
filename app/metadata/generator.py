"""
Converts the discovered database schema into a metadata document
that can be consumed by the Metadata Repository and Query Engine.
"""


from app.metadata.models import DatabaseSchema
from app.metadata.models import TableSchema
from app.metadata.models import ColumnSchema



class MetadataGenerator:
    

    def generate(self, schema: DatabaseSchema) -> dict:
        """
        Generates metadata from a discovered database schema.

        """

        metadata = {
            "database" : schema.database_name,
            "tables" : [],
        }

        for table in schema.tables:

            metadata["tables"].append(
                self._generate_table_metadata(table)
            )

        return metadata 
    

    def _generate_table_metadata(
                    self,
                    table: TableSchema,
             ) -> dict:
     """
     Generates metadata for a single table.
     """

     return {
        "name": table.name,
        "description": "",
        "entity_type": "table",
        "columns": [
            self._generate_column_metadata(column)
            for column in table.columns
        ],
        "relationships": [
            {
                "column": fk.column,
                "references": f"{fk.referenced_table}.{fk.referenced_column}",
            }
            for fk in table.foreign_keys
        ],
    }



    def _generate_column_metadata(
             self,
            column: ColumnSchema,
              ) -> dict:
     """
     Generates metadata for a single column.
     """
     return {
        "name": column.name,
        "data_type": column.data_type,
        "nullable": column.nullable,
        "primary_key": column.is_primary_key,
        "foreign_key": column.is_foreign_key,
        "default": column.default_value,
        "description": "",
        "synonyms": [],
        "tags": [],
    }