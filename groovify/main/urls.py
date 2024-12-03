# main/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('register_user/', views.register_user_view, name='register_user'),
    path('login/', views.login_view, name='login'),
    path('home_user/', views.home_user, name='home_user'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
