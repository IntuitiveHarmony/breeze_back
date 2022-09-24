from rest_framework import serializers
from .models import Sequence, User

class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence 
        fields = ('id', 'name', 'tempo',) 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'email', 'password', 'username', 'location') 
