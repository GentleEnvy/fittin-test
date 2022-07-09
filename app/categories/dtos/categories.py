import dataclasses
from typing import Any

from app.base.dtos.base import BaseDTO


@dataclasses.dataclass
class CategoryDTO(BaseDTO):
    id: int
    name: str
    children: Any = dataclasses.field(default_factory=set)  # set[CategoryDTO]

    def __hash__(self):
        return self.id
