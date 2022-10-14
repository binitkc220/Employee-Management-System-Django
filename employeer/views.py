from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeerForm
from .models import employees
from django.contrib.auth.decorators import login_required

def employeer(request):
    if request.method == 'POST':
        data = request.POST
        emp_name = data['full_name']
        emp_add = data['address']
        emp_email = data['email']
        obj = employees.objects.create(full_name=emp_name,address=emp_add,email=emp_email)

        if obj:
            return redirect('/employeer')
        return HttpResponse("Sorry data not created..")
    else:
        emp_datas = employees.objects.all()
        context = {
            'emps' : emp_datas
        }
        return render(request,'employeer.html',context)


@login_required()
def employeer_update(request,id):
    emps = employees.objects.get(id=id)
    if request.method == 'POST':
        emps.full_name = request.POST['full_name']
        emps.address = request.POST['address']
        emps.email = request.POST['email']
        emps.save()
        return redirect('/employeer')
    context = {
        'emp' : emps
    }
    return render(request,'employeer_update.html',context)


@login_required()
def employeer_delete(request,id):
    emps = employees.objects.get(id=id)
    if request.method == 'POST':
        emps.delete()
        return redirect('/employeer')
    context = {
        'emp' : emps
    }
    return render(request,'employeer_delete.html',context)