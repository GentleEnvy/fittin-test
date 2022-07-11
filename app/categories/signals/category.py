from django.db.models.signals import post_save
from django.dispatch import receiver

from app.categories.models import Category
from app.products.services.product_categories import ProductCategoriesService


@receiver(post_save, sender=Category)
def categories_category_post_save(instance, created, *_, **__):
    product_categories_service = ProductCategoriesService()
    rebuilt_products = set()

    def _rebuild(_category):
        for _product in _category.products.all():
            if _product not in rebuilt_products:
                product_categories_service.rebuild(_product)
                rebuilt_products.add(_product)
        for _child in _category.children.all():
            _rebuild(_child)

    if not created:
        _rebuild(instance)
