from django.urls import path
from questions.views import TopicListView

from . import views

urlpatterns = [
    path("topics/", TopicListView.as_view(), name='topics'),
]