from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=20)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    
    class Meta:
        db_table = 'stocks_table'

    def __str__(self):
        return f"{self.ticker}-{self.date}"
