from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('al/', views.admin, name='adminL'),
    path('faculty/', views.createFaculty, name='faculty'),
    path('student/', views.createStudent, name='student'),
    path('ds/', views.readStudent, name='datastudent'),
    path('df/', views.readFaculty, name='datafaculty'),
    path('dh/', views.readHistory, name='datahistory'),
    path('faculty/success.html/', views.success, name='success'),
    path('student/success.html/', views.success, name='success'),
    #path('createFaculty/', views.createFaculty, name='createFaculty'),
    #path('createStudent/', views.createStudent, name='createStudent'),
    path('acceptFaculty/<faculty_pk>', views.acceptFaculty, name='acceptFaculty'),
    path('rejectFaculty/<faculty2_pk>', views.rejectFaculty, name='rejectFaculty'),
    path('acceptStudent/<student_pk>', views.acceptStudent, name='acceptStudent'),
    path('rejectStudent/<student2_pk>', views.rejectStudent, name='rejectStudent'),
]