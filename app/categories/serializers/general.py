from rest_framework import serializers

from app.base.serializers.fields.base64.recursive import RecursiveListField
from app.categories.models import Category


class GET_CategoriesSerializer(serializers.ModelSerializer):
    children = RecursiveListField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'children']
