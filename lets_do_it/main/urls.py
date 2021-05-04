from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login_user', views.login),
    path('registration', views.registration),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('new_task', views.new_task),
    path('create_task', views.create_task),
    path('add_task/<int:id>', views.add_task),
    path('remove_task/<int:id>', views.remove_task),
    path('abandon/<int:id>', views.abandon),
    path('complete/<int:id>', views.complete),
    path('home', views.home),
]