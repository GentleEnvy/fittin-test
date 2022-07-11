from django.db.models import Manager
from rest_framework.fields import ListField
from rest_framework_recursive.fields import RecursiveField


class RecursiveListField(ListField):
    def __init__(self, **kwargs):
        kwargs.setdefault('child', RecursiveField())
        super().__init__(**kwargs)

    def get_attribute(self, instance):
        attr = super().get_attribute(instance)
        if isinstance(attr, Manager):
            return attr.all()
        return attr
