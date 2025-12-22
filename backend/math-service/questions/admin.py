from django.contrib import admin
from .models import Topic, Question, Choice  # Include others if needed

# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Columns in list view
    search_fields = ('title',)  # Search bar

# Optional: Register others
admin.site.register(Question)
admin.site.register(Choice)