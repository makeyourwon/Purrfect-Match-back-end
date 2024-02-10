from rest_framework import serializers
from .models import  Animal, Favorite, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile_name = serializers.CharField(source='profile.name')
    profile_age = serializers.CharField(source='profile.age')
    profile_location = serializers.CharField(source='profile.location')
    profile_phone = serializers.CharField(source='profile.phone')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile_name', 'profile_age', 'profile_location', 'profile_phone']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user, **profile_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'