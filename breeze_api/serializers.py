from rest_framework import serializers
from .models import Sequence, User

class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence # tell django which model to use
        fields = ('id', 'name', 'tempo', 'polyCsSteps', 'polyCsSynth', 'polyCsVolume', 'polyCsFilter', 'polyCsDist', 'polyCsReverb', 'polyCsDelay',) # tell django which fields to includeSequence

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'email', 'password', 'username', 'location')
