from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
# If the model is updated, make sure to update the serializer as well
class Sequence(models.Model):
    name = models.CharField(max_length=32, default='')
    tempo = models.IntegerField(default=0)

    poly0Steps = ArrayField(models.CharField(max_length=10, default=''))
    poly0Synth = models.CharField(max_length=32, default='')
    poly0Volume = models.IntegerField(default=0)
    poly0Filter = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    poly0Dist = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    poly0Reverb = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    poly0Delay = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    
    poly1Steps = ArrayField(models.CharField(max_length=11, default=''))
    poly1Synth = models.CharField(max_length=32, default='')
    poly1Volume = models.IntegerField(default=1)
    poly1Filter = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    poly1Dist = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    poly1Reverb = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    poly1Delay = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    poly2Steps = ArrayField(models.CharField(max_length=11, default=''))
    poly2Synth = models.CharField(max_length=32, default='')
    poly2Volume = models.IntegerField(default=1)
    poly2Filter = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    poly2Dist = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    poly2Reverb = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    poly2Delay = models.DecimalField(max_digits=3, decimal_places=1, default=0)
