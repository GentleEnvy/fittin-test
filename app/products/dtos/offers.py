import dataclasses

from app.base.dtos.base import BaseDTO


@dataclasses.dataclass()
class OfferDTO(BaseDTO):
    id: int
    name: str
    simular: str | None
    price: int
    price_begin: int
    percent: int
    vat: int
    vendor_code: str
    description: str
    barcode: str
    pictures: set[str] = dataclasses.field(default_factory=set)
    params: dict[str, str] = dataclasses.field(default_factory=dict)

    def __hash__(self):
        return self.id
