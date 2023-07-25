from django.contrib import admin
from .models import ComplaintsData

# Register your models here.
admin.site.register(ComplaintsData)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'complaintAgainst', 'complaintDetails')