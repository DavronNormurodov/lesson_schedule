from django.urls import path, include

from users.views.auth import UserRegisterView, UserLoginView
from users.views.user import UserDataView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserDataView, 'user_set')

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('', include(router.urls)),
]

