from django.urls import path

from . import views

urlpatterns = [
    path("echo", views.handle_echo, name="handle_echo"),
    path("register", views.handle_register, name="handle_register"),
]