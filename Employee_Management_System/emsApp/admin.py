from django.contrib import admin
from .models import Employee,Department,Employee_Salary

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
        list_display = ('name','email','designation','reporting_manager' ,'departments')
        search_fields=('name', 'email', 'designation', 'departments')
        list_filter = ('designation', 'departments')

admin.site.register(Employee, EmployeeAdmin)

class DepartmentAdmin(admin.ModelAdmin):
        list_display = ('name', 'managers', 'floor')
        search_fields = ('name', 'floor')
        list_filter = ('floor',)

admin.site.register(Department, DepartmentAdmin)

class EmployeeSalaryAdmin(admin.ModelAdmin):
        list_display = ('salary', 'employee', 'from_Date', 'till_Date')
        search_fields = ('employee',)
        list_filter = ('salary', 'from_Date', 'till_Date')

admin.site.register(Employee_Salary,EmployeeSalaryAdmin)