#Django modules
from django.contrib import admin

#Project modules
from .models import Payment, Transaction


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Admin settings for Payment"""
    list_display = ('id', 'ride', 'amount', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'payment_method')
    search_fields = ('ride__id',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Admin settings for Transaction"""
    list_display = ('id', 'payment', 'transaction_type', 'amount', 'timestamp')
    list_filter = ('transaction_type',)
