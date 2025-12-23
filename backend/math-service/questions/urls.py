from django.urls import path
from questions.views import TopicListView, QuestionDetailView

from . import views

urlpatterns = [
    path("topics/", TopicListView.as_view(), name='topics'),
    path("<str:question_slug>/", QuestionDetailView.as_view(), name='question_detail'),
]