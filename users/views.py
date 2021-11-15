from django.shortcuts import render
from rest_framework import viewsets
from .serializers import theOfficeSerializer, GOTSerializer, random_userSerializer
from .models import theOffice, GOT, random_user

# Create your views here.
class theOfficeViewSet(viewsets.ModelViewSet):
    queryset = theOffice.objects.all().order_by('name')
    serializer_class = theOfficeSerializer

class GOTViewSet(viewsets.ModelViewSet):
    queryset = GOT.objects.all().order_by('name')
    serializer_class = GOTSerializer

class random_userViewSet(viewsets.ModelViewSet):
    queryset = random_user.objects.all().order_by('name')
    serializer_class = random_userSerializer