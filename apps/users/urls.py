from django.urls import path

from apps.users.views import LoginAPIView, RegisterUserAPIView, LogoutAPIView, GetAllUsersAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register/', RegisterUserAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('', GetAllUsersAPIView.as_view()),
]