from django.contrib import admin
from User.models import Profile


@admin.register(Profile)
class Admin(admin.ModelAdmin):
    pass


