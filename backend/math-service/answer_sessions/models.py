from django.db import models
from django.utils import timezone
import uuid

from users.models import User
from questions.models import Question

# Create your models here.
class Session(models.Model):
    session_id  =   models.UUIDField(
        primary_key =   True,
        default     =   uuid.uuid4,
        editable    =   False
    )  # Standard PK as sessionID (UUID for uniqueness/security)

    user        =   models.ForeignKey(User, on_delete=models.CASCADE)  # Renamed from user_id for convention
    start_at    =   models.DateTimeField(default=timezone.now)  # Auto-set on creation
    end_at      =   models.DateTimeField(null=True, blank=True)
    # removed status, as end_at can handle

    MODES = [
        ('daily', 'Daily'),
        ('standard', 'Standard'),
        # can be more if we have more features
    ]

    mode = models.CharField(max_length=128, choices=MODES, default='standard')

    class Meta:
        unique_together = ['user', 'start_at']  # Enforce composite unique (user + start_at can't duplicate)
        indexes = [models.Index(fields=['user', 'start_at'])]  # For fast lookups on the pair

    def __str__(self):
        return f"Session {self.session_id} for {self.user.user_name} at {self.start_at}"


class UserAnswer(models.Model):
    session     =   models.ForeignKey(Session, on_delete=models.CASCADE)  # Normal FK to Session (references session_id)
    question    =   models.ForeignKey(Question, on_delete=models.CASCADE)
    answer      =   models.PositiveIntegerField(
        null=True,
        blank=True,
        default=None,
        # validators=[MinValueValidator(0), MaxValueValidator(3)]
    )

    pk = models.CompositePrimaryKey('session', 'question')  # Composite PK: session + question

    class Meta:
        unique_together = ['session', 'question']  # Ensure no duplicate answers per session-question

    def __str__(self):
        return f"Answer for Session {self.session.session} for Question {self.question}"