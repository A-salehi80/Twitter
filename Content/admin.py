from django.contrib import admin
from .models import Post,Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Like)
class LikesAdmin(admin.ModelAdmin):
    pass

