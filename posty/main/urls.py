from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("add_user", views.add_user),
    path("chat", views.chat),
    path("login_page", views.login_page),
    path("login", views.login),
    path("new_post", views.new_post),
    path("edit_post/<int:id>", views.edit_post),
    path("update_post", views.update_post),
    path("delete_post/<int:id>", views.delete_post),
    path("logout", views.logout),
    path("add_favorite/<int:post_id>", views.add_favorite),
]