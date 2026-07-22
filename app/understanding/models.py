from dataclasses import dataclass, field


@dataclass(slots=True)
class NormalizedQuery:
    original: str
    normalized: str
    tokens: list[str] = field(default_factory=list)

    