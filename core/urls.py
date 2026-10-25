from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),       # Membuka halaman utama (http://127.0.0.1:8000/)
    path('home', views.home, name='home'),   # Membuka via (http://127.0.0.1:8000/home)
    path('media/<int:pk>/', views.media_detail, name='media_detail'), # Membuka halaman detail media (http://127.0.0.1:8000/media/1/)
    path('media/', views.media, name='media'), # Membuka halaman media (http://127.0.0.1:8000/media/)
    path('news/', views.news, name='news'), # Membuka halaman berita (http://127.0.0.1:8000/news/)
    path('base/', views.base_test, name='base_test'), #test media
]