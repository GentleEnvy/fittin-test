from typing import Protocol

from app.categories.dtos.categories import CategoryDTO
from app.categories.models import Category


class _CategoryManagerType(Protocol):
    def get(self, *, id: int) -> Category:
        pass

    def create(self, *, id: int, name: str, parent: Category = None) -> Category:
        pass


class CategoryFactory:
    def __init__(self):
        self.manager: _CategoryManagerType = Category.objects

    def create(self, category_dto: CategoryDTO) -> Category:
        return self._create(category_dto)

    def _create(self, category_dto: CategoryDTO, parent: Category = None) -> Category:
        category = self._update_or_create(category_dto, parent)
        for child_dto in category_dto.children:
            self._create(child_dto, category)
        return category

    def _update_or_create(
        self, category_dto: CategoryDTO, parent: Category = None
    ) -> Category:
        try:
            category = self.manager.get(id=category_dto.id)
            category.name = category_dto.name
            category.parent = parent
            category.save()
        except Category.DoesNotExist:
            category = self.manager.create(
                id=category_dto.id, name=category_dto.name, parent=parent
            )
        return category
