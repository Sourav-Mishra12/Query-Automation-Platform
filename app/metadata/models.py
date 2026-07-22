
"""
Defines the core schema models used throughout the Metadata Platform.
These models represent the discovered database structure and act as the
contract between the Schema Scanner, Metadata Generator, and Repository.
"""


from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ColumnSchema:
    name: str
    data_type: str
    nullable: bool
    is_primary_key: bool = False
    is_foreign_key: bool = False
    default_value: Optional[str] = None


@dataclass
class ForeignKeySchema:
    column: str
    referenced_table: str
    referenced_column: str


@dataclass
class TableSchema:
    name: str
    columns: List[ColumnSchema] = field(default_factory=list)
    foreign_keys: List[ForeignKeySchema] = field(default_factory=list)


@dataclass
class DatabaseSchema:
    database_name: str
    tables: List[TableSchema] = field(default_factory=list)