from django.db import models
from django.conf import settings
from Common.utils import getcode
import datetime
from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class State(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    code = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='statecreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='stateupdated', on_delete=models.RESTRICT,  null=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)


    def save(self, *args, **kwargs):
        if self.id is None and (self.code == "" or self.code == None):
            self.code = getcode(State,'STA')
        super(State, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    code = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    state = models.ForeignKey(State, related_name='districts', on_delete=models.RESTRICT, null=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='districtcreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='districtupdated', on_delete=models.RESTRICT,  null=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)


    def save(self, *args, **kwargs):
        if self.id is None and (self.code == "" or self.code == None):
            self.code = getcode(District,'DIST')
        super(District, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    code = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    district = models.ForeignKey(District, related_name='cities', on_delete=models.RESTRICT, null=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='citycreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cityupdated', on_delete=models.RESTRICT,  null=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)



    def save(self, *args, **kwargs):
        if self.id is None and (self.code == "" or self.code == None):
            self.code = getcode(City,'CITY')
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"



class Area(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    code = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    city = models.ForeignKey(City, related_name='areas', on_delete=models.RESTRICT, null=True)
    district = models.ForeignKey(District, related_name='areas', on_delete=models.RESTRICT, null=True)
    state = models.ForeignKey(State, related_name='areas', on_delete=models.RESTRICT, null=True)
    pincode = models.CharField(max_length=10, null=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='areacreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='areaupdated', on_delete=models.RESTRICT,  null=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)


    def save(self, *args, **kwargs):
        if self.id is None and (self.code == "" or self.code == None):
            self.code = getcode(Area,'AREA')
        super(Area, self).save(*args, **kwargs)
 
    def __str__(self):
        return self.name


class Department(models.Model):
    code = models.CharField(max_length=30,null=True, blank=True)
    name = models.CharField(max_length=180,null=True, blank=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    
    def save(self, *args, **kwargs):
        if self.id is None:
            self.code = getcode(Department,'DEP')
        super(Department, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.name) + ' - ' + str(self.code)
    
class Designation(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    code = models.CharField(max_length=30,null=True, blank=True)
    name = models.CharField(max_length=180, null=True, blank=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)


    def save(self, *args, **kwargs):
        if self.id is None:
            self.code = getcode(Designation,'DSG')
        super(Designation, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.name) + ' - ' + str(self.code)
