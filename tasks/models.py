from django.db import models

from django.utils import timezone


class Tasks(models.Model):
    title = models.CharField(max_length=100)
    complated = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} , {self.complated}'