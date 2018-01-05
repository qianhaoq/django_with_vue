from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
from .serializer import PokemonSerilizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
# Create your views here.

def hello(request):
    return HttpResponse("hello mongo")

class PokemonViewSet(MongoModelViewSet):
    """
    API endpoint that allows pokemon to be viewed
    """
    queryset = Pokemon.objects.order_by('id')
    serializer_class = PokemonSerilizer
    my_filter_fields = ('id', 'name_cn', 'name_en')

    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name_cn', 'name_en')
    ordering_fields = ('id', 'name_cn', 'name_en')
    # filter_backends = (MongoFilterBackend,)
    # filter_class = PokemonFilter

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    def get_kwargs_for_filtering(self):
        filtering_kwargs = {} 
        for field in  self.my_filter_fields: # iterate over the filter fields
            field_value = self.request.query_params.get(field) # get the value of a field from request query parameter
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get_queryset(self):
        queryset = Pokemon.objects.all() 
        filtering_kwargs = self.get_kwargs_for_filtering() # get the fields with values for filtering 
        if filtering_kwargs:
            queryset = Pokemon.objects.filter(**filtering_kwargs) # filter the queryset based on 'filtering_kwargs'
        return queryset
