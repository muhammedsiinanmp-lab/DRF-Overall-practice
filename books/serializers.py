from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','is_staff']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class BookSerializer(serializers.ModelSerializer):

    author_details = UserSerializer(source="author",read_only=True)

    author = serializers.SlugRelatedField(
        queryset = User.objects.all(),
        slug_field = 'username'
    )

    is_classic = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_is_classic(self,obj):
        if obj.published_year and obj.published_year < 2000:
            return True
        return False

    def validate(self, data):
        year = data.get('published_year')
        if year and year > 2026:
            raise serializers.ValidationError({"Error":"Invalid published_year"})
        return data
