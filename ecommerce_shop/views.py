from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.edit import FormMixin
from ecommerce_shop.utils import PaginationMixin
from ecommerce_shop.models import Product
from django.shortcuts import get_object_or_404
from inbox.forms import InboxForm


class CatalogView(PaginationMixin, ListView):
    model = Product
    queryset = Product.objects.filter(draft=False)
    template_name = 'ecommerce_shop/ecommerce_shop-view.html'


class CatalogDeepView(PaginationMixin, ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get('slug'))

    template_name = 'ecommerce_shop/ecommerce_shop-view.html'


class ProductView(FormMixin, DetailView):
    model = Product
    form_class = InboxForm
    success_url = '/thanks/'

    @property
    def get_product(self):
        return get_object_or_404(Product, slug=self.kwargs.get('product_slug'))

    def get_object(self, *args, **kwargs):
        product = self.get_product
        return product

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.product = self.get_product
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form)

    template_name = 'ecommerce_shop/ecommerce_shop_product-view.html'


class ThanksView(TemplateView):
    template_name = 'ecommerce_shop/ecommerce_shop_thanks-view.html'
