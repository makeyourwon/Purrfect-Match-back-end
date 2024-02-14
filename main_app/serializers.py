from rest_framework import serializers
from .models import  Animal, Favorite, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
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
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = Animal
        fields = ['id','name', 'type', 'breed', 'age', 'size', 'gender', 'color', 'status', 'location', 'description', 'photo_url', 'contact']

    def get_photo_url(self,obj):
        # if obj.photos and len(obj.photos) > 0:
        #     return obj.photos[0]
        # else:
        #     return 'https://images.pexels.com/photos/6601811/pexels-photo-6601811.jpeg?auto=compress&cs=tinysrgb&w=800'
        if obj.photos and len(obj.photos) > 0:
            return {"photo": obj.photos}
        else:
            return {"photo": [{"medium": "https://images.pexels.com/photos/6601811/pexels-photo-6601811.jpeg?auto=compress&cs=tinysrgb&w=300"}]}

    
class FavoriteSerializer(serializers.ModelSerializer):
    animals = AnimalSerializer(many=True, read_only=True)
    class Meta:
        model = Favorite
        fields = ['id', 'animals',]

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    favorites = FavoriteSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'


