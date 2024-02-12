from django.contrib import admin
from .models import Profile, Animal, Favorite
# Register your models here.
admin.site.register(Profile)
admin.site.register(Animal)
admin.site.register(Favorite)