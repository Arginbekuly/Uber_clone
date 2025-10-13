from django.contrib import admin
from django.contrib.admin import register, ModelAdmin

from accounts.models import Account

# Register your models here.
@register(Account)
class AccountAdmin(ModelAdmin):
    list_display = ['email','username','first_name','last_name',
                    'role','is_active'
                    ]
    readonly_fields = ['last_login','date_joined','rating','created_at','updated_at','deleted_at']
    save_on_top = True
    fieldsets = (
        (
            "Personal Info",
        {
            "fields":(
                "first_name",
                "last_name",
                "username",
                "email",
                "phone_number",
            )
        }
        ),
        (
            "User Info related to App",
            {
                "fields":(
                    "role",
                    "rating",
                    "is_active",
                )
            }
        ),
         (
            "Date and Time Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                    "deleted_at",
                    "date_joined",
                    "last_login",
                )
            }
        )
    )