from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SessionViewSet  # Import your ViewSet

router = DefaultRouter()
router.register(r'sessions', SessionViewSet, basename='session')  # basename for reverse URLs

urlpatterns = router.urls  # This includes all generated paths (e.g., /sessions/, /sessions/{pk}/, /sessions/{pk}/edit/)