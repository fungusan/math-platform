from django.urls import path

from . import views

urlpatterns = [
    path("", views.handle_register, name="handle_register"),
]