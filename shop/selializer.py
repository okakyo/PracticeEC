from rest_framework import serializers
from .models import ShopItems

class ItemSelializer(serializers.ModelSerializer):
    class Meta:
        model=ShopItems
        fields=('itemName','itemValue','itemExplain','itemDate')