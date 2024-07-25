from rest_framework import serializers, status
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from apps.property.models import Property


class PropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['owner']


class PropertyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['owner']

    def update(self, pk, validated_data):
        property = get_object_or_404(Property, pk=pk)
        property = Property.objects.update(**validated_data)
        return property


class PropertyDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['owner']

    def delete_property(self, pk):
        property = get_object_or_404(Property, pk=pk)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['owner']

    def available(self):
        return Property.objects.filter(available=True)


class PropertyFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['owner']

    def filter(self, attrs):
        price =attrs.get('price')
        city = attrs.get('city')
        room = attrs.get('room')
        property_type = attrs.get('property_type')
        if price:
            return Property.objects.filter(price=price)
        if city:
            return Property.objects.filter(city=city)
        if room:
            return Property.objects.filter(room=room)
        if property_type:
            return Property.objects.filter(property_type=property_type)
