from django.contrib import admin
from .models import Status, Favorite

# Register your models here.
class StatusAdmin(amin.ModelAdmin):
    list_display = ['user', 'text']


#Register models here
admin.site.register(Status, StatusAdmin)
admin.site.register(Favorite)
