from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('album/<int:id>', views.album, name='album'),
    path('search/', views.search, name='search')
    ]
