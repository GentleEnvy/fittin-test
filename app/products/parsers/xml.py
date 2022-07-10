from typing import Protocol
from xml.etree.ElementTree import Element

from inflection import underscore

from app.base.parsers.xml.base import BaseXMLParser
from app.categories.models import Category
from app.products.dtos.offers import OfferDTO
from app.products.dtos.proucts import ProductDTO


class _CategoryManager(Protocol):
    def get(self, *, id: int) -> Category:
        pass


class ProductXMLParser(BaseXMLParser[ProductDTO]):
    def __init__(self):
        super().__init__()
        self.category_manager: _CategoryManager = Category.objects

    def _parse(self, element_root):
        model_product_map: dict[str, ProductDTO] = {}
        for element_offer in element_root[0][1]:  # root -> shop -> (categories, offers)
            offer_dto = self._parse_offer(element_offer)
            model = [e for e in element_offer if e.tag == 'model'][0].text
            if (product_dto := model_product_map.get(model)) is None:
                product_dto = self._parse_product(element_offer)
                model_product_map[model] = product_dto
            product_dto.offers.add(offer_dto)
        return set(model_product_map.values())

    def _parse_product(self, element_offer: Element):
        kwargs = {}
        for element_field in element_offer:
            tag = underscore(element_field.tag)
            match tag:
                case 'model':
                    kwargs[tag] = element_field.text
                case 'category_id':
                    kwargs['basic_category'] = self.category_manager.get(
                        id=int(element_field.text)
                    )
        return ProductDTO(**kwargs)

    def _parse_offer(self, element_offer: Element):
        kwargs = {'id': int(element_offer.attrib['id'])}
        for element_field in element_offer:
            tag = underscore(element_field.tag)
            match tag:
                case 'price' | 'price_begin' | 'percent' | 'vat':
                    kwargs[tag] = int(element_field.text)
                case 'name' | 'simular' | 'vendor_code' | 'description' | 'barcode':
                    kwargs[tag] = element_field.text
        offer_dto = OfferDTO(**kwargs)
        for element_field in element_offer:
            tag = underscore(element_field.tag)
            match tag:
                case 'picture':
                    offer_dto.pictures.add(element_field.text)
                case 'param':
                    offer_dto.params[element_field.attrib['name']] = element_field.text
        return offer_dto
