from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list_view, name='movie_list'),
    path('add/', views.movie_create_view, name='movie_create'),  # Это важный маршрут
]
