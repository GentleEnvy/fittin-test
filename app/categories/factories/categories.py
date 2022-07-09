from typing import Protocol

from app.categories.dtos.categories import CategoryDTO
from app.categories.models import Category


class _CategoryManagerType(Protocol):
    def create(self, *, id: int, name: str, parent: Category = None) -> Category:
        pass


class CategoryFactory:
    def __init__(self):
        self.manager: _CategoryManagerType = Category.objects

    def create(self, category_dto: CategoryDTO) -> Category:
        category = self.manager.create(id=category_dto.id, name=category_dto.name)
        for child_dto in category_dto.children:
            self._create_child(child_dto, category)
        return category

    def _create_child(self, category_dto: CategoryDTO, parent: Category) -> None:
        child = self.manager.create(
            id=category_dto.id, name=category_dto.name, parent=parent
        )
        for child_dto in category_dto.children:
            self._create_child(child_dto, child)
