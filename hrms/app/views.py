from django.shortcuts import render,HttpResponse
from .models import *
from .seriliazers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Count

import json

# Create your views here.
''' Views for left panel navigation start '''
def home(request):
    return render(request,'index.html')

def navAddEmployee(request):
    return render(request, 'addEmployee.html')

def navAllEmployee(request):
    return render(request, 'listAllEmployee.html')

def navAttendence(request):
    return render(request, 'attendence.html')

def navReport(request):
    return render(request, 'report.html')

def employeedetails(request):
    return render(request,'employee.html')

''' Views for left panel navigation end '''




@api_view(['POST',])
def addemployee(request):
    ''' use to add the employee in the records '''
    try:
        data =request.data
        print(data)
        print(type(data))
        result= Employee.objects.create(name=data['name'],email = data['email'],department = data['department'],designation = data['designation'],doj=data['doj'])
        return JsonResponse({'success':"success"})
    except Exception as e:
        return Response({"error" :"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(('GET',))
def allEmployeeDetails(request):
    ''' This method sends all the records of employee to frontend'''
    try:
        data = Employee.objects.filter().values()
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error" :"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getemployeedetails(request,id):
    ''' used to retrieve the record of a single particular employee'''
    try:
        print(id)
        emp_exists=Employee.objects.filter(id=id).exists()
        if emp_exists:
            print("hello")
            data = Employee.objects.filter(id = id).values().first()
            return Response(data)
        else:
            return Response({"error":"User with given id does not exists."})
    except Exception as e:
        return Response({"error":"Internal Server Error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def makeattendence(request):
    try:
        # print(request.data)
        data=Employee.objects.get(id=request.data['id'])
        attendance=eval(data.attendance)
        # print(attendance)
        if(request.data['type'] == 'clockin'):
            print('clockin')
            obj={
                "clockin":datetime.now().strftime("%m/%d/%Y , %H:%M:%S")
            }
            attendance.insert(0,obj)
            print(obj)
        else:
            print('clockout')
            attendance[0]['clockout'] = datetime.now().strftime("%m/%d/%Y , %H:%M:%S")
        data.attendance=attendance
        data.save()
        print(attendance)
        return Response({"success":"success"},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error" :"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getreportdata(request):
    try:
        ''' Sends the whole report containing department name and the no. of        employees in each department
        '''
        data = Employee.objects.values('department').annotate(total_employees=Count('id'))
        data = list(data)
        print(data)
        context = {
            'data':data
        }
        return Response(context,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error" :"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)