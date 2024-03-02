from django.contrib import admin

from .models import *


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", 'username', 'text', 'date', )
    list_display_links = ("id", "username")
    
    search_fields = ("id", "username")


# Register your models here.
admin.site.register(Review, ReviewAdmin)
