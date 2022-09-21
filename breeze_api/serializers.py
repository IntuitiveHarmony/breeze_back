from rest_framework import serializers
from .models import Sequence

class SequenceSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Sequence # tell django which model to use
        fields = ('id', 'name', 'tempo',) # tell django which fields to includeSequence
