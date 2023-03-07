from django.urls import path
from . import views

app_name = 'parse'
urlpatterns = [
    path('movie_list/', views.ParserView.as_view(), name='movie_list'),
    path('parsing/', views.ParserFormView.as_view(), name='parser_film'),

]