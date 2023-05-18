from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        NORMAL_USER = "0", 'Normal'
        ADMIN = "1", 'Admin'

    base_role = Role.NORMAL_USER
    role = models.CharField(max_length=50, choices=Role.choices, default=0)

    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = UserManager()
