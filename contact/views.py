from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import MyContactSerializer
from .models import MyContact 

# Create your views here.
class MyContactViewSet(viewsets.ModelViewSet):
    queryset=MyContact.objects.all().order_by('-id')
    serializer_class=MyContactSerializer
    