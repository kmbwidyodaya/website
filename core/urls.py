from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),       # Membuka halaman utama (http://127.0.0.1:8000/)
    path('home', views.home, name='home'),   # Membuka via (http://127.0.0.1:8000/home)
]