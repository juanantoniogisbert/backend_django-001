from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Comment(TimestampedModel):
        body = models.TextField()

        hotels = models.ForeignKey(
            'hotels.Hotel', related_name='comments', on_delete=models.CASCADE
        )

        clients = models.ForeignKey(
            'clients.Client', related_name='comments', on_delete=models.CASCADE
        )