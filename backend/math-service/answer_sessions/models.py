from django.db import models
from django.utils import timezone
from users.models import User
from questions.models import Question


# Create your models here.
class Session(models.Model):
    user_id     =   models.ForeignKey(User, on_delete=models.CASCADE)
    start_at    =   models.DateTimeField("date published")
    end_at      =   models.DateTimeField(null=True, blank=True)
    # removed status, as end_at can handle

    MODES = [
        ('daily', 'daily'),
        ('standard', 'Standard'),
        # can be more if we have more features
    ]

    mode        =   models.CharField(max_length=128, choices=MODES, default='standard')

    class Meta:
        unique_together = ['user_id', 'start_at']  # Enforces composite unique key (candidate key)

    def __str__(self):
        return f"Session for {self.user.user_name} at {self.start_at}"
    

class UserAnswer(models.Model):
    user_id     =   models.ForeignKey(User, on_delete=models.CASCADE)
    start_at    =   models.ForeignKey(Session, on_delete=models.CASCADE)
    question_id =   models.ForeignKey(Question, on_delete=models.CASCADE)
    answer      =   models.PositiveIntegerField(
        default=0,
        # validators=[MinValueValidator(0), MaxValueValidator(3)]
    )

    class Meta:
        unique_together = ['user_id', 'start_at']

    def __str__(self):
        return f"Answer for User {self.user_id} in Session starting at {self.start_at} for Question {self.question_id}"