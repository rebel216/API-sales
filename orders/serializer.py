from dataclasses import field
from rest_framework import serializers
from orders.models import Data 

class Dataserializer(serializers.ModelSerializer):
    class Meta():
            
         model = Data
         fields = ('__all__')
