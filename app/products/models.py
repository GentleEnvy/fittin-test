from django.db import models

from app.base.models.base import AbstractModel
from app.categories.models import Category


class ProductCategories(AbstractModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_categories'
        unique_together = ('product', 'category')


class Product(AbstractModel):
    basic_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products_by_basic_category'
    )
    model = models.TextField(unique=True)
    categories = models.ManyToManyField(
        Category, through=ProductCategories, related_name='products'
    )


class Offer(AbstractModel):
    id = models.BigIntegerField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='offers'
    )
    name = models.TextField()
    simular = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    price_begin = models.IntegerField()
    percent = models.IntegerField()
    vat = models.IntegerField()
    vendor_code = models.TextField()
    description = models.TextField()
    barcode = models.TextField()


class OfferPicture(AbstractModel):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='pictures')
    url = models.URLField()


class OfferParam(AbstractModel):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='params')
    name = models.TextField()
    value = models.TextField(null=True, blank=True)
