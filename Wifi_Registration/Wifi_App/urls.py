from django.urls import path

from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminLogin/', views.admin, name='adminL'),
    path('faculty/', views.faculty, name='faculty'),
    path('student/', views.student, name='student'),
    path('dataRequest/', views.dataReq, name='datarequest'),
    path('dataFaculty/', views.dataFac, name='datafaculty'),
    path('dataHistory/', views.dataFac, name='datahistory'),
    path('success/', views.success, name='success'),
    
]