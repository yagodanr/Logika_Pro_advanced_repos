from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'description', 'price')
    list_display_links = ("id", "name")

    search_fields = ('id', 'name')
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", 'product', 'author', 'text', 'rating', "created_at")

    search_fields = ('id', 'name', "created_at")
    
    
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)