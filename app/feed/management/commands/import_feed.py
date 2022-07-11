from django.core.management.base import BaseCommand

from app.categories.factories.categories import CategoryFactory
from app.categories.parsers.xml import CategoryXMLParser
from app.products.factories.products import ProductFactory
from app.products.parsers.xml import ProductXMLParser


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.category_parser = CategoryXMLParser()
        self.category_factory = CategoryFactory()
        self.product_parser = ProductXMLParser()
        self.product_factory = ProductFactory()

    def handle(self, *args, **options):
        match options:
            case {'filename': str(filename)}:
                category_dtos = self.category_parser.parse_from_file(filename)
                product_dtos = self.product_parser.parse_from_file(filename)
            case _:
                category_dtos = self.category_parser.parse_from_file()
                product_dtos = self.product_parser.parse_from_file()
        for category_dto in category_dtos:
            self.category_factory.create(category_dto)
        for product_dto in product_dtos:
            self.product_factory.create(product_dto)

    def add_arguments(self, parser):
        parser.add_argument('--filename', type=str, default=None)
