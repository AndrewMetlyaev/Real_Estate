import re
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from apps.users.models import User


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )
        extra_kwargs = {"password": {
            "write_only": True
        }}


class RegisterUserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "type_of_account",
            "password",
            "re_password",
        )
        extra_kwargs = {"password": {
            "write_only": True
        }}

    def validate(self, attrs):
        name = attrs.get('name')
        email = attrs.get('email')
        type_of_account = attrs.get('type_of_account')

        if not re.match('^[A-Za-z0-9_@.]+$', email):
            raise serializers.ValidationError(
                {'email': 'The email must be alphanumeric characters or have only _ . @ symbols.'}
            )

        if not re.match('^[A-Za-z ]+$', name):
            raise serializers.ValidationError(
                {'name': 'The name must be alphabet characters.'}
            )

        if not type_of_account:
            raise serializers.ValidationError(
                {'type_of_account': 'The type_of_account must be set.'}
            )

        password = attrs.get('password')
        re_password = attrs.get('re_password')

        if password != re_password:
            raise serializers.ValidationError(
                {'password': 'Password must be the same.'}
            )

        try:
            validate_password(password)
        except ValidationError as err:
            raise serializers.ValidationError(
                {'password': err.messages}
            )
        return attrs

    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data.pop('re_password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "email",
            "name",
            "type_of_account",
        ]
