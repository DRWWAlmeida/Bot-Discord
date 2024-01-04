from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.event_name
