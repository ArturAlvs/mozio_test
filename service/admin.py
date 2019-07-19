from django.contrib import admin

from .models import Provider, ServiceArea


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'poly')

admin.site.register(Provider)
admin.site.register(ServiceArea, ServiceAdmin)
