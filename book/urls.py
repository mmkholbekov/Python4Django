from django.urls import path
from . import views

urlpatterns = [
    path('book_link', views.book_view, name='book'),
    path('book_link/<int:id>/', views.book_detail_view, name='details'),
    path('book_link/<int:id>/update/', views.update_book_view, name='update'),
    path('book_link/<int:id>/delete/', views.delete_book_view, name='delete'),
    path('add-book/', views.create_book_view, name='create'),
]
