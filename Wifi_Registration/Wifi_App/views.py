from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Faculty
from .form import FacultyForm

def index(request):
    return render(request, 'Wifi_App/create.html')

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

def create_view(request):

    context = {}

    form = FacultyForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']=form
    return render(request, 'Wifi_App/faculty.html', context)