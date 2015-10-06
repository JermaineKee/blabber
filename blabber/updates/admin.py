from django.contrib import admin
from .models import Status, Favorite

# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'posted_at', 'favorite_count']

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']


#Register models here
admin.site.register(Status, StatusAdmin)
admin.site.register(Favorite, FavoriteAdmin)
