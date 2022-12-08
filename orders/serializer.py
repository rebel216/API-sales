from dataclasses import field
from rest_framework import serializers
from orders.models import Data 


class Dataserializer(serializers.Serializer):
    # user_slug = serializers.CharField(max_length=200)
    # file = serializers.FileField()
    class Meta():
        model = Data
        fields = ('__all__')
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Data.objects.create(**validated_data)
