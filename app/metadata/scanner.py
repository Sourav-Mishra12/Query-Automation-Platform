"""
Discovers the database schema by inspecting tables, columns, and relationships.
Returns a structured DatabaseSchema object without applying any business logic.
"""

from sqlalchemy import inspect
from sqlalchemy.engine import Engine

from app.metadata.models import (
    ColumnSchema,
    DatabaseSchema,
    ForeignKeySchema,
    TableSchema,
)

class SchemaScanner:
    """
    Reads database metadata using SQLAlchemy's inspection API.
    """

    def __init__(self, engine: Engine):
        self.engine = engine
        self.inspector = inspect(engine)

    
    def scan(self) -> DatabaseSchema:
     """
      Scans the database and returns its schema.
    """

     tables = self._scan_tables()

     return DatabaseSchema(
        database_name=self.engine.url.database or "Unknown",
        tables=tables,
    )


    def scan(self) -> DatabaseSchema:
     """
     Scans the database and returns its schema.
    """

     tables = self._scan_tables()

     return DatabaseSchema(
        database_name=self.engine.url.database or "Unknown",
        tables=tables,
    )


    def _scan_tables(self) -> list[TableSchema]:
     """
     Scans all database tables.
     """

     tables = []

     for table_name in self.inspector.get_table_names():

        table = TableSchema(
            name=table_name,
            columns=self._scan_columns(table_name),
            foreign_keys=self._scan_foreign_keys(table_name),
        )

        tables.append(table)

     return tables
    

    def _scan_columns(self, table_name: str) -> list[ColumnSchema]:
     """
     Scans all columns of a table.
     """
     return []
    
    
    def _scan_foreign_keys(self, table_name: str) -> list[ForeignKeySchema]:
     """
     Scans all foreign keys of a table.
     """
     return []
    

    def _scan_columns(self, table_name: str) -> list[ColumnSchema]:
      """
        Scans all columns of a table.
      """

      columns = []

      primary_keys = set(
         self.inspector.get_pk_constraint(table_name).get("constrained_columns", [])
       )

      foreign_keys = {
        fk["constrained_columns"][0]
        for fk in self.inspector.get_foreign_keys(table_name)
        if fk.get("constrained_columns")
       }

      for column in self.inspector.get_columns(table_name):

        columns.append(
            ColumnSchema(
                name=column["name"],
                data_type=str(column["type"]),
                nullable=column["nullable"],
                default_value=column.get("default"),
                is_primary_key=column["name"] in primary_keys,
                is_foreign_key=column["name"] in foreign_keys,
            )
        )

      return columns
    

    def _scan_foreign_keys(self, table_name: str) -> list[ForeignKeySchema]:
     """
     Scans all foreign key relationships of a  table.
     """

     foreign_keys = []

     for fk in self.inspector.get_foreign_keys(table_name):

        constrained_columns = fk.get("constrained_columns", [])
        referred_columns = fk.get("referred_columns", [])

        if not constrained_columns or not referred_columns:
            continue

        foreign_keys.append(
            ForeignKeySchema(
                column=constrained_columns[0],
                referenced_table=fk["referred_table"],
                referenced_column=referred_columns[0],
            )
        )

     return foreign_keys