from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from users.models.user import User
from users.serializers.user import UserSerializers


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def to_internal_value(self, data):
        password = data.get('password')
        username = data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"error": "Does not exist"})
        else:
            if user.check_password(password):
                return super(MyTokenObtainPairSerializer, self).to_internal_value(data)
            raise serializers.ValidationError({
                "error": "Incorrect password"
            })

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user_data'] = UserSerializers(self.user, context=self.context).data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class UserRegisterSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'role',
            # 'profile',
        ]

    def validate(self, attrs):
        # data = super().validate(attrs)
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            try:
                User.objects.get(username=username)
                raise serializers.ValidationError('User already exist with provided credentials')
            except User.DoesNotExist:
                pass
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
