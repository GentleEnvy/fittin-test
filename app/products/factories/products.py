from app.products.dtos.proucts import ProductDTO
from app.products.factories.offers import OfferFactory
from app.products.models import Product


class ProductFactory:
    def __init__(self):
        self.manager = Product.objects
        self.offer_factory = OfferFactory()

    def create(self, product_dto: ProductDTO) -> Product:
        try:
            product = self.manager.get(model=product_dto.model)
            product.basic_category = product_dto.basic_category
            product.save()
        except Product.DoesNotExist:
            product = self.manager.create(
                model=product_dto.model, basic_category=product_dto.basic_category
            )
        for offer_dto in product_dto.offers:
            self.offer_factory.create(offer_dto, product)
        return product
