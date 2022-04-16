from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register_faculty/',views.register_faculty, name='register_faculty'),
    path('register_student/',views.register_student, name='register_student'),
    path('login_user/',views.login_user, name='login_user'),
    path('logout_user/',views.logout_user, name='logout_user'),
    path('print/',views.print_view, name='Ppdf'),
    path('facultyWifi/', views.facultyWifi, name='facultyWifi'),
    path('studentWifi/', views.studentWifi, name='studentWifi'),
    path('student_request/', views.readStudent, name='datastudent'),
    path('faculty_request/', views.readFaculty, name='datafaculty'),
    path('history/', views.readHistory, name='datahistory'),
    path('student/portal/', views.portal, name='portal_student'),
    path('faculty/portal/', views.portal, name='portal_faculty'),

    path('to_pdf/', views.print_view, name='pdf'),
    path('to_csv/', views.csv_view, name='csv'),

    path('faculty/success/', views.success, name='success'),
    path('student/success/', views.success, name='success'),
    path('acceptFaculty/<faculty_pk>', views.acceptFaculty, name='acceptFaculty'),
    path('rejectFaculty/<faculty_pk>', views.rejectFaculty, name='rejectFaculty'),
    path('acceptStudent/<student_pk>', views.acceptStudent, name='acceptStudent'),
    path('rejectStudent/<student_pk>', views.rejectStudent, name='rejectStudent'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)