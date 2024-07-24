from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView

from apps.users.serializers import RegisterUserSerializer, LoginUserSerializer, CustomUserSerializer
from apps.middleware.set_cookies import set_jwt_cookies
from apps.users.models import User


class RegisterUserAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        set_jwt_cookies(response, user)
        return response


class LoginAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(
            request,
            username=email,
            password=password
        )
        if user:
            response = Response(status=status.HTTP_200_OK)
            set_jwt_cookies(response, user)
            return response
        else:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):

    def get(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('refresh_token')
        response.delete_cookie('access_token')
        return response


class GetAllUsersAPIView(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
