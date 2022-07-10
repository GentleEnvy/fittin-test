from abc import ABC
from typing import Generic, TypeVar
from xml.etree import ElementTree
from xml.etree.ElementTree import Element


T = TypeVar('T')


class BaseXMLParser(ABC, Generic[T]):
    def parse_from_file(self, filename: str = 'feed.xml') -> set[T]:
        element_tree = ElementTree.parse(filename)
        return self._parse(element_tree.getroot())

    def _parse(self, element_root: Element):
        raise NotImplementedError
