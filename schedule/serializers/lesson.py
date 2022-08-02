from rest_framework import serializers

from references.serializers import SubjectSerializer, RoomSerializer, PairSerializer
from schedule.models.lesson import Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):

    subject = SubjectSerializer()
    room = RoomSerializer()
    pair = PairSerializer()

    class Meta:
        model = Lesson
        fields = [
            'id',
            'subject',
            'room',
            'teacher',
            'group',
            'pair',
            'day_of_week',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['teacher'] = instance.teacher.username
        representation['group'] = instance.group.title

        return representation
