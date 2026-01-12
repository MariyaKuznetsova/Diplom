from django.contrib import admin

from diary.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "contents", "owner")
    list_filter = ("date",)
    search_fields = ("date", "owner")
