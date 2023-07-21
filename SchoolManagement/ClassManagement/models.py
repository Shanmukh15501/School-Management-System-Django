from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createdby = models.ForeignKey(User, related_name='subjectscreated', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    std = models.IntegerField()
    section = models.CharField(max_length=100,blank=True)
    createdby = models.ForeignKey(User, related_name='classcreated', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return str(self.std)