from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    employee_id = models.PositiveIntegerField()
    designation = models.CharField(max_length=30)
    time = models.PositiveIntegerField()

    def __str__(self):
        return self.name
