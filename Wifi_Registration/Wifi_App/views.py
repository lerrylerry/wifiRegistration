from django.shortcuts import render, redirect
from Wifi_App.models import Faculty, Student, History

# Buttons===============

def index(request):
    return render(request, 'Wifi_App/HOMEPAGE.html')

def faculty(request):
    return render(request, 'Wifi_App/FACULTY.html')

def student(request):
    return render(request, 'Wifi_App/STUDENT.html')

def admin(request):
    return render(request, 'Wifi_App/ADMINLOGIN.html')

# request view of faculty
def readFaculty(request):
    data = Faculty.objects.all()
    context = {"faculty_request" : data}
    return render(request, 'Wifi_App/DATAFACULTY.html', context)

# request view of student
def readStudent(request):
    data2 = Student.objects.all()
    context = {"student_request" : data2}
    return render(request, 'Wifi_App/DATASTUDENT.html', context)

# data history view
def readHistory(request):
    data3 = History.objects.all()
    context = {"history" : data3}
    return render(request, 'Wifi_App/DATAHISTORY.html', context)

def success(request):
    return render(request, 'Wifi_App/success.html')

# CRUD/OTHERS================

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

                # for the faculty history
                history = History()
                history.names2 = request.POST.get('fname')
                history.email2 = request.POST.get('femail')
                history.macadd2 = request.POST.get('fmacadd')
                history.marked = 'Pending'
                history.kind = 'Faculty'

                history.save()

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
                submit.snames = request.POST.get('snames')
                submit.scourse = request.POST.get('scourse')
                submit.ssemester = request.POST.get('ssemester')
                submit.stupid = request.POST.get('stupid')
                submit.sornum = request.POST.get('sornum')
                submit.sphone = request.POST.get('sphone')
                submit.ssystem = request.POST.get('ssystem')
                submit.sothers = request.POST.get('sothers')
                submit.smacadd = request.POST.get('smacadd')
                submit.semail = request.POST.get('semail')
                submit.sresidAdd = request.POST.get('sresidAdd')
                #submit.schecked = request.POST.get('schecked')

                submit.save()

                # for the student history
                history = History()
                history.names2 = request.POST.get('sname')
                history.email2 = request.POST.get('semail')
                history.macadd2 = request.POST.get('smacadd')
                history.marked = 'Pending'
                history.kind = 'Student'

                history.save()

                return redirect('/faculty/success.html/')

            else:
                return render(request, 'Wifi_App/STUDENT.html')

        except:
            pass
    else:
        return render(request, 'Wifi_App/STUDENT.html')

# accept faculty
def acceptFaculty(request, faculty_pk):
    add = Faculty.objects.get(pk = faculty_pk)
    add.delete()
    add.fmark = 'Accepted' # changing pending status to 'Accepted'
    add.save()

    # remove this if the creation works
    history = History.objects.all() # getting data for history
    context = {"history":history}

    return render(request, 'Wifi/DATAHISTORY.html', context)

#accept student
def acceptStudent(request, student_pk):
    add = Student.objects.get(pk = student_pk)
    add.delete()
    add.smark = 'Accepted' # changing pending status to 'Accepted'
    add.save()

    # remove this if the creation works
    history = History.objects.all() # getting data for student
    context = {"history":history}

    return render(request, 'Wifi/DATAHISTORY.html', context)

# reject faculty
def rejectFaculty(request, faculty_pk):
    remove = Faculty.objects.get(pk = faculty_pk)
    remove.delete()
    return redirect('/df')

# reject student
def rejectStudent(request, student_pk):
    remove = Student.objects.get(pk = student_pk)
    remove.delete()
    return redirect('/dr')