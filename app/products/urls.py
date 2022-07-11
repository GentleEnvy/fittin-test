from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductsView.as_view()),
    path('<int:id>/', ProductView.as_view()),
]
