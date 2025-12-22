from django.urls import path
from .views import UserDetailView, RegisterView, LoginView

from . import views

urlpatterns = [
    path("echo/", views.handle_echo, name='handle_echo'),
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name='login'),
    path("<str:id>/", UserDetailView.as_view(), name='user_detail'),
]