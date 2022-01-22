from django.urls import path

from  . import views

urlpatterns = [
    path('hi/', views.index, name='index'),
    path('faculty/', views.faculty, name='faculty'),
    path('student/', views.student, name='student'),
]