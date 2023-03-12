from django.urls import path
from . import views

urlpatterns = [
    path("cloth/", views.ProductListView.as_view(), name="cloth"),
    path("baby_cloth/", views.BabyListlView.as_view(), name="baby_cloth"),
    path("men_cloth/", views.MenListlView.as_view(), name="men_cloth"),
    path("women_cloth/", views.WomenListlView.as_view(), name="women_cloth"),
    path("electronics/", views.ElectronicsListlView.as_view(), name="electronics"),
    path("add-order/", views.OrderCreateView.as_view(), name="add"),
]
