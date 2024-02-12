from rest_framework import serializers
from .models import  Animal, Favorite, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # profile_name = serializers.CharField(source='profile.name')
    # profile_age = serializers.IntegerField(source='profile.age',default=None)
    # profile_location = serializers.CharField(source='profile.location',default='')
    # profile_phone = serializers.IntegerField(source='profile.phone',default=None)
    # profile_name = serializers.CharField(source='profile.name', default='')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # profile_data = validated_data.pop('profile', {})
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user)
        return user
    
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

    
class FavoriteSerializer(serializers.ModelSerializer):
    animals = AnimalSerializer(many=True, read_only=True)
    class Meta:
        model = Favorite
        fields = ['id', 'animals',]

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    favorites = FavoriteSerializer()
    class Meta:
        model = Profile
        fields = '__all__'


