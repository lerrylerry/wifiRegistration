from django.shortcuts import render, redirect
from staff.models import faculty

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
    staff=faculty.objects.create(
    f_name = request.POST['fname'],
    f_dept = request.POST['fdept'],
    f_design = request.POST['fdesign'],
    f_mac = request.POST['fmac'],
    f_device = request.POST['fdevice'],
    f_others = request.POST['fothers'],
    f_email = request.POST['femail'],
    f_phone = request.POST['fphone'],
    f_facname =request.POST['ffacname'],
    f_upload = request.POST['fupload'],
    f_date = request.POST['fdate'],
    )
    return render(request, 'Wifi_App/FACULTY.html')

def show(request):
    faculties = faculty.objects.all()
    return render(request, 'Wifi_App/DATAHISTORY.html')