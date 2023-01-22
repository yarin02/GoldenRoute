from django.shortcuts import render
from rest_framework import generics
from .serializers import WeightSerializer
from .models import Weight

# Create your views here.

class WeightView(generics.CreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer