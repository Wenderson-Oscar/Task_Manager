from . import views
from django.urls import path

urlpatterns = [
    path('list_task/', views.list_task, name='list_task'),
    path('task/new/', views.add_task, name='add_task'),
    path('task/<int:id>/', views.detail_task, name='detail_task'),
    path('task/edit/<int:id>/', views.edit_task, name='edit_task'),
    path('task/<int:id>/delete/', views.confirm_delete_task, name='confirm_delete_task'),
    path('task/<int:id>/delete/confirmed/', views.delete_task, name='delete_task'),
    path('task/<int:id>/completed/', views.confirm_completed_task, name='confirm_completed_task'),
    path('task/<int:id>/completd/confirmed/', views.task_completed, name='task_completed'),
]
