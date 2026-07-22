from dataclasses import dataclass, field


@dataclass
class TableEnrichment:
    """
    AI-generated business metadata for a database table.
    """

    description: str = ""
    synonyms: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)


@dataclass
class ColumnEnrichment:
    """
    AI-generated business metadata for a database column.
    """

    description: str = ""
    synonyms: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)