from rest_framework import serializers

from app.categories.models import Category
from app.products.models import Product


class POST_ProductsSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        extra_kwargs = {'category': {'write_only': True}, 'model': {'read_only': True}}
        fields = ['category', 'id', 'model']
