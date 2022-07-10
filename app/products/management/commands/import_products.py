from django.core.management.base import BaseCommand

from app.products.factories.products import ProductFactory
from app.products.parsers.xml import ProductXMLParser


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.parser = ProductXMLParser()
        self.factory = ProductFactory()

    def handle(self, *args, **options):
        match options:
            case {'filename': str(filename)}:
                product_dtos = self.parser.parse_from_file(filename)
            case _:
                product_dtos = self.parser.parse_from_file()
        for product_dto in product_dtos:
            self.factory.create(product_dto)

    def add_arguments(self, parser):
        parser.add_argument('--filename', type=str, default=None)
