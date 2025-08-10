from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('task/add/', views.add_task_view, name='add_task'),
    path('task/<int:task_id>/edit/', views.edit_task_view, name='edit_task'),
    path('task/<int:task_id>/delete/', views.delete_task_view, name='delete_task'),
    path('task/<int:task_id>/toggle/', views.toggle_task_completion, name='toggle_task'),
] 