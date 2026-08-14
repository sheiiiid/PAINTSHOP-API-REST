from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    paternal_last_name = models.CharField(max_length=100)
    maternal_last_name = models.CharField(max_length=100)
    rut = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.paternal_last_name} {self.maternal_last_name}"

    class Meta:
        db_table = "Customer"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
