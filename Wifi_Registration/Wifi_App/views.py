from multiprocessing import context
from django.shortcuts import render, redirect
from Wifi_App.models import Faculty
from Wifi_App.form import FacultyForm

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

def fac(request):
    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass
    else:
        form = FacultyForm()
    return render(request, '', {'form' , form})

def show(request):
    person = Faculty.objects.all()
    return render(request, 'show.html', {'person' , person})

def edit(request,id):
    person = Faculty.objects.get(id=id)
    return render(request, 'edit.html', {'person' , person})

def update(request,id):
    person = Faculty.objects.get(id=id)
    form = FacultyForm(request.POST,instance=person)
    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request, 'edit.html', {'person' , person})

def delete(request,id):
    person = Faculty.objects.get(id=id)
    person.delete()
    return redirect("/show")