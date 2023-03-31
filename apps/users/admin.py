from django.contrib import admin
from .models import User
from django.contrib import admin

admin.site.site_header = "Lexus Dealer"
admin.site.site_title = "Lexus Dealer Title"


@admin.register(User)
class Users(admin.ModelAdmin):
    list_display = ("id", "info",)
    list_filter = ("id",)
    search_fields = ("id",)

