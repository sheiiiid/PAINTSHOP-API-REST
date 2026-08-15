from django.db import models

class Inspection(models.Model):
    work_order = models.ForeignKey('work_orders.WorkOrder', on_delete=models.PROTECT, related_name='inspections')
    user = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='inspections')
    kilometers = models.IntegerField()
    fuel_level = models.DecimalField()
    color = models.CharField(max_length=100)
    paint_condition = models.CharField(max_length=100)
    observations = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Inspection'
        verbose_name_plural = 'Inspections'
        db_table = 'Inspection'

    def __str__(self):
        return f'Inspection {self.id}'