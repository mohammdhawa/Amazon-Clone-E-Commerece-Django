from django.urls import path
from .views import ProductDetail, ProductList, BrandList, BrandDetail, mydebug, add_review

from . import api


urlpatterns = [
    path('mydebug/', mydebug, name='mydebug'),
    path('', ProductList.as_view(), name='product_list'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    path('brands/<slug:slug>/', BrandDetail.as_view(), name='brand_detail'),
    path("<slug:slug>/", ProductDetail.as_view(), name='product_detail'),
    path("<slug:slug>/add_review/", add_review, name='add_review'),

    # API urls
    path('api/list', api.ProductListAPI.as_view(), name='product_list_api'),
    path('api/list/brands/', api.BrandListAPI.as_view(), name='brand_list_api'),
    path('api/list/brands/<int:pk>/', api.BrandDetailAPI.as_view(), name='brand_detail_api'),
    path('api/list/<int:pk>/', api.ProductDetailAPI.as_view(), name='product_detail_api'),
]
