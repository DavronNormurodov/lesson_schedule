from rest_framework import serializers

from .models import Subject, Room, Groups, Pair


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'


class PairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'
