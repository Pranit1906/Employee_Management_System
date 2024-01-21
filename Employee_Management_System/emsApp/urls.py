from django.urls import path
from . import views

urlpatterns =[
    #---------------------  Employee Urls  ---------------------------
    path('view-employee/',views.View_Employee, name='view-employee'),
    path('add-employee/', views.Create_Employee, name='add-employee'),
    path('update-employee/<int:id>', views.Update_Employee, name='update-employee'),
    path('delete-employee/<int:id>/',views.Delete_Employee, name='delete-employee'),

    #---------------------  Department Urls  ---------------------------
    path('view-department/',views.View_Department, name='view-department'),
    path('add-department/', views.Create_Department, name='add-department'),
    path('update-department/<int:id>', views.Update_Department, name='update-department'),
    path('delete-department/<int:id>/',views.Delete_Department, name='delete-department'),
    path('department/<int:id>/hierarchy/', views.department_hierarchy, name='department_hierarchy'),

    #---------------------  Salary Urls  ---------------------------
    path('view-salary/',views.View_Salary, name='view-salary'),
    path('add-salary/', views.Create_Employee_Salary, name='add-salary'),
    path('update-salary/<int:id>', views.Update_Employee_Salary, name='update-salary'),
    path('delete-salary/<int:id>/',views.Delete_Employee_Salary, name='delete-salary'),
    path('salary-report/',views.Salary_Report,name='salary-report')
]