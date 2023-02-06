from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('register/new', views.register_client, name='register'),
    path('authenticate_client', views.authenticate_client, name='authenticate_client'),
]