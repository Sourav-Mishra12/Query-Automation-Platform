from dataclasses import dataclass


@dataclass
class SqlPrompt:
    system_prompt: str
    user_prompt: str