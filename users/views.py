from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import theOfficeSerializer, GOTSerializer, random_userSerializer
from .models import theOffice, GOT, random_user
from rest_framework.response import Response


# Create your views here.
class theOfficeViewSet(viewsets.ModelViewSet):
    queryset = theOffice.objects.all().order_by('name')
    serializer_class = theOfficeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GOTViewSet(viewsets.ModelViewSet):
    queryset = GOT.objects.all().order_by('name')
    serializer_class = GOTSerializer

class random_userViewSet(viewsets.ModelViewSet):
    queryset = random_user.objects.all().order_by('name')
    serializer_class = random_userSerializer