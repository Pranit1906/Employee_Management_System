from django.shortcuts import render,HttpResponseRedirect
from .forms import EmployeeForms,DepartmentForm,Employee_SalaryForm,ReportForm
from .models import Employee, Department, Employee_Salary
from django.contrib import messages
from django.db import models

# Create your views here.

# ---------------------------------------------   EMPLOYEE SECTION   ----------------------------------------------------------------------
def View_Employee(request):
    try:
        employee = Employee.objects.all()
        messages.success(request, 'Data Fetched SuccessFull!!')
        stored_messages = messages.get_messages(request)
        return render(request, 'employee.html',{'employee':employee,'messages':stored_messages})
    except  Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        stored_messages = messages.get_messages(request)
        return render(request, 'employee.html',{'messages':stored_messages}) 

def Create_Employee(request):
    try:
        if request.method == 'POST':
            employee_form = EmployeeForms(request.POST)
            if employee_form.is_valid():
                employee_form.save()
                messages.success(request, 'Employee Added SuccessFully!!')
                stored_messages = messages.get_messages(request)
                return HttpResponseRedirect('/view-employee/')
        else:
            employee_form = EmployeeForms()
            stored_messages = ''
        return render(request, 'create_employee.html', {'form':employee_form,'messages':stored_messages})
    except Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        stored_messages = messages.get_messages(request)
        return render(request, 'create_employee.html', {'form':employee_form,'messages':stored_messages})
    
def Update_Employee(request, id):
    try:
        if request.method == 'POST':
            emp = Employee.objects.get(pk=id)
            emp_form = EmployeeForms(request.POST, instance=emp)
            if emp_form.is_valid():
                emp_form.save()
                messages.success(request, 'Data Updated SuccessFully!!!')
                return HttpResponseRedirect('/view-employee/')
        else:
            emp = Employee.objects.get(pk = id)
            emp_form = EmployeeForms(instance=emp)
        return render(request, 'update_employee.html', {'form':emp_form,'messages':messages})
    except Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        return render(request, 'update_employee.html', {'form':emp_form, 'messgaes':messages})

def Delete_Employee(request,id):
    try:
        if request.method == 'POST':
            emp = Employee.objects.get(pk=id)
            emp.delete()
            messages.success(request, 'Data Deleted SuccessFully!!!')
            return HttpResponseRedirect('/view-employee/')
    except Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        return HttpResponseRedirect('/view-employee/')


# ---------------------------------------------   DEPARTMENT SECTION   ----------------------------------------------------------------------



def View_Department(request):
    try:
        department = Department.objects.all()
        messages.success(request, 'Data Fetched SuccessFull!!')
        stored_messages = messages.get_messages(request)
        return render(request, 'department.html',{'department':department,'messages':stored_messages})
    except  Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        stored_messages = messages.get_messages(request)
        return render(request, 'department.html',{'department':department,'messages':stored_messages})
    
def Create_Department(request):
    try:
        if request.method == 'POST':
            dept_form = DepartmentForm(request.POST)
            if dept_form.is_valid():
                dept_form.save()
                messages.success(request, 'Department Added SuccessFully!!')
                stored_messages = messages.get_messages(request)
                return HttpResponseRedirect('/view-department/')
        else:
            dept_form = DepartmentForm()
            stored_messages = ''
        return render(request, 'add_department.html', {'form':dept_form,'messages':stored_messages})
    except Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        stored_messages = messages.get_messages(request)
        return render(request, 'add_department.html', {'form':dept_form,'messages':stored_messages})

def Update_Department(request, id):
    try:
        if request.method == 'POST':
            dept = Department.objects.get(pk=id)
            dept_form = DepartmentForm(request.POST, instance=dept)
            if dept_form.is_valid():
                dept_form.save()
                messages.success(request, 'Data Updated SuccessFully!!!')
                return HttpResponseRedirect('/view-department/')
        else:
            dept = Department.objects.get(pk = id)
            dept_form = DepartmentForm(instance=dept)
        return render(request, 'update_department.html', {'form':dept_form, 'messages':messages})
    except Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        return render(request, 'update_department.html', {'form':dept_form, 'messgaes':messages})

