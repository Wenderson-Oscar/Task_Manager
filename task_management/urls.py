from . import views
from django.urls import path

urlpatterns = [
    path('', views.list_task, name='home'),
    path('task/new/', views.add_task, name='add_task'),
]