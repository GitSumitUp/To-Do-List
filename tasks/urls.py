from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_task, name='add_task'),  
    path('view/', views.task_list, name='task_list'), 
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'), 
]