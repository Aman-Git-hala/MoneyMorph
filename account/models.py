from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    # one user one portfolio, i mean why do you need more than one portfolio? i mean yeah but still tf
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #  DecimalField for floating point nums hehe
    stocks = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    liquid_cash = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    bank = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"