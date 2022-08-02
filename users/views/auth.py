from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models.user import User
from users.serializers.auth import MyTokenObtainPairSerializer, UserRegisterSerializers
from rest_framework.generics import CreateAPIView


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializers


class UserLoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
