from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
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

    @action(['GET'], False)
    def get_me(self, request, *args, **kwargs):
        # import jwt
        # from base import settings
        # print('request ==== ', request.auth)
        # user_id = jwt.decode(request.auth.token, settings.SECRET_KEY, algorithms=['HS256'])['user_id']
        # print('from jwt ======== ', user_id)
        # return Response(UserSerializers(User.objects.get(id=user_id)).data)
        return Response(UserSerializers(request.user).data)

