from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeFrom


def home(request):
    return render(request, "myapp/home.html")


def load_form(request):
    form = EmployeeFrom
    return render(request, "myapp/index.html", {'form': form})


def add(request):
    form = EmployeeFrom(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    employee = Employee.objects.all
    return render(request,'myapp/show.html', {'employee':employee})
def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, "myapp/edit.html",{'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeFrom(request.POST, instance=employee)
    form.save()
    return redirect('/show')


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')
def sharch(request):
    id = request.POST['id']
    employee = Employee.objects.filter(eid__icontains= id)
    for i in employee:
        print(i.ename)
    return render(request, "myapp/show.html", {'employee':employee})



