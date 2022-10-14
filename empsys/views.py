from django.shortcuts import render
from employee.models import Person
from employeer.models import employees
from django.contrib.auth.decorators import login_required

def indexpage(request):
    employee_no = Person.objects.all().count()
    employeer_no = employees.objects.all().count()
    context = {
        'employee_no' : employee_no,
        'employeer_no' : employeer_no 
    }
    return render(request,'index.html',context)
    
@login_required()
def dashboard(request):
    return render(request,'dashboard.html')