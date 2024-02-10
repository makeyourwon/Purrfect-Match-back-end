from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import  Animal, Favorite
from .serializers import AnimalSerializer, FavoriteSerializer

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