from django.shortcuts import render


from rest_framework import generics
from .serializers import SequenceSerializer, UserSerializer
from .models import Sequence, User

class SequenceList(generics.ListCreateAPIView):
    queryset = Sequence.objects.all().order_by('id')
    serializer_class = SequenceSerializer 

class SequenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sequence.objects.all().order_by('id')
    serializer_class = SequenceSerializer
    
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
