from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.employeedetails, name=""),
    path('employeedetails/', views.employeedetails, name="employeedetails"),
    path('employee/add/', views.navAddEmployee, name="employee/add"),
    path('employee/all', views.navAllEmployee, name="employee/all"),
    path('attendence/', views.navAttendence, name="attendence"),
    path('report/', views.navReport, name="report"),



    path('getemployeedetails/', views.getemployeedetails, name="getemployeedetails"),
    path('addemployee/', views.addemployee, name="addemployee"),
    path('allEmployeeDetails/', views.allEmployeeDetails, name="allEmployeeDetails"),
    path('getAttendanceDetails/<int:id>', views.getAttendanceDetails, name="getAttendanceDetails"),

    path('makeattendence/', views.makeattendence, name="makeattendence"),
    path('getreportdata/', views.getreportdata, name="getreportdata"),


]