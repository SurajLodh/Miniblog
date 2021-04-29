from django.contrib import admin
from .models import Blogs
# Register your models here.

@admin.register(Blogs)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dis']
