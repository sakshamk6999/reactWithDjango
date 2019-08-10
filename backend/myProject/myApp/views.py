from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import Blog
from myApp.serializer import MySerializer
from rest_framework import generics
# Create your views here.

class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = MySerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = MySerializer

