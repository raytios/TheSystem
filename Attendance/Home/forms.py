from django import forms
from django.contrib.auth.models import User

from .models import Employee, Check


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['employee_no', 'first_name', 'last_name', 'address']


class CheckForm(forms.ModelForm):

    class Meta:
        model = Check
        fields = ['time_in', 'time_out']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']