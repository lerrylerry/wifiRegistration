from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from Wifi_App.models import Faculty, Student, History
from django.contrib import messages

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
    #data = Faculty.objects.filter(fmacadd = '44-44-44-44-44').values('fmark').distinct()
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

#and request.POST.get('checked') == 'off'

# Create a faculty request
def createFaculty(request):
    if request.method == 'POST':
        try:
            if request.POST.get('fnames') and request.POST.get('fdepartment') and request.POST.get('fdesignation') \
                and request.POST.get('fmacadd') and request.POST.get('fsystem') and request.POST.get('fothers') \
                and request.POST.get('femail') and request.POST.get('fphone') \
                and request.POST.get('ffacultys') and request.POST.get('fupload'):

                submit = Faculty()
                submit.fnames = request.POST.get('fnames')
                submit.fdepartment = request.POST.get('fdepartment')
                submit.fdesignation = request.POST.get('fdesignation')
                submit.fmacadd = request.POST.get('fmacadd')
                submit.fsystem = request.POST.get('fsystem')
                submit.fothers = request.POST.get('fothers')
                submit.femail = request.POST.get('femail')
                submit.fphone = request.POST.get('fphone')
                submit.fupload = request.POST.get('fupload')
                #submit.fchecked = request.POST.get('fchecked')
                submit.ffacultys = request.POST.get('ffacultys')

                submit.save()

                # for the faculty history
                history = History()
                history.names2 = request.POST.get('fnames')
                history.email2 = request.POST.get('femail')
                history.macadd2 = request.POST.get('fmacadd')
                history.marked = 'Pending'
                history.kind = 'Faculty'

                history.save()
                print("win")

                return redirect('/faculty/success.html/')
                #return redirect('/dh')

            else:
                print("error2")
                return render(request, 'Wifi_App/FACULTY.html')

        except:
            pass
    else:
        print("error3")
        return render(request, 'Wifi_App/FACULTY.html')


#and request.POST.get('checked')

# Create a student request
def createStudent(request):
    if request.method == 'POST':
        try:
            if request.POST.get('snames') and request.POST.get('scourse') and request.POST.get('ssemester') \
                and request.POST.get('stupid') and request.POST.get('sornum') and request.POST.get('sphone') \
                and request.POST.get('ssystem') and request.POST.get('sothers') and request.POST.get('smacadd') \
                and request.POST.get('semail') and request.POST.get('sresidAdd') and request.POST.get('supload') :

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
                submit.supload = request.POST.get('fupload')
                #submit.schecked = request.POST.get('schecked')

                submit.save()

                # for the student history
                history = History()
                history.names2 = request.POST.get('snames')
                history.email2 = request.POST.get('semail')
                history.macadd2 = request.POST.get('smacadd')
                history.marked = 'Pending'
                history.kind = 'Student'

                history.save()
                print('win')

                return redirect('/student/success.html/')
                #return redirect('/dh')

            else:
                print('error2')
                return render(request, 'Wifi_App/STUDENT.html')

        except:
            pass
    else:
        print('error3')
        return render(request, 'Wifi_App/STUDENT.html')


# accept faculty
def acceptFaculty(request, faculty_pk):
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
def acceptStudent(request, student_pk):
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

        # -------
        forhis = History.objects.get(email2 = removed.semail)
        forhis.marked = 'Rejected'
        forhis.save()

        return redirect('/ds')

    except:
        pass