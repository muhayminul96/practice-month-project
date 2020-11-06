from django import forms
from .models import Employee
class EmployeeFrom(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

