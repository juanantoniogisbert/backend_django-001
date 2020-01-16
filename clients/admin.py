from django.contrib import admin

# Register your models here.
from clients.models import Client

admin.site.register(Client)