from django.urls import path, re_path
from apps.property.views import (
    CreatePropertyAPIView,
    UpdatePropertyAPIView,
    DeletePropertyAPIView,
    PropertyFilterAPIView,
    GetAllPropertyAPIView,
    GetPropertyDetailAPIView
)


urlpatterns = [
    path('create/', CreatePropertyAPIView.as_view()),
    path('<int:pk>/edit/', UpdatePropertyAPIView.as_view()),
    path('<int:pk>/delete/', DeletePropertyAPIView.as_view()),
    path('<int:pk>/', GetPropertyDetailAPIView.as_view()),
    path('', GetAllPropertyAPIView.as_view()),
    re_path('filter/', PropertyFilterAPIView.as_view()),
]