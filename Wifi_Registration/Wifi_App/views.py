from django.shortcuts import render, redirect

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
