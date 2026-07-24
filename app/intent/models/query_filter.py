from dataclasses import dataclass


@dataclass
class QueryFilter:

    field: str

    operator: str

    value: str