from django.contrib import admin
from .models import Employee


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee_id', 'designation', 'time']


admin.site.register(Employee, EmployeeAdmin)
