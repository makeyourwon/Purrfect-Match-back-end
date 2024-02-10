from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import  Animal, Favorite, Profile
from .serializers import AnimalSerializer, FavoriteSerializer, ProfileSerializer, UserSerializer
from rest_framework.exceptions import PermissionDenied


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
    # queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)
    
    ## return to auth repo to implement this to work with favorite list when implemented.
    # def retrieve(self, request, *args, **kwargs):
    def perform_update(self, serializer):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        if profile.user != user:
            raise PermissionDenied('You do not have permission to update this profile')
        serializer.save()


class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to Purrfect Match!'}
        return Response(content)
    
class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'pk'

class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    lookup_field = 'pk'