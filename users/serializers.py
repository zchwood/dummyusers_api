from rest_framework import serializers
from .models import theOffice, GOT, random_user

class theOfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = theOffice
        fields = ('id','name','email','phone')

class GOTSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GOT
        fields = ('id','name','email','phone')

class random_userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = random_user
        fields = ('id','name','email','phone')