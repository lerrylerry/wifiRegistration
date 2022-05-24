from django.shortcuts import render, redirect, get_object_or_404
from Wifi_App.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Wifi_App.forms import *
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponse, HttpResponseForbidden
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime, csv , io
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage

'''username: lerry / password: akosilerry (admin account) // optional = email: sample@gmail.com'''

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
            )
            history.save()

            return redirect('/register_student/success.html')
    else:
        form = StudentForm
    time = Time.objects.get(id=1)
    context = {'form': form, 'time':time}
    return render(request, 'Wifi_App/STUDENT.html', context)

'''CREATE A STAFF'''
@login_required(login_url='/login_user/')
def createStaff(request):
    if request.user.userType == 'ADMIN':
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

    else:
        return HttpResponseForbidden()

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
            return redirect('/admin1/student_request')
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
@login_required(login_url='/login_user/')
def viewCalendar(request):
    if request.user.userType == 'ADMIN':
        time = get_object_or_404(Time, id=1)
        return render(request, 'Wifi_App/calendar.html', {'time': time})

    else:
        return HttpResponseForbidden()

'''EDIT CALENDAR'''
@login_required(login_url='/login_user/')
def editCalendar(request, id):
    if request.user.userType == 'ADMIN':
        time = get_object_or_404(Time, id=id)
        return render(request, 'Wifi_App/editCalendar.html', {'time': time})

    else:
        return HttpResponseForbidden()

'''UPDATE CALENDAR'''
@login_required(login_url='/login_user/')
def updateCalendar(request, id):
    if request.user.userType == 'ADMIN':
        time = get_object_or_404(Time, id=id)
        time.start = request.POST.get('first')
        time.end = request.POST.get('second')
        if time.start == "" or time.end == "":
            return redirect("/editCalendar/1")
        else:
            time.save()
            return redirect("/viewCalendar")
    else:
        return HttpResponseForbidden()

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
            return redirect('/email_sent/success.html')

    else:
        form = ContactForm()
    return render(request, 'Wifi_App/contact.html', {'form': form})

'''GENERATE PDF'''
@login_required(login_url='/login_user/')
def generatePDF(request):
    if request.user.userType == 'STAFF':
        names = request.GET['username']
        namez = names+'.pdf'
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFillColorRGB(1, 0, 0)
        can.setFont("Times-Roman", 16)
        can.drawString(270, 450, "username"+ ' : ' +request.GET['username'])
        can.drawString(270, 400, "password"+ ' : ' +request.GET['password'])
        can.showPage()
        can.save()
        packet.seek(0)
        return FileResponse(packet, as_attachment=True, filename=namez)

    else:
        return HttpResponseForbidden()
        
'''SEND EMAIL PDF STUDENT'''
@login_required(login_url='/login_user/')
def notifyUserStudent(request, user_pk):
    if request.user.userType == 'STAFF':
        stud = get_object_or_404(Student, pk=user_pk)
        stud.done = 1
        stud.save()
        attachment = AttachmentStudent(
            student=stud,
            attach=request.FILES['details']
            )
        attachment.save(force_insert=True)

        link = attachment.attach.file.name
        print(link)
        
        msg = EmailMessage(
            'WIFI REGISTRATION ACCOUNT',
            'You can now connect to wifi in tup-cavite!',
            settings.EMAIL_HOST_USER,
            [stud.email]
            )
        msg.content_subtype = "html"  
        msg.attach_file(link)
        msg.send()
        return redirect('/email_sent/success.html')

    else:
        return HttpResponseForbidden()

'''SEND EMAIL PDF FACULTY'''
@login_required(login_url='/login_user/')
def notifyUserFaculty(request, user_pk):
    if request.user.userType == 'STAFF':
        facs = get_object_or_404(Faculty, pk=user_pk)
        facs.done = 1
        facs.save()
        attachment = AttachmentFaculty(
            faculty=facs,
            attach=request.FILES['details']
            )
        attachment.save(force_insert=True)

        link = attachment.attach.file.name
        print(link)
        
        msg = EmailMessage(
            'WIFI REGISTRATION ACCOUNT',
            'You can now connect to wifi in tup-cavite!',
            settings.EMAIL_HOST_USER,
            [facs.email]
            )
        msg.content_subtype = "html"  
        msg.attach_file(link)
        msg.send()
        #success page
        return redirect('/email_sent/success.html')

    else:
        return HttpResponseForbidden()

