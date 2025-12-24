from django.db import models
from django.utils.text import slugify
from django.utils import timezone
import uuid

# Create your models here.
class Topic(models.Model):
    topic_id    =   models.UUIDField(
        primary_key =   True,
        default     =   uuid.uuid4, 
        editable    =   False
    )

    title           =   models.CharField(max_length = 128, unique=True)
    description     =   models.CharField(max_length = 255)

    def __str__(self):
        return self.title


class Question(models.Model):
    question_id     =   models.UUIDField(
        primary_key =   True,
        default     =   uuid.uuid4,
        editable    =   False
    )
    
    topic       =   models.ForeignKey(Topic, on_delete=models.CASCADE)
    slug        =   models.SlugField(max_length=255, unique=True, editable=False)  # Unique, short slug for UI refs
    content     =   models.TextField()
    answer_key  =   models.PositiveIntegerField(
        default=0,
        # validators=[MinValueValidator(0), MaxValueValidator(3)]
    )

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    difficulty  =   models.CharField(max_length=128, choices=DIFFICULTY_CHOICES, default='medium')

    pub_date    =   models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [models.Index(fields=['topic', 'difficulty'])]

    def save(self, *args, **kwargs):
        if not self.slug:
            # Short base: Just topic title slugified
            base = self.topic.title.lower()
            slug_base = slugify(base)

            # Find the highest increment for this base and add 1
            existing = Question.objects.filter(slug__startswith=slug_base).order_by('-slug')
            increment = 1
            if existing.exists():
                last_slug = existing.first().slug
                try:
                    last_inc = int(last_slug.rsplit('-', 1)[-1]) + 1
                    increment = last_inc
                except ValueError:
                    pass  # If no number, start at 1
            self.slug = f"{slug_base}-{increment}" if increment > 1 else slug_base

            # Ensure global uniqueness (rare collision across topics)
            while Question.objects.filter(slug=self.slug).exists():
                increment += 1
                self.slug = f"{slug_base}-{increment}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Q{self.question_id} - {self.content[:50]}"


class Choice(models.Model):
    question        =   models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text     =   models.CharField(max_length = 200)
    order           =   models.PositiveIntegerField(default=0)  # For sequencing (A=1, B=2, etc.)

    pk = models.CompositePrimaryKey('question', 'choice_text', 'order')  # Composite PK: question + choice_text + order

    class Meta:
        ordering = ['order']  # Default sort by order ASC on querysets
        indexes = [models.Index(fields=['order'])]

    def __str__(self):
        return f"{self.choice_text} (Order: {self.order})"