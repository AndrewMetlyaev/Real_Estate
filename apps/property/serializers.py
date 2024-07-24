from rest_framework import serializers, status
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from apps.property.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        location = validated_data.pop('location', None)
        try:
            apartment = Property.objects.create(address=location, **validated_data)
        except IntegrityError:
            raise serializers.ValidationError("This combination of title and address already exists.")

        return apartment

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        if address_data:
            address = get_or_create_address(address_data)
            instance.address = address
        for key, value in validated_data.items():
            setattr(instance, key, value)
        try:
            instance.save()
        except IntegrityError:
            raise serializers.ValidationError("This combination of title and address already exists.")

        return instance

    def delete_property(self, pk):
        property = get_object_or_404(Property, pk=pk)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
