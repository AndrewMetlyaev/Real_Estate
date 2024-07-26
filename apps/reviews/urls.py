from django.urls import path

from apps.reviews.views import ReviewCreateAPIView, ReviewListAPIView


urlpatterns = [
    path('', ReviewListAPIView.as_view()),
    path('create/', ReviewCreateAPIView.as_view())
]