from django.db import models

from core.models import TimestampedModel
from profiles.models import Profile


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    stars = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Comment(TimestampedModel):
    body = models.TextField()

    hotels = models.ForeignKey(
        Hotel, related_name='comments', on_delete=models.CASCADE
    )

    profile = models.ForeignKey(
        Profile, related_name='comments', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.body
