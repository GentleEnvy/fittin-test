from rest_framework.mixins import ListModelMixin

from app.base.views.base import BaseView
from app.categories.models import Category
from app.categories.serializers.general import GET_CategoriesSerializer


class CategoriesView(ListModelMixin, BaseView):
    serializer_map = {'get': GET_CategoriesSerializer}
    queryset = Category.objects.filter(parent__isnull=True)

    def get(self, request):
        return self.list(request)
