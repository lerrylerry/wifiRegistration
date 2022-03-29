from django.shortcuts import render, redirect, get_object_or_404
from Wifi_App.models import Faculty, Student, History
from django.contrib import messages
from Wifi_App.forms import facultyform, studentform 
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from reportlab.pdfgen import canvas
import datetime
import io

#username = lerry123, password = wifi123

#unfinished task
def print_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello World")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="lerry.pdf")

def faculty(request):
    if request.method == 'POST':
        form = facultyform(request.POST,request.FILES)
        if form.is_valid():
            submit = Faculty.objects.create(
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
                decision = 'Pending',
                userType = 'Faculty',
            )
            if submit.otherDevice == '':
                submit.otherDevice = "-"
            submit.save()
            
            logged = History.objects.create(
                names = request.POST['names'],
                macadd = request.POST['macadd'],
                email = request.POST['email'],
                userType = 'Faculty',
                decision = 'Pending',
            )
            logged.save()

            # redirect to success page
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
            submit = Student.objects.create(
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
                decision = 'Pending',
                userType = 'Student',
            )
            if submit.otherDevice == '':
                submit.otherDevice = "-"
            submit.save()
            
            logged = History.objects.create(
                names = request.POST['names'],
                macadd = request.POST['macadd'],
                email = request.POST['email'],
                userType = 'Faculty',
                decision = 'Pending',
            )
            logged.save()

            # redirect to success page
            return redirect('/student/success.html/')

        else:
            messages.error(request, "You're too fast! Please correct the errors first.")

    else:
        form = studentform()
    return render(request, 'Wifi_App/STUDENT.html',{'form':form})

# request view of faculty
@login_required(login_url='/login/')
def readFaculty(request):
    excludes = ['Accepted','Rejected']
    data = Faculty.objects.exclude(decision__in=excludes)
    count = Student.objects.exclude(decision__in=excludes).count()
    context = {"faculty_request" : data, "count" :count}
    print(context)
    return render(request, 'Wifi_App/DATAFACULTY.html', context)

# request view of student
@login_required(login_url='/login/')
def readStudent(request):
    excludes = ['Accepted','Rejected']
    data2 = Student.objects.exclude(decision__in=excludes)
    count = Faculty.objects.exclude(decision__in=excludes).count()
    context = {"student_request" : data2, "count" :count}
    print(context)
    return render(request, 'Wifi_App/DATASTUDENT.html', context)

# data history view
@login_required(login_url='/login/')
def readHistory(request):
    excludes = ['Accepted','Rejected']
    history = History.objects.all()
    countA = Student.objects.exclude(decision__in=excludes).count()
    countB = Faculty.objects.exclude(decision__in=excludes).count()
    context = {"history" : history, "countA" :countA, "countB" :countB}
    print("context: " , context)
    return render(request, 'Wifi_App/DATAHISTORY.html', context)

def success(request):
    return render(request, 'Wifi_App/success.html')

# CRUD/OTHERS================

# accept faculty
def acceptFaculty(request,faculty_pk):
    try:
        added = Faculty.objects.get(pk=faculty_pk)
        added.decision = 'Accepted'
        added.save()

        # -------
        forhis = History.objects.get(email = added.email)
        # changing pending status to 'Accepted'
        forhis.decision = 'Accepted'
        forhis.dateEvaluated = datetime.datetime.now()
        forhis.save()

        return redirect('/df')

    except:
        pass

# reject faculty
def rejectFaculty(request,faculty2_pk):
    try:
        removed = Faculty.objects.get(pk=faculty2_pk)
        removed.decision = 'Rejected' # changing pending status to 'Rejected'
        removed.save()


        # -------
        forhis = History.objects.get(email = removed.email)
        forhis.decision = 'Rejected'
        forhis.dateEvaluated = datetime.datetime.now()
        forhis.save()

        return redirect('/df')
         
    except:
        pass

#accept student
def acceptStudent(request,student_pk):
    try:
        added = Student.objects.get(pk = student_pk)
        added.decision = 'Accepted' # changing pending status to 'Accepted'
        added.save()

        # -------
        forhis = History.objects.get(email = added.email)
        forhis.decision = 'Accepted'
        forhis.save()

        return redirect('/ds')

    except:
        pass

# reject student
def rejectStudent(request, student2_pk):
    try:
        removed = Student.objects.get(pk = student2_pk)
        removed.decision = 'Rejected' # changing pending status to 'Rejected'
        removed.save()

        # -------
        forhis = History.objects.get(email = removed.email)
        forhis.decision = 'Rejected'
        forhis.save()

        return redirect('/ds')

    except:
        pass