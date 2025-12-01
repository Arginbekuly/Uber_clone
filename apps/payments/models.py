#Django modules
from django.db import models

#Project modules
from apps.rides.models import Ride

class Payment(models.Model):
    """
    Payment fro a ride.

    ride: the ride this payyment belongs to
    amount: how much money
    payment_method: card, cash or wallet
    status: pending,completed,failed
    created_at: when payment was created
    update_at : when payment last updated
    """

    PAYMENT_METHODS = [
        ('card' , 'Card'),
        ('cash', 'Cash'),
        ('wallet', 'Wallet'),
    ]

    ride = models.OneToOneField(Ride,on_delete= models.CASCADE, related_name = 'payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices= PAYMENT_METHODS)
    status = models.CharField(max_length=20, choices = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ],
    default = 'pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment { self.id } for Ride { self.ride.id }: { self.amount } ({ self.status })"
    
class Transaction(models.Model):
    """
    One transaction linked to a payment.

    payment: which payment this transaction belongs to
    transaction_type : type of trans
    amount : money amount
    timestamp: when it happened
    """
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length = 50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction { self.id } for Payment { self.payment.id }: { self.transaction_type } - { self.amount }"