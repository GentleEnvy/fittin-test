from rest_framework.mixins import ListModelMixin

from app.base.views.base import BaseView
from app.products.filter_sets.general import ProductsFilterSet
from app.products.models import Product
from app.products.serializers.general import POST_ProductsSerializer


class ProductsView(ListModelMixin, BaseView):
    serializer_map = {'post': POST_ProductsSerializer}
    queryset = Product.objects.all()
    filterset_class = ProductsFilterSet

    def post(self, request):
        return self.list(request)

    def filter_queryset(self, queryset):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return (
            super()
            .filter_queryset(queryset)
            .filter(categories=serializer.validated_data['category'])
        )
