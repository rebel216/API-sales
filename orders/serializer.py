from dataclasses import field
from rest_framework import serializers
from orders.models import Data 

class Dataserializer(serializers.ModelSerializer):
    user_slug = serializers.CharField(max_length=200)
    filename = serializers.CharField(max_length=200)
    
    class Meta:
        model = Data
        fields = ('__all__')
