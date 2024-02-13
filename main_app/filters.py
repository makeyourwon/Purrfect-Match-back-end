import django_filters
from .models import Animal

class AnimalFilter(django_filters.FilterSet):
    primary_breed = django_filters.CharFilter(method='filter_primary_breed')

    class Meta:
        model = Animal
        fields = {
            'name':['icontains'],
            'type':['icontains'],
            'age':['icontains'],
            'size':['icontains'],
            'gender':['icontains'],
            'status':['icontains'],
            'location':['icontains'],
            
        }

    
    def filter_primary_breed(self, queryset, name, value):
        """
        This method filters the queryset by the primary breed within the JSON field.
        """
        return queryset.filter(breed__primary__icontains=value)
    
