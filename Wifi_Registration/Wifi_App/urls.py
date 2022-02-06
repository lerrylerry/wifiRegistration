from unicodedata import name
from django.urls import path

from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('al/', views.admin, name='adminL'),
    path('faculty/', views.faculty, name='faculty'),
    path('student/', views.student, name='student'),
    path('ds/', views.readStudent, name='datastudent'),
    path('df/', views.readFaculty, name='datafaculty'),
    path('dh/', views.readHistory, name='datahistory'),
    path('faculty/success.html/', views.success, name='success'),
    path('student/success.html/', views.success, name='success'),
    path('createFaculty/<int:id>', views.createFaculty, name='createFaculty'),
    path('acceptFaculty/<int:id>', views.acceptFaculty, name='acceptFaculty'),
    path('acceptStudent/<int:id>', views.acceptStudent, name='acceptStudent'),
    path('rejectFaculty/<int:id>', views.rejectFaculty, name='rejectFaculty'),
    path('rejectStudent/<int:id>', views.readStudent, name='rejectStudent'),
]