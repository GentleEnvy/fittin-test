from collections import defaultdict

from app.base.parsers.xml.base import BaseXMLParser
from app.categories.dtos.categories import CategoryDTO


class CategoryXMLParser(BaseXMLParser[CategoryDTO]):
    def _parse(self, element_root):
        root_categories: set[CategoryDTO] = set()
        child_categories: dict[int, set[CategoryDTO]] = defaultdict(set)
        for element_category in element_root[0][0]:  # root -> shop -> categories
            category_dto = CategoryDTO(
                id=int(element_category.attrib['id']), name=element_category.text
            )
            if (str_parent_id := element_category.attrib.get('parentId')) is None:
                root_categories.add(category_dto)
            else:
                child_categories[int(str_parent_id)].add(category_dto)

        def set_children(_root_category: CategoryDTO):
            _root_category.children = child_categories[_root_category.id]
            for _child in _root_category.children:
                set_children(_child)

        for root_category in root_categories:
            set_children(root_category)
        return root_categories
