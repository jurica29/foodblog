from django.contrib import admin
# Import post model from models.py
from .models import Post

# Registering models here
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)

admin.site.register(Post, PostAdmin)