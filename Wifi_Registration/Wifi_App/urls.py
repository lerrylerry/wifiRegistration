from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #path('', views.index, name='home'),
    path('print/',views.print_view, name='Ppdf'),
    path('faculty/', views.faculty, name='faculty'),
    path('student/', views.student, name='student'),
    path('ds/', views.readStudent, name='datastudent'),
    path('df/', views.readFaculty, name='datafaculty'),
    path('dh/', views.readHistory, name='datahistory'),

    path('to_pdf/', views.print_view, name='pdf'),
    path('to_csv/', views.csv_view, name='csv'),

    path('faculty/success.html/', views.success, name='success'),
    path('student/success.html/', views.success, name='success'),
    path('acceptFaculty/<faculty_pk>', views.acceptFaculty, name='acceptFaculty'),
    path('rejectFaculty/<faculty_pk>', views.rejectFaculty, name='rejectFaculty'),
    path('acceptStudent/<student_pk>', views.acceptStudent, name='acceptStudent'),
    path('rejectStudent/<student_pk>', views.rejectStudent, name='rejectStudent'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)