from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models import CharField, DateTimeField, BooleanField, ForeignKey, PROTECT
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.managers.user import UserManager
from users.models.role import Role


class User(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    first_name = CharField('first name', max_length=150, blank=True)
    last_name = CharField('last name', max_length=150, blank=True)
    email = CharField("email field", max_length=150, null=True, blank=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    is_active = BooleanField(default=True)

    role = ForeignKey(Role, PROTECT, 'role_users')
    date_joined = DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ("-date_joined",)

    def __str__(self):
        return self.username
