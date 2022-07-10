import dataclasses

from app.base.dtos.base import BaseDTO
from app.categories.models import Category
from app.products.dtos.offers import OfferDTO


@dataclasses.dataclass
class ProductDTO(BaseDTO):
    basic_category: Category
    model: str
    offers: set[OfferDTO] = dataclasses.field(default_factory=set)

    def __hash__(self):
        return hash(self.model)
