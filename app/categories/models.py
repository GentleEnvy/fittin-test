from django.db import models

from app.base.models.base import AbstractModel


class Category(AbstractModel):
    id = models.BigIntegerField(primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField()
