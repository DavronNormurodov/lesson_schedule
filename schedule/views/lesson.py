
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from references.models import Groups, Pair
from schedule.models.lesson import Lesson
from schedule.serializers.lesson import LessonSerializer, LessonListSerializer
from schedule.utils import get_schedule_for_day, get_schedule_for_week


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.select_related('subject', 'room', 'group', 'teacher', 'pair')
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['subject', 'room', 'teacher', 'day_of_week', ]

    def list(self, request, *args, **kwargs):

        day = request.query_params.get('day_of_week', None)

        if request.user.role.unique_name == 'student':
            student = request.user
            lessons = self.get_queryset().filter(group_id__in=student.student_groups.values_list('id'))
            serializer = LessonListSerializer(lessons, many=True)

        elif request.user.role.unique_name == 'teacher':
            teacher = request.user
            lessons = teacher.teacher_lessons.all()
            serializer = LessonListSerializer(lessons, many=True)
        else:
            groups = Groups.objects.all().order_by('-id')
            response = [{"group": title, "lesson_schedule": []} for title in groups.values_list('title')]
            j = 0
            for group in groups:
                response[j] = {"group": group.title, "lesson_schedule": []}
                lessons = self.get_queryset().filter(group=group)
                serializer = LessonListSerializer(lessons, many=True)

                lesson_schedule = get_schedule_for_week(serializer)
                response[j]['lesson_schedule'] = lesson_schedule
                j += 1
            return Response(response)

        if not day:
            lesson_schedule = get_schedule_for_week(serializer)
            return Response(lesson_schedule)

        else:
            lesson_schedule = get_schedule_for_day(serializer, day)
            return Response(lesson_schedule)

    def create(self, request, *args, **kwargs):
        data = request.data
        pair = Pair.objects.get(id=data.get('pair'))
        room_id = data.get('room')
        day_of_week = data.get('day_of_week')
        group_id = data.get('group')
        teacher_id = data.get('teacher')

        if self.get_queryset().filter(
                room_id=room_id, pair__index=pair.index, day_of_week=day_of_week).exists():
            return Response({"msg": "This room is busy for gavin time"})

        elif self.get_queryset().filter(
                teacher_id=teacher_id,
                pair__index=pair.index,
                day_of_week=day_of_week).exists():
            return Response({"msg": "Teacher already has a lesson for gavin time"})
        elif self.get_queryset().filter(
                group_id=group_id, pair__index=pair.index, day_of_week=day_of_week).exists():
            return Response({"msg": "The group has a lesson at this time"})
        else:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(['POST', ], detail=False)
    def get_lesson_schedule_for_group(self, request, *args, **kwargs):
        """
        Should have a get but post chosen for the sake of easily getting parameters
        """
        group_id = request.data.get('group')
        day = request.data.get('day')
        lessons = self.get_queryset().filter(group_id=group_id)
        serializer = LessonListSerializer(lessons, many=True)

        if not day:
            lesson_schedule = get_schedule_for_week(serializer)
            return Response(lesson_schedule)

        else:
            lesson_schedule = get_schedule_for_day(serializer, day)
            return Response(lesson_schedule)

    def get_queryset(self):
        return self.queryset
