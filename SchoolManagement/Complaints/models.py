from django.db import models

CHOICES = (
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
)
# Create your models here.
class ComplaintsData(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    complaintAgainst = models.CharField(max_length=8, choices=CHOICES)
    complaintDetails = models.TextField(blank=True, null=True)