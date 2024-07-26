from django.urls import path

from apps.booking.views import (
    BookingCreateAPIView,
    BookingListAPIView,
    BookingDeleteAPIView,
    BookingApproveView
)


urlpatterns = [
    path('', BookingListAPIView.as_view()),
    path('create/', BookingCreateAPIView.as_view()),
    path('<int:pk>/approve/', BookingApproveView.as_view()),
    path('<int:pk>/delete/', BookingDeleteAPIView.as_view()),
]