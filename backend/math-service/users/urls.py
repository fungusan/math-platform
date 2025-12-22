from django.urls import path
from .views import UserDetailView, RegisterView

from . import views

urlpatterns = [
    path("echo/", views.handle_echo, name='handle_echo'),
    path("<str:id>/", UserDetailView.as_view(), name='user_detail'),
    path("register/", RegisterView.as_view(), name='register'),
]