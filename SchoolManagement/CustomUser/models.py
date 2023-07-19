from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group, Permission 
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.utils import timezone
from django.db import models
import datetime
from Common.utils import getcode


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if email is None:
            raise TypeError('Users should have a email')
    
        user = self.model(**kwargs, email=email, )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,  password=None, **kwargs):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

USER_ROLE = (
   (1, 'Student'),
   (2, 'Teacher'),
   (3, 'Parent')
)

class Users(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255, db_index=True, unique=True)
    phone = models.CharField(max_length=15, db_index=True, blank=True)
    first_name = models.CharField( max_length=150, blank=True)
    last_name = models.CharField( max_length=150, blank=True)
    state = models.ForeignKey('Masters.State', related_name='users', on_delete=models.RESTRICT, null=True, blank=True)
    district = models.ForeignKey('Masters.District', related_name='users', on_delete=models.RESTRICT, null=True, blank=True)
    city = models.ForeignKey('Masters.City', related_name='users', on_delete=models.RESTRICT, null=True, blank=True)
    area = models.ForeignKey('Masters.Area', related_name='users', on_delete=models.RESTRICT, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    department =  models.ForeignKey('Masters.Department', related_name='users', on_delete=models.RESTRICT, null=True, blank=True)
    designation =  models.ForeignKey('Masters.Designation', related_name='users', on_delete=models.RESTRICT, null=True, blank=True)
    role = models.SmallIntegerField( choices= USER_ROLE, blank=True, null=True, default=1)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default= datetime.datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='userscreated', on_delete=models.RESTRICT, null=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='usersupdated', on_delete=models.RESTRICT,  null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email