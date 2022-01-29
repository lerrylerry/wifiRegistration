from django.urls import path

from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('al/', views.admin, name='adminL'),
    path('faculty/', views.faculty, name='faculty'),
    path('student/', views.student, name='student'),
    path('dr/', views.dataReq, name='datarequest'),
    path('df/', views.dataFac, name='datafaculty'),
    path('dh/', views.dataHis, name='datahistory'),
    path('faculty/success.html/', views.success, name='success'),
    path('student/success.html/', views.success, name='success'),
    
]