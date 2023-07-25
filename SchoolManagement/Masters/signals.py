from Masters.models import *
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

model_classes = [User]

def handler_logs(sender,  instance,  created, *args, **kwargs):
    if not instance.is_superuser:
         
        if sender in model_classes and created :
                print("---------------------")
                if instance.role ==2:
                    group, gr = Group.objects.get_or_create(name='Teacher',defaults={},)
                    instance.groups.add(group)
                    instance.save()
                    Teacher.objects.create(user=instance,dept =instance.department,name =instance.first_name+ ' ' +instance.last_name,
                                       sex =instance.gender,DOB =instance.DOB)
                elif instance.role == 1:
                    group, gr = Group.objects.get_or_create(name='Student',defaults={},)
                    instance.groups.add(group)
                    instance.save()
                    Student.objects.create(user=instance)
                else:
                    pass


for model_class in model_classes:
    post_save.connect(handler_logs, sender=model_class, dispatch_uid="post_log_"+model_class.__name__)

