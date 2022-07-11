from django.core.management.base import BaseCommand

from app.categories.factories.categories import CategoryFactory
from app.categories.parsers.xml import CategoryXMLParser
from app.products.factories.products import ProductFactory
from app.products.parsers.xml import ProductXMLParser


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.feed_filename = 'feed.xml'
        self.category_parser = CategoryXMLParser()
        self.category_factory = CategoryFactory()
        self.product_parser = ProductXMLParser()
        self.product_factory = ProductFactory()

    def handle(self, *args, **options):
        filename = options.get('filename') or self.feed_filename
        for category_dto in self.category_parser.parse_from_file(filename):
            self.category_factory.create(category_dto)
        for product_dto in self.product_parser.parse_from_file(filename):
            self.product_factory.create(product_dto)

    def add_arguments(self, parser):
        parser.add_argument('--filename', type=str, default=None)
