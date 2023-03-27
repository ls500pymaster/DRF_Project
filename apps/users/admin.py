from django.contrib import admin
from .models import User


@admin.register(User)
class Users(admin.ModelAdmin):
    list_display = ("id", "info",)
    list_filter = ("id",)
    search_fields = ("id",)

