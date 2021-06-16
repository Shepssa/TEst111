from django.contrib import admin
from inbox.models import Customer


@admin.register(Customer)
class CusttomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_created")
    readonly_fields = ("date_created",)
