from django.contrib import admin

# Register your models here.
from categories.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   

    list_display = ('id', 'name')
