from django.db import models

# Create your models here.
# If the model is updated, make sure to update the serializer as well
class Sequence(models.Model):
    name = models.CharField(max_length=32)
    tempo = models.IntegerField()
