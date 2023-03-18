from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = ['id', 'title', 'description', 'created_at']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

class FollowingSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # following_user = UserSerializer()
    class Meta:
        model = Following
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

class commentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = comment
        fields = "__all__"
    
