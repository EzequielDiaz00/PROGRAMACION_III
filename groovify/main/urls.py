# main/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('register_user/', views.register_user_view, name='register_user'),
    path('register_artist/', views.register_artist_view, name='register_artist'),
    path('login/', views.login_view, name='login'),
    path('home_user/', views.home_user, name='home_user'),
    path('home_artist/', views.home_artist, name='home_artist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
