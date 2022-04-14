from django.shortcuts import render, redirect, get_object_or_404
from Wifi_App.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Wifi_App.forms import LoginForm, facultyform, studentform, SignUpFormStudent, SignUpFormFaculty
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

def portal_student(request):
    return render(request, 'Wifi_App/student_portal.html')

def portal_faculty(request):
    return render(request, 'Wifi_App/faculty_portal.html')

def register_faculty(request):
    if request.method == 'POST':
        faculty_account = SignUpFormFaculty(request.POST)
        if faculty_account.is_valid():
            user = faculty_account.save(commit=False)
            user.userType = 'FACULTY'
            user.decision = 'PENDING'
            user.save()

            #messages.success(request, 'Account created successfully')
            return redirect('/login_user')
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
            return redirect('/login_user')
        else:
            messages.warning(request, 'Invalid account')

    else:
        student_account = SignUpFormStudent()
    return render(request, 'Wifi_App/register_student.html', {'form': student_account})

def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
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
                #messages.error(request, 'Account not found')
                return render(request, 'Wifi_App/login.html',{'form':form})
        
    else:
        form = LoginForm()
        #messages.error(request, 'Something went wrong!')
        return render(request, 'Wifi_App/login.html',{'form':form})

def logout_user(request):
    logout(request)
    #messages.success(request, 'You have successfully logout')
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
        form = facultyform(request.POST,request.FILES)
        account = get_object_or_404(CustomUser, pk=request.user.id)
        if form.is_valid():
            submit = Person.objects.create(
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
                user = account
            )
            if submit.otherDevice == '':
                submit.otherDevice = "-"
            submit.save()

            facs = Person.objects.get(user=submit.user)
            logged = History(
                macs=facs,
            )
            logged.save(force_insert=True)

            return redirect('/faculty/success/')
        
        else:
            messages.error(request, "You're too fast! Please correct the errors first.")

    else:
        form = facultyform()
    return render(request, 'Wifi_App/FACULTY.html', {'form': form})

# ----------------------------------------------------------------STUDENT FORM----------------------------------------------------------------------
@login_required(login_url='/login_user/')
def studentWifi(request):
    if request.method == 'POST':
        form = studentform(request.POST,request.FILES)
        account = get_object_or_404(CustomUser, pk=request.user.id)
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
                user = account,
                userType='STUDENT',
            )
            if submit.otherDevice == '':
                submit.otherDevice = "-"
            submit.save()

            stud = Person.objects.get(user=submit.user)
            logged = History(
                macs=stud,
            )
            logged.save(force_insert=True)

            return redirect('/student/success/')

        else:
            messages.error(request, "You're too fast! Please correct the errors first.")

    else:
        form = studentform()
    return render(request, 'Wifi_App/STUDENT.html',{'form':form})

# ====================================================================TABLES=================================================================

# ------------------------------------------------------------request view of faculty--------------------------------------------------------
@login_required(login_url='/login_user/')
def readFaculty(request):
    allowed_faculty = CustomUser.objects.filter(userType = 'FACULTY',decision = 'PENDING')
    student_count = CustomUser.objects.filter(userType = 'STUDENT',decision = 'PENDING').count()
    context = {"faculty_request" : allowed_faculty, "count" :student_count}
    return render(request, 'Wifi_App/DATAFACULTY.html', context)

# ------------------------------------------------------------request view of student--------------------------------------------------------
@login_required(login_url='/login_user/')
def readStudent(request):
    allowed_student = CustomUser.objects.filter(userType = 'STUDENT',decision = 'PENDING')
    faculty_count = CustomUser.objects.filter(userType = 'FACULTY',decision = 'PENDING').count()
    context = {"student_request" : allowed_student, "count" : faculty_count}
    return render(request, 'Wifi_App/DATASTUDENT.html', context)

# ------------------------------------------------------------data history view--------------------------------------------------------------
@login_required(login_url='/login_user/')
def readHistory(request):
    history = History.objects.all()
    student_count = CustomUser.objects.filter(userType = 'STUDENT',decision = 'PENDING').count()
    faculty_count = CustomUser.objects.filter(userType = 'FACULTY',decision = 'PENDING').count()
    context = {"history" : history, "countA" :student_count, "countB" :faculty_count}
    return render(request, 'Wifi_App/DATAHISTORY.html', context)

def success(request):
    return render(request, "Wifi_App/success.html")

# ====================================================================CRUD===================================================================

# ****************************************************************accept faculty*************************************************************
def acceptFaculty(request,faculty_pk):
    try:
        added = Person.objects.get(pk=faculty_pk)
        added.decision = 'ACCEPTED'
        added.save()
        # -------
        forhis = History.objects.get(emails=added.email)
        forhis.dateEvaluated = datetime.datetime.now()
        forhis.save()

        return redirect('/faculty_request')

    except:
        pass

# ****************************************************************reject faculty*************************************************************
def rejectFaculty(request,faculty_pk):
    try:
        removed = Person.objects.get(pk=faculty_pk)
        removed.decision = 'REJECTED' # changing pending status to 'REJECTED'
        removed.save()

        forhis = History.objects.get(emails=removed.email)
        forhis.dateEvaluated = datetime.datetime.now()
        forhis.save()

        return redirect('/faculty_request')
         
    except:
        pass

# ****************************************************************accept student*************************************************************
def acceptStudent(request,student_pk):
    try:
        added = Person.objects.get(pk = student_pk)
        added.decision = 'ACCEPTED' # changing pending status to 'ACCEPTED'
        added.save()
        # -------
        forhis = History.objects.get(emails=added.email)
        forhis.dateEvaluated = datetime.datetime.now()
        forhis.save()

        return redirect('/student_request')

    except:
        pass

# ****************************************************************reject student*************************************************************
def rejectStudent(request, student2_pk):
    try:
        removed = Person.objects.get(pk = student2_pk)
        removed.decision = 'REJECTED' # changing pending status to 'REJECTED'
        removed.save()
        # -------
        forhis = History.objects.get(emails=removed.email)
        forhis.dateEvaluated = datetime.datetime.now()
        forhis.save()

        return redirect('/student_request')

    except:
        pass