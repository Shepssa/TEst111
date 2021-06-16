from django.urls import path
from ecommerce_shop.views import CatalogView, CatalogDeepView, ProductView, ThanksView

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('catalog/<str:slug>/<str:product_slug>/', ProductView.as_view(), name='product'),
    path('catalog/<str:slug>/', CatalogDeepView.as_view(), name='catalog_deep'),
]
