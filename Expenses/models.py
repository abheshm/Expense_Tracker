from django.db import models

# Create your models here.
class Transaction(models.Model):
    TYPE_CHOICES = (
        ('income','Income'),
        ('expense','Expense'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type= models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.CharField(max_length=100)
    date= models.DateField()


    def __str__(self):
        return f"{self.type} - {self.amount}"
