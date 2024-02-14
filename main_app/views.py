from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions, filters
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import  Animal, Favorite, Profile
from .serializers import AnimalSerializer, FavoriteSerializer, ProfileSerializer, UserSerializer
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AnimalFilter

# add to favorites
class AddToFavoriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,pk):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        animal = get_object_or_404(Animal, pk=pk)
        if not profile.favorites:
            # profile.favorites = Favorite.objects.create(profile=profile)
            favorite = Favorite.objects.create()
            profile.favorites = favorite
            print(profile.favorites)
            profile.save()
        profile.favorites.animals.add(animal)
        # return Response(status=status.HTTP_204_NO_CONTENT)
        favorite_animals = profile.favorites.animals.all()
        serializer = AnimalSerializer(favorite_animals, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# remove from favorite
class RemoveFromFavoriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        animal = get_object_or_404(Animal, pk=pk)
        if profile.favorites:
            profile.favorites.animals.remove(animal)
            return Response({'message': f'Animal {animal.name} removed from favorites'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No favorites list found'}, status=status.HTTP_404_NOT_FOUND)

# user registration
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user = User.objects.get(username=response.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
            }, status=status.HTTP_201_CREATED)
        return response
    
class LoginView(APIView):
    permissions_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        else:
            return Response({
                'error': 'Username or password is incorrect'
            }, status=status.HTTP_400_BAD_REQUEST)
        
# User Verification
class VerifyUserView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = User.objects.get(username=request.user)
        refresh = RefreshToken.for_user(request.user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })
    
# User Profile
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permissions_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        # Fetch the profile for the authenticated user
        user = self.request.user
        return Profile.objects.filter(user=user)

    def get_object(self):
        queryset = self.get_queryset()
        # Get the profile object for the logged-in user
        profile = get_object_or_404(queryset)
        return profile

    def perform_update(self, serializer):
        profile = self.get_object()
        if profile.user != self.request.user:
            raise PermissionDenied('You do not have permission to update this profile')
        serializer.save()
# Home Page
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to Purrfect Match!'}
        return Response(content)

    
class AnimalList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,]
    filterset_class = AnimalFilter
    search_fields = ['name', 'id',]

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'pk'

class FavoriteList(generics.ListCreateAPIView):
    # queryset = Favorite.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        if profile.user != user:
            raise PermissionDenied('You do not have permission to view this favorite list')
        else:
            profile = get_object_or_404(Profile, user=user)
            return Favorite.objects.filter(profile=profile)

#no longer use this view. Instead, favoriteList does the job.
class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    lookup_field = 'pk'