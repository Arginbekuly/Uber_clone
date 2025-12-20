# Django modules
from django.contrib import admin

# Project modules
from .models import AutoPark

@admin.register(AutoPark)
class AutoParkAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
