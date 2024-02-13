from django.urls import path
from .views import Home, AnimalList, AnimalDetail, FavoriteList, FavoriteDetail, CreateUserView, LoginView, VerifyUserView, ProfileDetail, AddToFavoriteView, RemoveFromFavoriteView


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', VerifyUserView.as_view(), name='refresh'),
    path('profile/', ProfileDetail.as_view(), name='profile_detail'),
    path('animals/', AnimalList.as_view(), name='animal_list'),
    path('animals/<int:pk>/', AnimalDetail.as_view(), name='animal_detail'),
    path('favorites/', FavoriteList.as_view(), name='favorite_list'),
    path('favorites/<int:pk>/', FavoriteDetail.as_view(), name='favorites_detail'), #no longer use this url since we update
    #/favorites/ to show the specific profile's favorite list
    path('favorites/add/<int:pk>/', AddToFavoriteView.as_view(), name='add_to_favorites'),
    path('favorites/remove/<int:pk>/', RemoveFromFavoriteView.as_view(), name='remove_from_favorites'),
]