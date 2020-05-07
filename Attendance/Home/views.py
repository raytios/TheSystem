from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import EmployeeForm, CheckForm, UserForm
from .models import Employee, Check



def create_employee(request):
    if not request.user.is_authenticated():
        return render(request, 'Home/login.html')
    else:
        form = EmployeeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.save()
            return render(request, 'Home/detail.html', {'employee': employee})
        context = {
            "form": form,
        }
        return render(request, 'Home/create_employee.html', context)



def create_check(request, employee_id):
    form = CheckForm(request.POST or None, request.FILES or None)
    employee = get_object_or_404(Employee, pk=employee_id)
    if form.is_valid():
        employees_checks = employee.check_set.all()
        for s in employees_checks:
            context = {'employee': employee,'form': form,}
            check.employee = employee       
            return render(request, 'Home/create_check.html', context)
        check.save()
        return render(request, 'Home/details.html', {'employee': employee})
    context = {'employee': employee,'form': form,}
    return render(request, 'Home/create_check.html', context)


def delete_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.delete()
    employees = Employee.objects.filter(user=request.user)
    return render(request, 'Home/index.html', {'employees': employees})


def delete_check(request, employee_id, check_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    check = Check.objects.get(pk=check_id)
    check.delete()
    return render(request, 'Home/details.html', {'employee': employee})


def details(request, employee_id):
    if not request.user.is_authenticated():
        return render(request, 'Home/login.html')
    else:
        user = request.user
        employee = get_object_or_404(Employee, pk=employee_id)
        return render(request, 'Home/details.html', {'employee': employee, 'user': user})

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'Home/login.html')
    else:
        all_employee = Employee.objects.all()
    context = {'all_employee' : all_employee}
    return render(request, 'Home/index.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'Home/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                employees = Employee.objects.filter(user=request.user)
                return render(request, 'Home/index.html', {'employees': employees})
            else:
                return render(request, 'Home/login.html', {'error_message': 'Your account has been locked'})
        else:
            return render(request, 'Home/login.html', {'error_message': 'Your username, email or password is wrong'})
    return render(request, 'Home/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                employees = Employee.objects.filter(user=request.user)
                return render(request, 'Home/index.html', {'employees': employees})
    context = {
        "form": form,
    }
    return render(request, 'Home/register.html', context)


def checks(request):
    if not request.user.is_authenticated():
        return render(request, 'Home/login.html')
    else:
        try:
            check_ids = []
            for employee in Employee.objects.filter(user=request.user):
                for check in employee.check_set.all():
                    check_ids.append(check.pk)
            users_checks = Check.objects.filter(pk__in=check_ids)
        except Employee.DoesNotExist:
            users_checks = []
        return render(request, 'Home/checks.html', {
            'check_list': users_checks,
        })