from rest_framework import serializers
from .models import Blog

class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'content')