from . import views
from django.urls import path

urlpatterns = [
    path('list_task', views.list_task, name='list_task'),
    path('task/new/', views.add_task, name='add_task'),
    path('task/<int:id>/', views.detail_task, name='detail_task'),
    path('task/edit/<int:id>/', views.edit_task, name='edit_task'),
    path('task/delete/<int:id>/', views.delete_task, name='delete_task'),
    path('task/completed/<int:id>/', views.task_completed, name='task_completed'),
]
