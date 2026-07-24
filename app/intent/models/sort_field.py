from dataclasses import dataclass


@dataclass
class SortField:

    target: str

    descending: bool = False