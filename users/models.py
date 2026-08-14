from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class Role(models.Model):

    code = models.CharField(
        max_length=30,
        unique=True
    )

    name = models.CharField(
        max_length=100,
        unique=True
    )

    class Meta:
        db_table = "Role"
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    paternal_last_name = models.CharField(
        max_length=100
    )

    maternal_last_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=20
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "name",
        "paternal_last_name",
        "maternal_last_name"
    ]

    class Meta:
        db_table = "User"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email