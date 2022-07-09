from django.core.management.base import BaseCommand

from app.categories.factories.categories import CategoryFactory
from app.categories.parsers.xml import CategoryXMLParser


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.parser = CategoryXMLParser()
        self.factory = CategoryFactory()

    def handle(self, *args, **options):
        match options:
            case {'filename': str(filename)}:
                category_dtos = self.parser.parse_from_file(filename)
            case _:
                category_dtos = self.parser.parse_from_file()
        for category_dto in category_dtos:
            self.factory.create(category_dto)

    def add_arguments(self, parser):
        parser.add_argument('--filename', type=str, default=None)
