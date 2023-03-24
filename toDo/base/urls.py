from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.registerUser, name = 'register'),

    path('', views.homepage, name='home'),
    path('task/<str:pk>/', views.Taskpage, name='task'),

    path('create-task/', views.createTask, name='create-task'),
    path('edit-task/<str:pk>/', views.editTask, name='edit-task'),
    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task')
]