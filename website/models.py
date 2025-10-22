from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    date = models.DateField(db_index=True)
    time = models.TimeField(null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'time', 'created_at']
        indexes = [
            models.Index(fields=['user', 'date']),
            models.Index(fields=['user', 'completed']),
        ]

    def __str__(self):
        if self.time:
            return f"{self.date} {self.time.strftime('%I:%M %p')} - {self.title}"
        return f"{self.date} - {self.title}"
