from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# If the model is updated, make sure to update the serializer as well

# sequence is for drum patterns
class Sequence(models.Model):
    name = models.CharField(max_length=32, default='')
    tempo = models.IntegerField(default=0)
    polyCsSteps = ArrayField(models.CharField(max_length=10, default=''))
    polyCsSynth = models.CharField(max_length=32, default='')
    polyCsVolume = models.IntegerField(default=0)
    polyCsFilter = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    polyCsDist = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    polyCsReverb = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    polyCsDelay = models.DecimalField(max_digits=3, decimal_places=1, default=0)

class User(models.Model):
    email = models.EmailField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    location = models.CharField(max_length=48)
