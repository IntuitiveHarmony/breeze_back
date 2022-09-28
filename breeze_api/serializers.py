from rest_framework import serializers
from .models import Sequence

class SequenceSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Sequence # tell django which model to use
        fields = (
            'id',
            'name',
            'tempo',
            
            'poly0Steps',
            'poly0Synth',
            'poly0Volume',
            'poly0Filter',
            'poly0Dist',
            'poly0Reverb',
            'poly0Delay',

            'poly1Steps',
            'poly1Synth',
            'poly1Volume',
            'poly1Filter',
            'poly1Dist',
            'poly1Reverb',
            'poly1Delay',

            'poly2Steps',
            'poly2Synth',
            'poly2Volume',
            'poly2Filter',
            'poly2Dist',
            'poly2Reverb',
            'poly2Delay',) # tell django which fields to includeSequence
