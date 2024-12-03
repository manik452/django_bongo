from django.urls import path
from . import views

urlpatterns = [
    path("", views.receipe_home),
    path("login", views.login_page),
    path("logout", views.logout_page),
    path("register", views.register),
    path("delete/<id>", views.delete_receipe),
]
