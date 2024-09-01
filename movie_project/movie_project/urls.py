from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('films.urls')),
    path('', lambda request: redirect('movie_list')),  # Перенаправление с корневого URL на список фильмов
]
