from dataclasses import dataclass


@dataclass
class TimeRange:

    start: str | None = None

    end: str | None = None

    last_n_days: int | None = None

    today: bool = False