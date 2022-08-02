from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from users.models.user import User
from users.serializers.user import UserSerializers


class UserDataView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ['role', ]
    search_fields = ("username", )

