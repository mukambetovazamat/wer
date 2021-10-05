from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CarSerializer
from .models import Car
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter


class CarsPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class ListCar(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    pagination_class = CarsPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'color',]


class CarUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    # pagination_class = CarsPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwnerOrReadOnly,)
    lookup_field = 'id'

# class CarDetail(RetrieveAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()
