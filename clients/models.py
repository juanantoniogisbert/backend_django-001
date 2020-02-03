from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    # author = models.ForeignKey(
    #     'profiles.Profile', on_delete=models.CASCADE, related_name='articles'
    # )

    def __str__(self):
        return self.name
