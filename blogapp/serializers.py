from django_rest_framework import serializers
from .models import BlogPost

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
