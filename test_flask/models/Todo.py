from dataclasses import dataclass


@dataclass
class Todo:
    title: str
    completed: bool
