from django.contrib import admin

from .models import Provider, ServiceArea


# So I could see poly info inside admin page
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'poly')

admin.site.register(Provider)
admin.site.register(ServiceArea, ServiceAdmin)
