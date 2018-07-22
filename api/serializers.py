from rest_framework import serializers
from api.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'opening_time', 'closing_time',]