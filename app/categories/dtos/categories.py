from __future__ import annotations

import dataclasses

from app.base.dtos.base import BaseDTO


@dataclasses.dataclass
class CategoryDTO(BaseDTO):
    id: int
    name: str
    children: set[CategoryDTO] = dataclasses.field(default_factory=set)

    def __hash__(self):
        return self.id
