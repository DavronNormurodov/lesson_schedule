from django.urls import path, include

from references.views import RoomViewSet, SubjectViewSet, GroupsViewSet, PairViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('rooms', RoomViewSet, 'rooms')
router.register('subjects', SubjectViewSet, 'subjects')
router.register('groups', GroupsViewSet, 'groups')
router.register('pair', PairViewSet, 'Pair')

urlpatterns = [
    path('', include(router.urls)),
]

