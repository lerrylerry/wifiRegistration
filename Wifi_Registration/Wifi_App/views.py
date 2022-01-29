from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'Wifi_App/HOMEPAGE.html')

def faculty(request):
    return render(request, 'Wifi_App/FACULTY.html')

def student(request):
    return render(request, 'Wifi_App/STUDENT.html')

def admin(request):
    return render(request, 'Wifi_App/ADMINLOGIN.html')

def dataReq(request):
    return render(request, 'Wifi_App/DATA REQUEST.html')

def dataFac(request):
    return render(request, 'Wifi_App/DATAFACULTY.html')

def dataHis(request):
    return render(request, 'Wifi_App/DATAHISTORY.html')

def success(request):
    return render(request, 'Wifi_App/success.html')

def createFaculty(request):
    f_name = request.POST['fullname'],
    f_dept = request.POST['dept'],
    f_design = request.POST['design'],
    f_mac = request.POST['mac'],
    f_device = request.POST['device'],
    f_others = request.POST['others'],
    f_email = request.POST['email'],
    f_phone = request.POST['phone'],
    f_facname =request.POST['facname'],
    f_upload = request.POST['upload'],
    f_date = request.POST['date'],
    person = Faculty(f_name = f_name, f_dept = f_dept, f_design = f_design, f_mac = f_mac, f_device = f_device, f_others = f_others, f_email = f_email
                    , f_phone = f_phone, f_facname = f_facname, f_upload = f_upload, f_date = f_date)
    person.save()

    faculties = Faculty.objects.all()
    context = {
        'faculties' : faculties
    }
    return render(request, 'Wifi_App/DATAHISTORY.html', context)