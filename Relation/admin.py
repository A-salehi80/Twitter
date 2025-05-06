from django.contrib import admin

from Relation.models import Relation


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    pass

# Register your models here.
