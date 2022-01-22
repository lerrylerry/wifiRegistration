from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'Wifi_App/BaseTemplate.html')

def faculty(request):
    return render(request, 'Wifi_App/index.html')

def student(request):
    return render(request, 'Wifi_App/STUDENT.html')