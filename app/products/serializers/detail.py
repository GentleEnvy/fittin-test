from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from app.products.models import Offer, Product


class _GET_Product__OffersSerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField()
    params = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = [
            'id',
            'name',
            'simular',
            'price',
            'price_begin',
            'percent',
            'vat',
            'vendor_code',
            'description',
            'barcode',
            'pictures',
            'params',
        ]

    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_pictures(self, offer):
        return [picture.url for picture in offer.pictures.all()]

    @extend_schema_field(
        serializers.DictField(child=serializers.CharField(allow_null=True))
    )
    def get_params(self, offer):
        return {param.name: param.value for param in offer.params.all()}


class GET_ProductSerializer(serializers.ModelSerializer):
    offers = _GET_Product__OffersSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'model', 'categories', 'offers']
