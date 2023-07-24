from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin, GroupAdmin as AuthGroupAdmin

from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportMixin, ExportMixin, ImportExportMixin
from import_export import resources, fields
from import_export.mixins import base_formats
from import_export.fields import Field

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import *





class ExportMixinAdmin(ExportMixin):

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
          )

        return [f for f in formats if f().can_export()]

    class Meta:
        abstract = True

class ImportMixinAdmin(ImportMixin):

    def get_import_formats(self):
        formats = (
            base_formats.CSV,
          )

        return [f for f in formats if f().can_export()]

    class Meta:
        abstract = True





class UserAdmin(   admin.ModelAdmin):
    def get_list_display(self, request):
        model = self.model
        return [field.name for field in model._meta.fields]
    
    def get_fields(self, request, obj=None):

        if self.fields:
            return self.fields
        # _get_form_for_get_fields() is implemented in subclasses.
        form = self._get_form_for_get_fields(request, obj)
        return [*form.base_fields, *self.get_readonly_fields(request, obj),'groups']


admin.site.register(Users,UserAdmin)