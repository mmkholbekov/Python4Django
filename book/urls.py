from django.urls import path
from . import views

urlpatterns = [
    path('book_link', views.book_view, name='book'),
    path('book_link/<int:id>/', views.book_detail_view, name='details'),
]
