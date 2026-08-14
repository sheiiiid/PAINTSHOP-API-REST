from django.db import models

# Create your models here.
class WorkOrderStatus(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Work_Order_Status'
        verbose_name_plural = 'Work_Order_Status'
        db_table = 'WorkOrderStatus'