'''email sent success'''
def emailSuccess(request):
    return render(request, 'Wifi_App/success_mail.html')

'''Faculty table'''
@login_required(login_url='/login_user/')
def readFaculty(request):
    if request.user.userType == 'ADMIN':
        allowed_faculty = Faculty.objects.filter(status='PENDING')
        student_count = Student.objects.filter(status='PENDING').count()
        all_faculty = Faculty.objects.filter(status='APPROVED')
        history = HistoryFaculty.objects.all()
        context = {"faculty_request" : allowed_faculty, "count" :student_count, "all_faculty":all_faculty, "history":history}
        return render(request, 'Wifi_App/DATAFACULTY.html', context)

    else:
        approved_faculty = Faculty.objects.filter(status='APPROVED', done=0)
        history = HistoryFaculty.objects.all()
        context = {"approved_faculty":approved_faculty, "history":history}
        return render(request, 'Wifi_App/DATAFACULTY.html', context)

'''Student table'''
@login_required(login_url='/login_user/')
def readStudent(request):
    if request.user.userType == 'ADMIN':
        allowed_student = Student.objects.filter(status='PENDING')
        faculty_count = Faculty.objects.filter(status='PENDING').count()
        all_student = Student.objects.filter(status='APPROVED')
        history = HistoryStudent.objects.all()
        context = {"student_request" : allowed_student, "count" : faculty_count, "all_student":all_student , "history":history}
        return render(request, 'Wifi_App/DATASTUDENT.html', context)

    else:
        approved_student = Student.objects.filter(status='APPROVED', done=0)
        history = HistoryStudent.objects.all()
        context = {"approved_student":approved_student, "history":history}
        return render(request, 'Wifi_App/DATASTUDENT.html', context)

'''APPROVED STUDENT'''
def acceptStudent(request,user_pk):
    if request.user.userType == 'ADMIN':
        add_student = get_object_or_404(Student, pk=user_pk)
        add_student.status = 'APPROVED'
        add_student.save()
        # ____________________________________________________________
        logged = HistoryStudent.objects.create(
            names = add_student.names,
            tupid = add_student.tupid,
            email = add_student.email,
            macadd = add_student.macadd,
            agenda = add_student.status,
        ) 
        logged.save()
        return redirect('/admin1/student_request')

    else:
        return HttpResponseForbidden()
        
'''APPROVED FACULTY'''
def acceptFaculty(request, user_pk):
    if request.user.userType == 'ADMIN':
        add_faculty = get_object_or_404(Faculty, pk=user_pk)
        add_faculty.status = 'APPROVED'
        add_faculty.save()
        
        logged = HistoryFaculty.objects.create(
            names = add_faculty.names,
            macadd = add_faculty.macadd,
            email = add_faculty.email,
            agenda = add_faculty.status,
        )
        logged.save()
        return redirect('/admin1/faculty_request')

    else:
        return HttpResponseForbidden()

'''REJECTED STUDENT'''
def rejectStudent(request, user_pk):
    if request.user.userType == 'ADMIN':
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
        ) 
        logged.save()
        return redirect('/admin1/student_request')

    else:
        return HttpResponseForbidden()
        
'''REJECTED STUDENT'''
def rejectFaculty(request, user_pk):
    if request.user.userType == 'ADMIN':
        destroy_faculty = get_object_or_404(Faculty, pk=user_pk)
        destroy_faculty.status = 'REJECTED'
        destroy_faculty.save()
        # ________________________________________________________________
        logged = HistoryFaculty.objects.create(
            names = destroy_faculty.names,
            macadd = destroy_faculty.macadd,
            email = destroy_faculty.email,
            agenda = destroy_faculty.status,
        ) 
        logged.save()
        return redirect('/admin1/faculty_request')

    else:
        return HttpResponseForbidden()