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
    path('admin1/student_request/', views.readStudent, name='datastudent'),
    path('admin1/faculty_request/', views.readFaculty, name='datafaculty'),
    path('admin1/history/', views.readHistory, name='datahistory'),
    path('student-portal/', views.portal, name='portal_student'),
    path('faculty-portal/', views.portal, name='portal_faculty'),
    path('faculty-portal/facultyWifi/', views.facultyWifi, name='facultyWifi'),
    path('student-portal/studentWifi/', views.studentWifi, name='studentWifi'),
    path('faculty-portal/facultyWifi/success.html', views.success, name='success'),
    path('student-portal/studentWifi/success.html', views.success, name='success'),

    path('to_pdf/', views.print_view, name='pdf'),
    path('to_csv/', views.csv_view, name='csv'),

    path('acceptFaculty/<user_pk>', views.acceptFaculty, name='acceptFaculty'),
    path('rejectFaculty/<user_pk>', views.rejectFaculty, name='rejectFaculty'),
    path('acceptStudent/<user_pk>', views.acceptStudent, name='acceptStudent'),
    path('rejectStudent/<user_pk>', views.rejectStudent, name='rejectStudent'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)