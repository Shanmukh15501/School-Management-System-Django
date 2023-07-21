from django.contrib import admin
from .models import *
# Register your models here.

    
class ClassAdmin(   admin.ModelAdmin):
    def get_list_display(self, request):
        """
        Return a sequence containing the fields to be displayed on the
        changelist.
        """
        return self.list_display
    
    def get_fields(self, request, obj=None):

        if self.fields:
            return self.fields
        # _get_form_for_get_fields() is implemented in subclasses.
        form = self._get_form_for_get_fields(request, obj)
        return [*form.base_fields, *self.get_readonly_fields(request, obj)]

admin.site.register(Class,ClassAdmin)
