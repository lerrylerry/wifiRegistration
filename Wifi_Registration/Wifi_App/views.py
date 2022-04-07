#from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render, redirect
from Wifi_App.models import Person, History
from django.contrib import messages
from Wifi_App.forms import facultyform, studentform 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime
import csv
import os
import io

#username = lerry123, password = wifi123

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        form = UserCreationForm()

    return render(request, 'cadmin/register.html', {'form': form})

#unfinished task
def print_view(request):
    packet = io.BytesIO()#
    can = canvas.Canvas(packet, pagesize=letter)#
    can.setFillColorRGB(1, 0, 0)
    can.setFont("Times-Roman", 14)
    can.drawString(70, 655, "Hello from Python")
    #can.showPage()#
    can.save()#
    packet.seek(0)#

    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(open("Wifi_App/files/TUPC-F-OCD-OIT-04 (WIFI-CONNECTIVITY REGISTRATION FORM STUDENT).pdf", "rb"))
    output = PdfFileWriter()

    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    outputStream = open("Wifi_App/files/Your.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

    with open("Wifi_App/files/Your.pdf", 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=form_request.pdf'
        return response
    #return FileResponse(packet, as_attachment=True, filename="form_request.pdf")#

def csv_view(request):
    # object
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Content-Disposition': 'attachment; filename = "lerry.csv"'},
    )
    # instance
    writer = csv.writer(response)

    # data to be inputted
    count = History.objects.all().count()
    context = History.objects.all()
    writer.writerow(['Name', 'Email', 'Mac Address','User Type', 'Decision', 'Date Created', 'Date Evaluated'])
    for data in range(count):
        #writer.writerow([context[data].names, context[data].department, context[data].designation , context[data].device, context[data].otherDevice, context[data].phoneNum, 
        #                context[data].email, context[data].macadd, context[data].facultyName, context[data].signature])

        writer.writerow([context[data].names, context[data].email, context[data].macadd, context[data].userType, 
                        context[data].decision, context[data].dateCreated, context[data].dateEvaluated])
    return response

def faculty(request):
    if request.method == 'POST':
        form = facultyform(request.POST,request.FILES)
        if form.is_valid():
            submit = Person.objects.create(
                names = request.POST['names'],
                department = request.POST['department'],
                designation = request.POST['designation'],
                macadd = request.POST['macadd'],
                device = request.POST['device'],
                otherDevice = request.POST['otherDevice'],
                email = request.POST['email'],
                phoneNum = request.POST['phoneNum'],
                signature = request.FILES['signature'],
                facultyName = request.POST['facultyName'],
                decision = 'PENDING',
                userType='FACULTY',
            )
            if submit.otherDevice == '':
                submit.otherDevice = "-"
            submit.save()

            fac = Person.objects.get(email=submit.email)
            logged = History(
                emails=fac,
            )
            logged.save(force_insert=True)

            return redirect('/faculty/success.html/')
        
        else:
            messages.error(request, "You're too fast! Please correct the errors first.")

    else:
        form = facultyform()
    return render(request, 'Wifi_App/FACULTY.html', {'form': form})

def student(request):
    if request.method == 'POST':
        form = studentform(request.POST,request.FILES)
        if form.is_valid():
            submit = Person.objects.create(
                names = request.POST['names'],
                course = request.POST['course'],
                semester = request.POST['semester'],
                tupid = request.POST['tupid'],
                orNum = request.POST['orNum'],
                phoneNum = request.POST['phoneNum'],
                device = request.POST['device'],
                otherDevice = request.POST['otherDevice'],
                macadd = request.POST['macadd'],
                email = request.POST['email'],
                residAdd = request.POST['residAdd'],
                signature = request.FILES['signature'],
                decision = 'PENDING',
                userType='STUDENT',
            )
            if submit.otherDevice == '':
                submit.otherDevice = "-"
            submit.save()

            stud = Person.objects.get(email=submit.email)
            logged = History(
                emails=stud,
            )
            logged.save(force_insert=True)

            return redirect('/student/success.html/')

        else:
            messages.error(request, "You're too fast! Please correct the errors first.")

    else:
        form = studentform()
    return render(request, 'Wifi_App/STUDENT.html',{'form':form})

# request view of faculty
@login_required(login_url='/login/')
def readFaculty(request):
    excludes = ['ACCEPTED','REJECTED']
    faculty_data = Person.objects.get(userType = 'FACULTY')
    allowed = faculty_data.exclude(decision__in=excludes)
    student_data = Person.objects.get(userType = 'STUDENT')
    student_count = student_data.exclude(decision__in=excludes).count()
    context = {"faculty_request" : allowed, "count" :student_count}
    print(context)
    return render(request, 'Wifi_App/DATAFACULTY.html', context)

# request view of student
@login_required(login_url='/login/')
def readStudent(request):
    excludes = ['ACCEPTED','REJECTED']
    student_data = Person.objects.get(userType = 'STUDENT')
    allowed = student_data.exclude(decision__in=excludes)
    faculty_data = Person.objects.get(userType = 'FACULTY')
    faculty_count = faculty_data.exclude(decision__in=excludes).count()
    context = {"student_request" : allowed, "count" : faculty_count}
    print(context)
    return render(request, 'Wifi_App/DATASTUDENT.html', context)

# data history view
@login_required(login_url='/login/')
def readHistory(request):
    excludes = ['ACCEPTED','REJECTED']
    history = History.objects.all()
    pending_stud = Person.objects.get(userType = 'STUDENT')
    student_count = pending_stud.exclude(decision__in=excludes).count()
    pending_fac = Person.objects.get(userType = 'FACULTY')
    faculty_count = pending_fac.exclude(decision__in=excludes).count()
    context = {"history" : history, "countA" :student_count, "countB" :faculty_count}
    print("context: " , context)
    return render(request, 'Wifi_App/DATAHISTORY.html', context)

def success(request):
    return render(request, "Wifi_App/success.html")

# CRUD/OTHERS================

# accept faculty
def acceptFaculty(request,faculty_pk):
    try:
        added = Person.objects.get(pk=faculty_pk)
        added.decision = 'ACCEPTED'
        added.save()
        # -------
        forhis = History.objects.get(emails=added.email)
        forhis.dateEvaluated = datetime.datetime.now()
        forhis.save()

        return redirect('/df')

    except:
        pass

# reject faculty
def rejectFaculty(request,faculty_pk):
    try:
        removed = Person.objects.get(pk=faculty_pk)
        removed.decision = 'REJECTED' # changing pending status to 'REJECTED'
        removed.save()

        forhis = History.objects.get(emails=removed.email)
        forhis.dateEvaluated = datetime.datetime.now()
        forhis.save()

        return redirect('/df')
         
    except:
        pass

#accept student
def acceptStudent(request,student_pk):
    try:
        added = Person.objects.get(pk = student_pk)
        added.decision = 'ACCEPTED' # changing pending status to 'ACCEPTED'
        added.save()
        # -------
        forhis = History.objects.get(emails=added.email)
        forhis.dateEvaluated = datetime.datetime.now()
        forhis.save()

        return redirect('/ds')

    except:
        pass

# reject student
def rejectStudent(request, student2_pk):
    try:
        removed = Person.objects.get(pk = student2_pk)
        removed.decision = 'REJECTED' # changing pending status to 'REJECTED'
        removed.save()
        # -------
        forhis = History.objects.get(emails=removed.email)
        forhis.dateEvaluated = datetime.datetime.now()
        forhis.save()

        return redirect('/ds')

    except:
        pass