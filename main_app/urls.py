from django.urls import path
from .views import Home, AnimalList, AnimalDetail, FavoriteList, FavoriteDetail, CreateUserView, LoginView, VerifyUserView, ProfileDetail


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', VerifyUserView.as_view(), name='refresh'),
    path('profile/<int:id>/', ProfileDetail.as_view(), name='profile_detail'),
    path('animals/', AnimalList.as_view(), name='animal_list'),
    path('animals/<int:pk>/', AnimalDetail.as_view(), name='animal_detail'),
    path('favorites/', FavoriteList.as_view(), name='favorite_list'),
    path('favorites/<int:pk>/', FavoriteDetail.as_view(), name='favorite_detail'),

]