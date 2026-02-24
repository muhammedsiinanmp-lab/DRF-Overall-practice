from rest_framework import serializers
from .models import Post
from books.serializers import UserSerializer
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author_details = UserSerializer(source="author",read_only=True)
    author = serializers.SlugRelatedField(
        queryset = User.objects.all(),
        slug_field = 'username'
    )
    class Meta:
        model = Post
        fields = '__all__'