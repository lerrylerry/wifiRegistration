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

    path('admin1/student_request/', views.readStudent, name='datastudent'),
    path('admin1/faculty_request/', views.readFaculty, name='datafaculty'),
    path('admin1/create_staff/', views.createStaff, name='createStaff'),

    path('viewCalendar/', views.viewCalendar, name='viewCalendar'),
    path('editCalendar/<int:id>', views.editCalendar, name='editCalendar'),
    path('updateCalendar/<int:id>', views.updateCalendar, name='updateCalendar'),

    path('contact_us/', views.contactUs, name='contactUs'),

    path('createStaff/', views.createStaff, name='createStaff'),
    path('register_faculty/success.html', views.success, name='success'),
    path('register_student/success.html', views.success, name='success'),
    path('email_sent/success.html', views.emailSuccess, name='emailSuccess'),

    path('generatePDF/', views.generatePDF, name='generatePDF'),
    path('notifyUserStudent/<user_pk>', views.notifyUserStudent, name='notifyUserStudent'),
    path('notifyUserFaculty/<user_pk>', views.notifyUserFaculty, name='notifyUserFaculty'),
    
    #path('to_pdf/', views.print_view, name='pdf'),
    #path('to_csv/', views.csv_view, name='csv'),

    path('acceptFaculty/<user_pk>', views.acceptFaculty, name='acceptFaculty'),
    path('rejectFaculty/<user_pk>', views.rejectFaculty, name='rejectFaculty'),
    path('acceptStudent/<user_pk>', views.acceptStudent, name='acceptStudent'),
    path('rejectStudent/<user_pk>', views.rejectStudent, name='rejectStudent'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)