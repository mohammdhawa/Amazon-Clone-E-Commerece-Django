from django.urls import path
from .views import ProductDetail, ProductList


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path("<slug:slug>/", ProductDetail.as_view(), name='product_detail'),
]
