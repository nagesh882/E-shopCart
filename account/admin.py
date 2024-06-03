from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(Account)
class AccountAdmin(UserAdmin):
    ordering = ["-account_id"]
    list_display = [
        "email", "username", "first_name", "last_name", "phone_number", "date_joined", "last_login","is_active", "is_staff"
    ]
    list_display_links = [
        "email", "username"    
    ]
    readonly_fields = ["date_joined", "last_login"]
    fieldsets = ()
    filter_horizontal = ()
    list_filter = ()

