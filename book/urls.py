from django.urls import path
from . import views

urlpatterns = [
    path('book_link/', views.BookView.as_view(), name='book'),
    path('book_link/<int:id>/', views.BookDetailView.as_view(), name='detail'),
    path('book_link/<int:id>/update/', views.BookUpdateView.as_view(), name='update'),
    path('book_link/<int:id>/delete/', views.BookDeleteView.as_view(), name='delete'),
    path('add-book/', views.BookCreateView.as_view(), name='create'),
    path('add-comment/', views.CreateCommentView.as_view(), name='comment'),
]
