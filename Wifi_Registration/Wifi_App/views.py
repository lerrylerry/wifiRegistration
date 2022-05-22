from django.shortcuts import render, redirect, get_object_or_404
from Wifi_App.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Wifi_App.forms import *
from django.contrib.auth.decorators import login_required
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime, csv , io
from django.conf import settings
from django.core.mail import send_mail

'''HOMEPAGE'''
def index(request):
    return render(request, 'Wifi_App/home.html')

'''FACULTY REQUEST'''
def register_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            history = HistoryFaculty.objects.create(
                names = request.POST['names'],
                email = request.POST['email'],
                macadd = request.POST['macadd'],
                agenda = request.POST['agenda'],
                timeStamp = request.POST['timeStamp'],
            )
            history.save()

            return redirect('/register_faculty/success.html')
    else:
        form = FacultyForm
    time = Time.objects.get(id=1)
    context = {'form': form, 'time':time}
    return render(request, 'Wifi_App/FACULTY.html', context)

'''STUDENT REQUEST'''
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            history = HistoryStudent.objects.create(
                names = request.POST['names'],
                tupid = request.POST['tupid'],
                email = request.POST['email'],
                macadd = request.POST['macadd'],
                agenda = request.POST['agenda'],
                timeStamp = request.POST['timeStamp'],
            )
            history.save()

            return redirect('/register_student/success.html')
    else:
        form = StudentForm
    time = Time.objects.get(id=1)
    context = {'form': form, 'time':time}
    return render(request, 'Wifi_App/STUDENT.html', context)

'''CREATE A STAFF'''
def createStaff(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.userType = "STAFF"
            user.save()
            return redirect('/admin1/student_request/')
        else:
            messages.error(request, 'Invalid Account')

    else:
        form = SignUpForm()
    return render(request, 'Wifi_App/create_staff.html', {'form': form})

'''ADMIN & STAFF LOGIN'''
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.userType == 'ADMIN':
            login(request, user)
            return redirect('/admin1/student_request')
        elif user is not None and user.userType == 'STAFF':
            login(request, user)
            return redirect('/faculty-portal')
        else:
            messages.error(request, 'Account not found')
            return render(request, 'Wifi_App/login.html')
        
    else:
        return render(request, 'Wifi_App/login.html')

'''ADMIN & STAFF LOGOUT'''
def logout_user(request):
    logout(request)
    return redirect('home')

'''VIEW CALENDAR'''
def viewCalendar(request):
    time = get_object_or_404(Time, id=1)
    return render(request, 'Wifi_App/calendar.html', {'time': time})

'''EDIT CALENDAR'''
def editCalendar(request, id):
    time = get_object_or_404(Time, id=id)
    return render(request, 'Wifi_App/editCalendar.html', {'time': time})

'''UPDATE CALENDAR'''
def updateCalendar(request, id):
    time = get_object_or_404(Time, id=id)
    time.start = request.POST.get('first')
    time.end = request.POST.get('second')
    if time.start == "" or time.end == "":
        return redirect("/editCalendar/1")
    else:
        time.save()
        return redirect("/viewCalendar")

'''Send username and password'''
def verified(request):
    pass

'''Success page'''
def success(request):
    return render(request, 'Wifi_App/success-form.html')

'''Contact page'''
def contactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST['names'] + ' : ' + request.POST['subject']
            message = request.POST['content']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["johnlerry.laungayan@gsfe.tupcavite.edu.ph",]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('/contact_us/success.html')

    else:
        form = ContactForm()
    return render(request, 'Wifi_App/contact.html', {'form': form})

'''Faculty table'''
#@login_required(login_url='/login_user/')
def readFaculty(request):
    if request.user.userType == 'ADMIN':
        allowed_faculty = Faculty.objects.filter(status='PENDING')
        student_count = Student.objects.filter(status='PENDING').count()
        all_faculty = Faculty.objects.filter(status='APPROVED')
        history = HistoryFaculty.objects.all()
        context = {"faculty_request" : allowed_faculty, "count" :student_count, "all_faculty":all_faculty, "history":history}
        return render(request, 'Wifi_App/DATAFACULTY.html', context)

    else:
        approved_faculty = Faculty.objects.filter(status='APPROVED')
        all_faculty = Faculty.objects.all()
        context = {"approved_faculty":approved_faculty, "all_faculty":all_faculty}
        return render(request, 'Wifi_App/DATAFACULTY.html', context)

'''Student table'''
#@login_required(login_url='/login_user/')
def readStudent(request):
    if request.user.userType == 'ADMIN':
        allowed_student = Student.objects.filter(status='PENDING')
        faculty_count = Faculty.objects.filter(status='PENDING').count()
        all_student = Student.objects.filter(status='APPROVED')
        history = HistoryStudent.objects.all()
        context = {"student_request" : allowed_student, "count" : faculty_count, "all_student":all_student , "history":history}
        return render(request, 'Wifi_App/DATASTUDENT.html', context)

    else:
        approved_student = Student.objects.filter(status='APPROVED')
        all_student = Student.objects.all()
        context = {"approved_student":approved_student, "all_faculty":all_student}
        return render(request, 'Wifi_App/DATASTUDENT.html', context)

'''APPROVED STUDENT'''
def acceptStudent(request,user_pk):
    try:
        add_student = get_object_or_404(Student, emails=user_pk)
        add_student.status = 'APPROVED'
        add_student.save()
        # ____________________________________________________________
        logged = HistoryStudent.objects.create(
            names = add_student.names,
            tupid = add_student.tupid,
            email = add_student.email,
            macadd = add_student.macadd,
            agenda = add_student.status,
            timeStamp = datetime.datetime.now()
        ) 
        logged.save()
        return redirect('/admin1/student_request')

    except:
        pass
        
'''APPROVED FACULTY'''
def acceptFaculty(request, user_pk):
    try:
        add_faculty = get_object_or_404(Faculty, pk=user_pk)
        add_faculty.status = 'APPROVED'
        add_faculty.save()
        
        logged = HistoryFaculty.objects.create(
            names = add_faculty.names,
            macadd = add_faculty.macadd,
            email = add_faculty.email,
            agenda = add_faculty.status,
            timeStamp = datetime.datetime.now()
        )
        logged.save()
        return redirect('/admin1/faculty_request')

    except:
        pass

'''REJECTED STUDENT'''
def rejectStudent(request, user_pk):
    try:
        destroy_student = get_object_or_404(Student, pk=user_pk)
        destroy_student.status = 'REJECTED'
        destroy_student.save()
        # ________________________________________________________________
        logged = HistoryStudent.objects.create(
            names = destroy_student.names,
            tupid = destroy_student.tupid,
            email = destroy_student.email,
            macadd = destroy_student.macadd,
            agenda = destroy_student.status,
            timeStamp = datetime.datetime.now()
        ) 
        logged.save()
        return redirect('/admin1/student_request')

    except:
        pass
        
'''REJECTED STUDENT'''
def rejectFaculty(request, user_pk):
    try:
        destroy_faculty = get_object_or_404(Faculty, pk=user_pk)
        destroy_faculty.status = 'REJECTED'
        destroy_faculty.save()
        # ________________________________________________________________
        logged = HistoryFaculty.objects.create(
            names = destroy_faculty.names,
            macadd = destroy_faculty.macadd,
            email = destroy_faculty.email,
            agenda = destroy_faculty.status,
            timeStamp = datetime.datetime.now()
        ) 
        logged.save()
        return redirect('/admin1/faculty_request')

    except:
        pass