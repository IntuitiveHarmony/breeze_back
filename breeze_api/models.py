from django.db import models

# Create your models here.
# If the model is updated, make sure to update the serializer as well
class Sequence(models.Model):
    name = models.CharField(max_length=32)
    tempo = models.IntegerField()

class Users(models.Model)
    email = models.EmailField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    username = models.CharField(max_length=32, unique=True)