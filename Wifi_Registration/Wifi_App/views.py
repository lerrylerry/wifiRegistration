from django.shortcuts import render, redirect, get_object_or_404
from Wifi_App.models import Faculty, Student, History, adminlogin
from django.contrib import messages
from Wifi_App.forms import facultyform, studentform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Buttons===============

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
                userType = 'Faculty',
            )
            submit.save()
            
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
                userType = 'Student',
            )
            submit.save()
            
            # redirect to success page
            return redirect('/student/success.html/')

        else:
            messages.error(request, "You're too fast! Please correct the errors first.")

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
    print("context: " , context)
    return render(request, 'Wifi_App/DATAHISTORY.html', context)

def success(request):
    return render(request, 'Wifi_App/success.html')

# CRUD/OTHERS================

# accept faculty
def acceptFaculty(request,faculty_pk):
    try:
        added = Faculty.objects.get(pk=faculty_pk)
        added.fmark = 'Accepted'
        added.save()

        # -------
        forhis = History.objects.get(email2 = added.femail)
        # changing pending status to 'Accepted'
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
'''
def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/dh')

    else:
        form = AuthenticateForm()

    return render(request, 'Wifi_App/ADMINLOGIN.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('Wifi_App/ADMINLOGIN.html')
'''