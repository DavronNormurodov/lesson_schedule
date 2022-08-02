from rest_framework import serializers

from users.models.user import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'role',
            'email',

        ]
        read_only_fields = ['id']
