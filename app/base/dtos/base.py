from __future__ import annotations

from dataclasses import asdict, dataclass

from app.base.models.base import AbstractModel


@dataclass
class BaseDTO:
    @classmethod
    def from_model(cls, instance: AbstractModel, **fields_map: str) -> BaseDTO:
        data = {}
        # noinspection PyUnresolvedReferences
        for field_name in cls.__dataclass_fields__:
            field_name = fields_map.get(field_name, field_name)
            data[field_name] = getattr(instance, field_name)
        # noinspection PyArgumentList
        return cls(**data)

    def __iter__(self):
        return iter(asdict(self).items())
