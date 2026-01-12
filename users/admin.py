from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "nik", "phone_number", "country")
    list_filter = (
        "email",
        "nik",
    )
    search_fields = (
        "email",
        "nik",
    )
