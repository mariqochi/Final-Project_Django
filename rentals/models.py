from django.db import models



class Car(models.Model):
    model_name = models.CharField(max_length=100)
    manufacturing_year = models.PositiveIntegerField()
    petrol_consumption = models.FloatField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_three_days = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.model_name

class RentalAvailability(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.car} - {self.date} - Available: {self.is_available}"

