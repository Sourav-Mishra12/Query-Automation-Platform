from dataclasses import dataclass, field


@dataclass(slots=True)
class NormalizedQuery:
    original: str
    normalized: str
    tokens: list[str] = field(default_factory=list)

@dataclass(slots=True)
class MetadataSearchResult:
    matched_tables: list[dict] = field(default_factory=list)
    matched_columns: list[dict] = field(default_factory=list)

    matched_terms: list[str] = field(default_factory=list)
    unmatched_terms: list[str] = field(default_factory=list)

    coverage_score: float = 0.0