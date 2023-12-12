from django.urls import path, include
from catalog.views import *

app_name = 'catalog'

urlpatterns = [
    path('', CatalogListView.as_view(), name='catalog'),
    path('product/<int:product_id>', ProductDetailView.as_view(), name='product'),
]
