from rest_framework.viewsets import ModelViewSet

from .models import Room, Subject, Groups, Pair
from .serializers import RoomSerializer, SubjectSerializer, GroupsSerializer, PairSerializer


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all().order_by('-id')
    serializer_class = RoomSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all().order_by('-id')
    serializer_class = SubjectSerializer


class GroupsViewSet(ModelViewSet):
    queryset = Groups.objects.prefetch_related('students').order_by('-id')
    serializer_class = GroupsSerializer


class PairViewSet(ModelViewSet):
    queryset = Pair.objects.all().order_by('-id')
    serializer_class = PairSerializer
