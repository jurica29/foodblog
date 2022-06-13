from django.contrib import admin
# Import post model from models.py
from .models import Post

# Registering models here
admin.site.register(Post)