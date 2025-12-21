from django.db import models
import uuid

# Create your models here.
class Topic(models.Model):
    topic_id    =   models.UUIDField(
        primary_key =   True,
        default     =   uuid.uuid4, 
        editable    =   False
    )

    title           =   models.CharField(max_length = 128)
    description     =   models.CharField(max_length = 254)


class Question(models.Model):
    question_id     =   models.UUIDField(
        primary_key =   True,
        default     =   uuid.uuid4, 
        editable    =   False
    )
    
    topic_id    =   models.ForeignKey(Topic, on_delete=models.CASCADE)
    content     =   models.TextField()
    answer_key  =   models.CharField(max_length = 128)
    difficulty  =   models.CharField(max_length = 128)
    pub_date    =   models.DateTimeField("date published")


class Choice(models.Model):
    question_id     =   models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text     =   models.CharField(max_length = 200)