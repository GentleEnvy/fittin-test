from app.products.models import Product


class ProductCategoriesService:
    def rebuild(self, product: Product) -> None:
        product.categories.clear()
        category = product.basic_category
        while category is not None:
            product.categories.add(category)  # noqa:
            # https://youtrack.jetbrains.com/issue/PY-15277#
            category = category.parent
