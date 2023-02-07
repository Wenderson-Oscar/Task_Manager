from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    #cadastro/login/logout/autenticar do cliente
    path('register/new/', views.register_client, name='register'),
    path('authenticate_client', views.authenticate_client, name='authenticate_client'),
    path('login_client', views.login_client, name='login_client'),
    path('logout_client', views.logout_client, name='logout_client'),
]