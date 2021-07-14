from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializers
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = ()


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializers


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializers
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )
