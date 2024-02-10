from django.contrib import admin

from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'published_date')
    list_display_links = ("id", "title")

    search_fields = ('id', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(Author)