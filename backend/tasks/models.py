from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True) # Making user optional for now to simplify testing if auth isn't ready
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
