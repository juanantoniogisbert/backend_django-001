from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    stars = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Comment(TimestampedModel):
        body = models.TextField()

        hotels = models.ForeignKey(
            'hotels.Hotel', related_name='comments', on_delete=models.CASCADE
        )

        clients = models.ForeignKey(
            'clients.Client', related_name='comments', on_delete=models.CASCADE
        )
