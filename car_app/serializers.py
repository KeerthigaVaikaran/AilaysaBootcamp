from rest_framework import serializers
from .models import *

# class ManufacturerSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(max_length=200)
#     country=serializers.CharField(max_length=200)
#     founded=serializers.IntegerField()
    
#     class Meta:
#         fields=['id','name','country','founded']
    
#     def create(self,validated_data):
#         return Manufacturer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name=validated_data.get("name",instance.name)
#         instance.country=validated_data.get("country",instance.country)
#         instance.founded=validated_data.get("founded",instance.founded)
#         instance.save()
#         return instance
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manufacturer
        fields=['id','name','country','founded']
