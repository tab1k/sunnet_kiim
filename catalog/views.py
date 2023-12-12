from django.shortcuts import get_object_or_404
from django.views.generic import *
from catalog.models import *


class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'catalog'
    paginate_by = 16


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/catalog_single.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product_id = self.kwargs['product_id']
        return get_object_or_404(Product, id=product_id)