from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from datetime import timezone, timedelta
from django.db.models import Q

from apps.booking.models import Booking


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['renter']

        def validate_date_from(self, value):
            if value < timezone.now().date():
                raise serializers.ValidationError(
                    'Date From must be today or later'
                )
            return value

        def validate_date_to(self, value):
            if value < timezone.now().date() + timedelta(days=1):
                raise serializers.ValidationError(
                    'Date To must be tomorrow or later'
                )
            return value

        def validate(self, data):
            date_from = data.get('date_from')
            date_to = data.get('date_to')
            apartment = data.get('apartment')

            if date_from >= date_to:
                raise serializers.ValidationError(
                    'Date From must be less than Date To'
                )

            check_dates(apartment, date_from, date_to)

            return data


class BookingDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['renter']

    def delete_booking(self, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['renter']


class ApproveBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = [
            'renter',
            'apartment',
            'date_from',
            'date_to',
            'is_canceled',
        ]


def check_dates(property, date_from, date_to, reservation_id=None):
    overlapping_reservations = (Booking.objects.filter(
        property=property,
        is_canceled=False,
        is_approved_by_landlord=True
    ).exclude(id=reservation_id).filter(
        Q(date_from__lte=date_to) & Q(date_to__gte=date_from)
    ))

    if overlapping_reservations.exists():
        raise serializers.ValidationError(
            'The apartment is already reserved for the selected dates. '
        )