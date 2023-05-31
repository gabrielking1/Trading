from django.db import models

# Create your models here.
from django.db import models

class Trader(models.Model):
    name = models.CharField(max_length=100)
    capital = models.FloatField(default=100.0)

    def __str__(self):
        return self.name

class Entry(models.Model):
    trader = models.ForeignKey(Trader, related_name='entries', on_delete=models.CASCADE)
    profit_loss = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trader.name} - {self.profit_loss}"
    
  
