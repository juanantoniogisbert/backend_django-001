from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    stars = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.comment
