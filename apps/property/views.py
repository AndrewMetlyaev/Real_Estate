from rest_framework.generics import RetrieveDestroyAPIView, ListAPIView, UpdateAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from django.contrib.auth import authenticate
from rest_framework.views import APIView

from apps.property.models import Property
from apps.property.serializers import (
    PropertySerializer,
    PropertyCreateSerializer,
    PropertyDeleteSerializer,
    PropertyUpdateSerializer,
    PropertyFilterSerializer
)


class GetAllPropertyAPIView(ListAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()


class GetPropertyDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        property = get_object_or_404(Property, pk=pk)
        serializer = PropertySerializer(property)
        return Response(serializer.data)


class CreatePropertyAPIView(ListCreateAPIView):
    serializer_class = PropertyCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class UpdatePropertyAPIView(UpdateAPIView):
    serializer_class = PropertyUpdateSerializer
    permission_classes = [AllowAny]

    def put(self, request, *args, **kwargs):
        property = get_object_or_404(Property, pk=kwargs['pk'])
        serializer = PropertyUpdateSerializer(instance=property, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )


class DeletePropertyAPIView(RetrieveDestroyAPIView):
    serializer_class = PropertyDeleteSerializer
    permission_classes = [AllowAny]

    def delete(self, request: Request, *args, **kwargs) -> Response:
        property = Property.objects.get(pk=self.kwargs['pk'])
        property.delete()

        return Response(
            data={
                'message': 'Property deleted successfully'
            },
            status=status.HTTP_200_OK
        )


class PropertyFilterAPIView(ListAPIView):
    serializer_class = PropertyFilterSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Property.objects.all()
