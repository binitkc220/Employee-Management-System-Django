from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Person
from django.contrib.auth.decorators import login_required

def employee(request):

    if request.method == 'POST':
        data = request.POST
        fname = data['first_name']
        lname = data['last_name']
        email = data['email']

        obj = Person.objects.create(first_name=fname,last_name=lname,email=email)

        if obj:
            return redirect('/employee')
        return HttpResponse("Sorry data not created...")
    else:
        persons = Person.objects.all()
        context = {
            'persons' : persons
        }
        return render(request,'employee.html',context)


@login_required()
def employee_update(request,id):
    person = Person.objects.get(id=id)
    if request.method == 'POST':
        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.email = request.POST['email']
        person.save()
        return redirect('/employee')
    context = {
        'person' : person
    }
    return render(request,'employee_update.html',context)


@login_required()
def employee_delete(request,id):
    person = Person.objects.get(id=id)
    if request.method == 'POST':
        person.delete()
        return redirect('/employee')
    context = {
        'person' : person
    }
    return render(request,'employee_delete.html',context)