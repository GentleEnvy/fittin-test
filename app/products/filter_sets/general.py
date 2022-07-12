from django.db.models import *

from app.base.filters.base import IntegerFilter
from app.base.filters.filtersets.base import BaseFilterSet
from app.products.models import Offer, Product


class ProductsFilterSet(BaseFilterSet):
    price__lte = IntegerFilter(method='filter_price__lte', label='price__lte')
    price__gte = IntegerFilter(method='filter_price__gte', label='price__gte')

    class Meta:
        model = Product
        fields = {}

    @staticmethod
    def filter_price__lte(queryset, _, value):
        return queryset.annotate(
            max_price=Subquery(
                Offer.objects.filter(product_id=OuterRef('id'))
                .order_by('-price')
                .values('price')[:1]
            )
        ).filter(max_price__lte=value)

    @staticmethod
    def filter_price__gte(queryset, _, value):
        return queryset.annotate(
            min_price=Subquery(
                Offer.objects.filter(product_id=OuterRef('id'))
                .order_by('price')
                .values('price')[:1]
            )
        ).filter(min_price__lte=value)
