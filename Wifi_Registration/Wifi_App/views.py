from django.shortcuts import render, redirect, get_object_or_404
from Wifi_App.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Wifi_App.forms import FacultyForm, StudentForm, SignUpFormStudent, SignUpFormFaculty
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime
import csv
import io

#username = lerry123, password = wifi123

def index(request):
    return render(request, 'Wifi_App/home.html')

@login_required(login_url='/login_user/')
def portal(request):
    return render(request, 'Wifi_App/portal.html')

def register_faculty(request):
    if request.method == 'POST':
        faculty_account = SignUpFormFaculty(request.POST)
        if faculty_account.is_valid():
            user = faculty_account.save(commit=False)
            user.userType = 'FACULTY'
            user.decision = 'PENDING'
            user.save()
            #messages.success(request, 'Account created successfully')
            return redirect('/login_user/')
        else:
            messages.warning(request, 'Invalid account')

    else:
        faculty_account = SignUpFormFaculty()
        print("error")
    return render(request, 'Wifi_App/register_faculty.html', {'form': faculty_account})

def register_student(request):
    if request.method == 'POST':
        student_account = SignUpFormStudent(request.POST)
        if student_account.is_valid():
            user = student_account.save(commit=False)
            user.userType = 'STUDENT'
            user.decision = 'PENDING'
            user.save()
            #messages.success(request, 'Account created successfully')
            return redirect('/login_user/')
        else:
            messages.warning(request, 'Invalid account')

    else:
        student_account = SignUpFormStudent()
    return render(request, 'Wifi_App/register_student.html', {'form': student_account})

def login_user(request):
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.userType == 'ADMIN':
                login(request, user)
                return redirect('/history')
            if user is not None and user.userType == 'FACULTY':
                login(request, user)
                return redirect('/faculty/portal')
            if user is not None and user.userType == 'STUDENT':
                login(request, user)
                return redirect('/student/portal')
            else:
                messages.error(request, 'Account not found')
                return render(request, 'Wifi_App/login.html')
        
    else:
        return render(request, 'Wifi_App/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logout')
    return redirect('home')

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

# ----------------------------------------------------------------FACULTY FORM----------------------------------------------------------------------
@login_required(login_url='/login_user/')
def facultyWifi(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST,request.FILES)
        account = get_object_or_404(CustomUser, pk=request.user.email)
        if form.is_valid():
            submit = Faculty.objects.create(
                names = request.POST['names'],
                department = request.POST['department'],
                designation = request.POST['designation'],
                macadd = request.POST['macadd'],
                device = request.POST['device'],
                otherDevice = request.POST['otherDevice'],
                #email = request.POST['email'],
                phoneNum = request.POST['phoneNum'],
                signature = request.FILES['signature'],
                facultyName = request.POST['facultyName'],
                user = account,
                userType = account.userType,
                decision = account.decision,
            )
            if submit.otherDevice == '':
                submit.otherDevice = "-"
            submit.save()

            facs = Faculty.objects.get(user=submit.user)
            logged = History(
                faculty=facs,
            )
            logged.save(force_insert=True)

            return redirect('/faculty-portal/facultyWifi/success/')
        
        else:
            messages.error(request, "You're too fast! Please correct the errors first.")

    else:
        form = FacultyForm()
    return render(request, 'Wifi_App/FACULTY.html', {'form': form})

