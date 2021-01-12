from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class AccountUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.save(using = self._db)
        return user

class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=25, primary_key=True)
    password = models.CharField(max_length=512)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = AccountUserManager()


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=512)

    def __str__(self):
        return self.role_name


class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=512)
    method = models.CharField(max_length=20, choices=(('GET', 'GET'), ('POST', 'POST')))
    url = models.CharField(max_length=512)

    def __str__(self):
        return self.permission_name


class RoleHasPermisson(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

