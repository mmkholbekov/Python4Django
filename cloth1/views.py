from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ProductListView(ListView):
    queryset = models.Product.objects.filter().order_by("-id")

    template_name = "clothes_list.html"

    def get_queryset(self):
        return models.Product.objects.filter().order_by("-id")


class BabyListlView(DetailView):
    queryset = models.Product.objects.filter(tags__name="Рубашки")
    template_name = "baby_list.html"
    success_url = "/baby_cloth/"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return models.Product.objects.filter(tags__name="Рубашки")


class MenListlView(DetailView):
    queryset = models.Product.objects.filter(tags__name="Брюки")
    template_name = "men_list.html"
    success_url = "/men_cloth/"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return models.Product.objects.filter(tags__name="Брюки")


class WomenListlView(DetailView):
    queryset = models.Product.objects.filter(tags__name="Платье")
    template_name = "women_list.html"
    success_url = "/women_cloth/"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return models.Product.objects.filter(tags__name="Платье")


class ElectronicsListlView(DetailView):
    queryset = models.Product.objects.filter(tags__name="Lenovo i5")
    template_name = "electronics_list.html"
    success_url = "/electronics/"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return models.Product.objects.filter(tags__name="Lenovo i5")


class OrderCreateView(CreateView):
    template_name = "add-order.html"
    form_class = forms.OrderForm
    success_url = "/add-order/"
    queryset = models.Order.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)
