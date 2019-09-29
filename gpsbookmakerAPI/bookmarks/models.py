from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, CharField, DateTimeField
# from django.forms import CharField

# Create your models here.


class Bookmark(models.Model):
    user = ForeignKey(User, related_name='bookmark', on_delete=models.CASCADE)
    lat = CharField(max_length=32)
    lon = CharField(max_length=32)
    timestamp = DateTimeField(auto_now_add=True)