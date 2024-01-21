from django import forms
from .models import Employee,Department,Employee_Salary

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class Employee_SalaryForm(forms.ModelForm):
    class Meta:
        model = Employee_Salary
        fields = '__all__'
    
class ReportForm(forms.Form):
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date'}))