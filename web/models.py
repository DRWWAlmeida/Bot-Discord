from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateField()
    event_message = models.CharField(max_length=300)

    def __str__(self):
        return self.event_name
