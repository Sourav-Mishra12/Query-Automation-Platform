from dataclasses import dataclass


@dataclass
class Aggregation:

    function: str

    target: str