# ----------------------------------------------------------------STUDENT FORM----------------------------------------------------------------------
@login_required(login_url='/login_user/')
def studentWifi(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        account = get_object_or_404(CustomUser, pk=request.user.email)
        if form.is_valid():
            submit = Student.objects.create(
                names = request.POST['names'],
                course = request.POST['course'],
                semester = request.POST['semester'],
                #tupid = request.POST['tupid'],
                orNum = request.POST['orNum'],
                phoneNum = request.POST['phoneNum'],
                device = request.POST['device'],
                otherDevice = request.POST['otherDevice'],
                macadd = request.POST['macadd'],
                #email = request.POST['email'],
                residAdd = request.POST['residAdd'],
                signature = request.FILES['signature'],
                user = account,
                userType = account.userType,
                decision = account.decision,
            )
            if submit.otherDevice == '':
                submit.otherDevice = "-"
            submit.save()

            stud = Student.objects.get(user=submit.user)
            logged = History(
                student=stud,
            )
            logged.save(force_insert=True)

            return redirect('/student-portal/facultyWifi/success/')

        else:
            messages.error(request, "You're too fast! Please correct the errors first.")

    else:
        form = StudentForm()
    return render(request, 'Wifi_App/STUDENT.html',{'form':form})

# ====================================================================TABLES=================================================================

# ------------------------------------------------------------request view of faculty--------------------------------------------------------
#@login_required(login_url='/login_user/')
def readFaculty(request):
    allowed_faculty = Faculty.objects.filter(userType='FACULTY',decision='PENDING',agreement=0)
    student_count = Student.objects.filter(userType='STUDENT',decision='PENDING',agreement=0).count()
    context = {"faculty_request" : allowed_faculty, "count" :student_count}
    return render(request, 'Wifi_App/DATAFACULTY.html', context)

# ------------------------------------------------------------request view of student--------------------------------------------------------
#@login_required(login_url='/login_user/')
def readStudent(request):
    allowed_student = Student.objects.filter(userType='STUDENT',decision='PENDING',agreement=0)
    faculty_count = Faculty.objects.filter(userType='FACULTY',decision='PENDING',agreement=0).count()
    context = {"student_request" : allowed_student, "count" : faculty_count}
    return render(request, 'Wifi_App/DATASTUDENT.html', context)

# ------------------------------------------------------------data history view--------------------------------------------------------------
#@login_required(login_url='/login_user/')
def readHistory(request):
    history = History.objects.all()
    student_count = Student.objects.filter(userType='STUDENT',decision='PENDING',agreement=0).count()
    faculty_count = Faculty.objects.filter(userType='FACULTY',decision='PENDING',agreement=0).count()
    context = {"history" : history, "countA" :student_count, "countB" :faculty_count}
    return render(request, 'Wifi_App/DATAHISTORY.html', context)

def success(request):
    return render(request, "Wifi_App/success.html")

# ====================================================================CRUD===================================================================

# ***********************************************************ACCEPT / REJECT FACULTY*********************************************************
def acceptFaculty(request,faculty_pk):
    try:
        add_faculty = get_object_or_404(CustomUser, pk=faculty_pk)
        add_faculty.decision = 'ACCEPTED'
        add_faculty.save()
        # ____________________________________________________________
        history = get_object_or_404(History, faculty=add_faculty.email)
        history.dateEvaluated = datetime.datetime.now()
        history.save()
        return redirect('/faculty_request')

    except:
        pass

def rejectFaculty(request,faculty_pk):
    try:
        destroy_faculty = get_object_or_404(CustomUser, pk=faculty_pk)
        destroy_faculty.decision = 'REJECTED' # changing pending status to 'REJECTED'
        destroy_faculty.save()
        # ________________________________________________________________
        history = get_object_or_404(History, emails=destroy_faculty.email)
        history.dateEvaluated = datetime.datetime.now()
        history.save()
        return redirect('/faculty_request')
         
    except:
        pass
    

# ***********************************************************ACCEPT / REJECT STUDENT*********************************************************
def acceptStudent(request,student_pk):
    try:
        add_student = get_object_or_404(CustomUser, pk=student_pk)
        add_student.decision = 'ACCEPTED' # changing pending status to 'ACCEPTED'
        add_student.save()
        # ____________________________________________________________
        history = get_object_or_404(History, emails=add_student.email)
        history.dateEvaluated = datetime.datetime.now()
        history.save()
        return redirect('/student_request')

    except:
        pass

def rejectStudent(request, student_pk):
    try:
        destroy_faculty = get_object_or_404(CustomUser, pk=student_pk)
        destroy_faculty.decision = 'REJECTED' # changing pending status to 'REJECTED'
        destroy_faculty.save()
        # ________________________________________________________________
        history = get_object_or_404(History, emails=destroy_faculty.email)
        history.dateEvaluated = datetime.datetime.now()
        history.save()
        return redirect('/student_request')

    except:
        pass