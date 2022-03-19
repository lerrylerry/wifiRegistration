import re
from django import forms
from email import message
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from Wifi_App.models import Faculty, Student, History, adminlogin
from django.contrib import messages
from Wifi_App.forms import facultyform, studentform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.urls import reverse

# Buttons===============

def faculty(request):
    if request.method == 'POST':
        form = facultyform(request.POST,request.FILES)
        if form.is_valid():
            submit = Faculty.objects.create(
                fnames = request.POST['fnames'],
                fdepartment = request.POST['fdepartment'],
                fdesignation = request.POST['fdesignation'],
                fmacadd = request.POST['fmacadd'],
                fsystem = request.POST['fsystem'],
                fothers = request.POST['fothers'],
                femail = request.POST['femail'],
                fphone = request.POST['fphone'],
                fupload = request.FILES['fupload'],
                ffacultys = request.POST['ffacultys'],
            )
            submit.save()

            history = History.objects.create(
                names2 = request.POST['fnames'],
                email2 = request.POST['femail'],
                macadd2 = request.POST['fmacadd'],
                marked = 'Pending',
                kind = 'Faculty',
            )
            history.save()

            return redirect('/faculty/success.html/')
        
        else:
            print("dont know")

    else:
        form = facultyform()
    return render(request, 'Wifi_App/FACULTY.html', {'form': form})


def student(request):
    if request.method == 'POST':
        form = studentform(request.POST,request.FILES)
        if form.is_valid():
            submit = Student.objects.create(
                snames = request.POST['snames'],
                scourse = request.POST['scourse'],
                ssemester = request.POST['ssemester'],
                stupid = request.POST['stupid'],
                sornum = request.POST['sornum'],
                sphone = request.POST['sphone'],
                ssystem = request.POST['ssystem'],
                sothers = request.POST['sothers'],
                smacadd = request.POST['smacadd'],
                semail = request.POST['semail'],
                sresidAdd = request.POST['sresidAdd'],
                supload = request.FILES['supload'],
            )
            submit.save()

            history = History.objects.create(
                names2 = request.POST['snames'],
                email2 = request.POST['semail'],
                macadd2 = request.POST['smacadd'],
                marked = 'Pending',
                kind = 'Student',

            )
            history.save()

            return redirect('/student/success.html/')

        else:
            print("dont know")

    else:
        form = studentform()
    return render(request, 'Wifi_App/STUDENT.html',{'form':form})

def index(request):
    return render(request, 'Wifi_App/HOMEPAGE.html')


def admin(request):
    return render(request, 'Wifi_App/ADMINLOGIN.html')

# request view of faculty
def readFaculty(request):
    excludes = ['Accepted','Rejected']
    data = Faculty.objects.exclude(fmark__in=excludes)
    context = {"faculty_request" : data}
    return render(request, 'Wifi_App/DATAFACULTY.html', context)

# request view of student
def readStudent(request):
    excludes = ['Accepted','Rejected']
    data2 = Student.objects.exclude(smark__in=excludes)
    context = {"student_request" : data2}
    print(context)
    return render(request, 'Wifi_App/DATASTUDENT.html', context)

# data history view
def readHistory(request):
    history = History.objects.all()
    context = {"history" : history}
    print("history: " , history)
    print("context: " , context )
    return render(request, 'Wifi_App/DATAHISTORY.html', context)

def success(request):
    return render(request, 'Wifi_App/success.html')

# CRUD/OTHERS================

# accept faculty
def acceptFaculty(request,faculty_pk):
    try:
        added = Faculty.objects.get(pk=faculty_pk)
        added.fmark = 'Accepted' # changing pending status to 'Accepted'
        added.save()

        # -------
        forhis = History.objects.get(email2 = added.femail)
        forhis.marked = 'Accepted'
        forhis.save()

        return redirect('/df')

    except:
        pass

# reject faculty
def rejectFaculty(request,faculty2_pk):
    try:
        removed = Faculty.objects.get(pk=faculty2_pk)
        removed.fmark = 'Rejected' # changing pending status to 'Rejected'
        removed.save()


        # -------
        forhis = History.objects.get(email2 = removed.femail)
        forhis.marked = 'Rejected'
        forhis.save()

        return redirect('/df')
         
    except:
        pass

#accept student
def acceptStudent(request,student_pk):
    try:
        added = Student.objects.get(pk = student_pk)
        added.smark = 'Accepted' # changing pending status to 'Accepted'
        added.save()

        # -------
        forhis = History.objects.get(email2 = added.semail)
        forhis.marked = 'Accepted'
        forhis.save()

        return redirect('/ds')

    except:
        pass

# reject student
def rejectStudent(request, student2_pk):
    try:
        removed = Student.objects.get(pk = student2_pk)
        removed.smark = 'Rejected' # changing pending status to 'Rejected'
        removed.save()

        # -------
        forhis = History.objects.get(email2 = removed.semail)
        forhis.marked = 'Rejected'
        forhis.save()

        return redirect('/ds')

    except:
        pass