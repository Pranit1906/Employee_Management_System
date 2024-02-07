from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
Des_Choice = (
    ('Associate','Associate'),
    ('TL','TL'),
    ('Manager','Manager')
)

class Department(models.Model):
    name = models.CharField(max_length = 155)
    managers = models.ForeignKey('Employee', on_delete = models.SET_NULL, null=True, blank=True)
    floor = models.IntegerField()

    def get_employee_hierarchy(self):
        # Retrieve the manager for the department
        manager = Employee.objects.filter(departments=self, designation='Manager').first()

        # Retrieve team leads for the department
        team_leads = Employee.objects.filter(departments=self, designation='TL', reporting_manager = manager)
        
    
        associates_hierarchy = {}
        for tl in team_leads:
            associates = Employee.objects.filter(departments=self, designation='Associate', reporting_manager = tl)
            associates_hierarchy[tl] = associates
        
        hierarchy = {
            'Manager': manager,
            'TL': team_leads,
            'Associate': associates_hierarchy,
        }

        return hierarchy

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    address = models.TextField()
    designation = models.CharField(max_length=25, choices = Des_Choice)
    departments = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank = True)

    def clean(self):
        if self.designation != 'TL' and self.reporting_manager and self.reporting_manager.designation != 'TL' and self.reporting_manager.designation == 'Manager':
            raise ValidationError("Reporting manager must have the designation of TL can be assigned to Associates Only.")
    # clean function will make sure reporting manager will be decided depending on employee designation
    # if employee designation is Associate then he can report to Team Leader but can't report to manager directly
    # Team leader will report to managers only.     


    
    def __str__(self):
        return self.name

class Employee_Salary(models.Model):
    salary = models.DecimalField(max_digits = 10, decimal_places = 2)
    employee = models.ForeignKey(Employee, on_delete= models.CASCADE, null=True)
    from_Date = models.DateField()
    till_Date = models.DateField()

    def __str__(self):
        return f'{self.employee} - {self.salary}'