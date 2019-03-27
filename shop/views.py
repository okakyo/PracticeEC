from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ShopItems
from .selializer import ItemSelializer

class ItemApiView(generics.ListAPIView):
    queryset=ShopItems.objects.all()
    serializer_class=ItemSelializer