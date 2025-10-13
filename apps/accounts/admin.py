from django.contrib import admin
from django.contrib.admin import register, ModelAdmin

from apps.accounts.models import Account

# Register your models here.
@register(Account)
class AccountAdmin(ModelAdmin):
    list_display = ['email','username','first_name','last_name',
                    'role','is_active'
                    ]
<<<<<<< HEAD:apps/accounts/admin.py
    readonly_fields = ['last_login','date_joined','rating', 'created_at', 'updated_at', 'deleted_at']
=======
    readonly_fields = ['last_login','date_joined','rating','created_at','updated_at','deleted_at']
>>>>>>> 065f406179b7d50e717b058711dac654a0ca92d0:accounts/admin.py
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