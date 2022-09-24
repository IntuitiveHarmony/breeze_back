from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# If the model is updated, make sure to update the serializer as well

# sequence is for drum patterns
class Sequence(models.Model):
    name = models.CharField(max_length=32)
    tempo = models.IntegerField()

# login
class User(models.Model):
    email = models.EmailField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    location = models.CharField(max_length=48)
