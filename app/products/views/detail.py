from django.db.models import Prefetch
from rest_framework.mixins import RetrieveModelMixin

from app.base.views.base import BaseView
from app.products.models import Offer, Product
from app.products.serializers.detail import GET_ProductSerializer


class ProductView(RetrieveModelMixin, BaseView):
    serializer_map = {'get': GET_ProductSerializer}
    queryset = Product.objects.prefetch_related(
        Prefetch('offers', Offer.objects.prefetch_related('pictures', 'params'))
    )

    def get(self, request, **_):
        return self.retrieve(request)
