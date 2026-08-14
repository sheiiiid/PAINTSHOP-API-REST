from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        from .models import Role
        
        if not email:
            raise ValueError("El email es obligatorio")

        email = self.normalize_email(email)

        if not extra_fields.get("role"):
            extra_fields["rol"] = Role.objects.get(code="COLAB")

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):

        from .models import Rol

        try:
            rol_admin = Rol.objects.get(code="ADMIN")
        except Rol.DoesNotExist:
            raise ValueError(
                "El rol ADMIN no existe. "
                "Ejecute primero: python manage.py loaddata roles"
            )

        extra_fields.setdefault("rol", rol_admin)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(
            email,
            password,
            **extra_fields
        )