def Delete_Department(request,id):
    try:
        if request.method == 'POST':
            dept = Department.objects.get(pk=id)
            dept.delete()
            messages.success(request, 'Data Deleted SuccessFully!!!')
            return HttpResponseRedirect('/view-department/')
    except Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        return HttpResponseRedirect('/view-department/')
    
def department_hierarchy(request, id):
    department = Department.objects.get(pk=id)
    hierarchy = department.get_employee_hierarchy()
    print('department:',department, 'hierarchy :',hierarchy)
    return render(request, 'department_hierarchy.html', {'department': department, 'hierarchy': hierarchy})


# ---------------------------------------------   SALARY SECTION   ----------------------------------------------------------------------
  


def View_Salary(request):
    try:
        salary = Employee_Salary.objects.all()
        print("salarY:,", salary[0].from_Date ,"-", salary[0].till_Date)
        messages.success(request, 'Data Fetched SuccessFull!!')
        stored_messages = messages.get_messages(request)
        return render(request, 'salary.html',{'salary':salary,'messages':stored_messages})
    except  Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        stored_messages = messages.get_messages(request)
        return render(request, 'salary.html',{'salary':salary,'messages':stored_messages}) 
 
def Create_Employee_Salary(request):
    try:
        if request.method == 'POST':
            sal_form = Employee_SalaryForm(request.POST)
            if sal_form.is_valid():
                sal_form.save()
                messages.success(request, 'Employee_Salary Added SuccessFully!!')
                stored_messages = messages.get_messages(request)
                return HttpResponseRedirect('/view-salary/')
        else:
            sal_form = Employee_SalaryForm()
            print("Sal_Form: ",sal_form)
            stored_messages = ''
        return render(request, 'add_salary.html', {'form':sal_form,'messages':stored_messages})
    except Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        stored_messages = messages.get_messages(request)
        return render(request, 'add_salary.html', {'form':sal_form,'messages':stored_messages})

def Update_Employee_Salary(request, id):
    try:
        if request.method == 'POST':
            sal = Employee_Salary.objects.get(pk=id)
            sal_form = Employee_SalaryForm(request.POST, instance=sal)
            if sal_form.is_valid():
                sal_form.save()
                messages.success(request, 'Data Updated SuccessFully!!!')
                return HttpResponseRedirect('/view-salary/')
        else:
            sal = Employee_Salary.objects.get(pk = id)
            sal_form = Employee_SalaryForm(instance=sal)
        return render(request, 'update_salary.html', {'form':sal_form, 'messages':messages})
    except Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        return render(request, 'update_salary.html', {'form':sal_form, 'messgaes':messages})

def Delete_Employee_Salary(request,id):
    try:
        if request.method == 'POST':
            sal = Employee_Salary.objects.get(pk=id)
            sal.delete()
            messages.success(request, 'Data Deleted SuccessFully!!!')
            return HttpResponseRedirect('/view-salary/')
    except Exception as e:
        messages.error(request, f'An Error Occured : {str(e)}')
        return HttpResponseRedirect('/view-salary/')
    

def Salary_Report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        salary_report_data = calculate_department_wise_salary(start_date, end_date)

        return render(request, 'salary_report.html', {'salary_report_data': salary_report_data, 'start_date': start_date, 'end_date': end_date})
    else:
        form = ReportForm()
    
    return render(request, 'salary_report_form.html',{'form':form})
    
    
    
    
    
def calculate_department_wise_salary(start_date, end_date):
    salary_report_data = Employee_Salary.objects.filter(
        from_Date__gte=start_date,
        till_Date__lte=end_date
    ).values('employee__department__name').annotate(total_salary_cost=models.Sum('salary'))
    print("salary_report_data :",salary_report_data)
    return salary_report_data