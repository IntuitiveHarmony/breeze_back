from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
# If the model is updated, make sure to update the serializer as well
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
