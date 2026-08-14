from django.db import models

# Create your models here.
class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vin = models.CharField(max_length=17)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.license_plate

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
        db_table = "Vehicle"