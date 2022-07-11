from django.db.models.signals import post_save
from django.dispatch import receiver

from app.products.models import Product
from app.products.services.product_categories import ProductCategoriesService


@receiver(post_save, sender=Product)
def products_product_post_save(instance, *_, **__):
    ProductCategoriesService().rebuild(instance)
