from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.booking.models import Booking
from apps.booking.serializers import (
    BookingSerializer,
    BookingCreateSerializer,
    BookingDeleteSerializer,
    ApproveBookingSerializer
)


class BookingListAPIView(ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def get_object(self):
        return get_object_or_404(Booking, pk=self.kwargs.get('pk'))


class BookingCreateAPIView(CreateAPIView):
    serializer_class = BookingCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(renter=self.request.user)


class BookingDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookingDeleteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Booking.objects.filter(user=self.request.user)
        else:
            return Booking.objects.none()


class BookingApproveView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ApproveBookingSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Booking.objects.none()

        return Booking.objects.filter(apartment__landlord=user, is_canceled=False)

    def get_object(self):
        obj = get_object_or_404(Booking, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
