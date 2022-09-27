from rest_framework import serializers
from .models import Sequence

class SequenceSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Sequence # tell django which model to use
        fields = ('id', 'name', 'tempo', 'polyCsSteps', 'polyCsSynth', 'polyCsVolume', 'polyCsFilter', 'polyCsDist', 'polyCsReverb', 'polyCsDelay',) # tell django which fields to includeSequence
