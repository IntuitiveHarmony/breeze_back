from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import SequenceSerializer
from .models import Sequence

class SequenceList(generics.ListCreateAPIView):
    queryset = Sequence.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = SequenceSerializer # tell django what serializer to use

class SequenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sequence.objects.all().order_by('id')
    serializer_class = SequenceSerializer
