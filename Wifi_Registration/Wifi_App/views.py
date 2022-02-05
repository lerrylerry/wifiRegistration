from django.shortcuts import render, redirect
from Wifi_App.models import Faculty, Student

# Buttons

def index(request):
    return render(request, 'Wifi_App/HOMEPAGE.html')

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

# CRUD/OTHERS

# Create a faculty request
def createFaculty(request):
    if request.method == 'POST':
        try:
            if request.POST.get('names') and request.POST.get('department') and request.POST.get('designation') \
                and request.POST.get('macadd') and request.POST.get('system') and request.POST.get('others') \
                and request.POST.get('email') and request.POST.get('phone') and request.POST.get('checked') \
                and request.POST.get('facultys') and request.POST.get('upload'):

                submit = Faculty()
                submit.names = request.POST.get('names')
                submit.department = request.POST.get('department')
                submit.designation = request.POST.get('designation')
                submit.macadd = request.POST.get('macadd')
                submit.system = request.POST.get('system')
                submit.others = request.POST.get('others')
                submit.email = request.POST.get('email')
                submit.phone = request.POST.get('phone')
                submit.checked = request.POST.get('checked')
                submit.facultys = request.POST.get('facultys')

                submit.save()
                return redirect('/faculty/success.html/')

            else:
                return render(request, 'Wifi_App/FACULTY.html')

        except:
            pass
    else:
        return render(request, 'Wifi_App/FACULTY.html')


# Create a student request
def createStudent(request):
    if request.method == 'POST':
        try:
            if request.POST.get('names') and request.POST.get('course') and request.POST.get('semester') \
                and request.POST.get('tupid') and request.POST.get('ornum') and request.POST.get('phone') \
                and request.POST.get('system') and request.POST.get('others') and request.POST.get('macadd') \
                and request.POST.get('email') and request.POST.get('residAdd') and request.POST.get('checked'):

                submit = Student()
                submit.names = request.POST.get('names')
                submit.course = request.POST.get('course')
                submit.semester = request.POST.get('semester')
                submit.tupid = request.POST.get('tupid')
                submit.ornum = request.POST.get('ornum')
                submit.phone = request.POST.get('phone')
                submit.system = request.POST.get('system')
                submit.others = request.POST.get('others')
                submit.macadd = request.POST.get('macadd')
                submit.email = request.POST.get('email')
                submit.residAdd = request.POST.get('residAdd')
                submit.checked = request.POST.get('checked')

                submit.save()
                return redirect('/faculty/success.html/')

            else:
                return render(request, 'Wifi_App/STUDENT.html')

        except:
            pass
    else:
        return render(request, 'Wifi_App/STUDENT.html')

def acceptFaculty():
    pass

def acceptStudent():
    pass

def rejectFaculty():
    pass

def rejectStudent():
    pass

def readFaculty():
    pass

def readStudent():
    pass

def readHistory():
    pass