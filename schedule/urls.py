from django.urls import path, include
from schedule.views.lesson import LessonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('lessons', LessonViewSet, 'lessons')

urlpatterns = [
    path('', include(router.urls)),
]

