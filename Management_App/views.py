from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'home.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees':employees})


def filters(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        employees = Employee.objects.all()
        if name:
            employees = employees.filter(name__icontains=name)

            return render(request, 'employee_list.html', {'employees': employees})
        else:
            return render(request, 'filters.html')
    else:
        return render(request, 'filters.html')


def remove(request, employee_id=0):
    if employee_id:
        removed_employee = Employee.objects.get(id=employee_id)
        removed_employee.delete()
        return HttpResponse('successfully delete')
    else:
        employees = Employee.objects.all()
        return render(request, 'remove.html', {'employees': employees})


def checking(request, employee_id=0):
    employees = Employee.objects.all()
    if employee_id:
        employees = employees.filter(id=employee_id)
    else:
        employees = Employee.objects.all()

    context ={'employees':employees

              }
    return render(request,'checking.html',context)