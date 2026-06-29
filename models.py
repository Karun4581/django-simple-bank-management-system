from django.db import models

# Create your models here.
class Account(models.Model):

    name = models.CharField(max_length=100)

    phone_number = models.IntegerField()

    address = models.CharField(max_length=100)

    account_number = models.IntegerField(unique=True)

    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name