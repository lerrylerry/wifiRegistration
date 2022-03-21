from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

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
    path('acceptFaculty/<faculty_pk>', views.acceptFaculty, name='acceptFaculty'),
    path('rejectFaculty/<faculty2_pk>', views.rejectFaculty, name='rejectFaculty'),
    path('acceptStudent/<student_pk>', views.acceptStudent, name='acceptStudent'),
    path('rejectStudent/<student2_pk>', views.rejectStudent, name='rejectStudent'),
    #path('accounts/login/',views.readFaculty),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
        #urlpatterns += static(settings.MEDIA_URL,
                              #document_root=settings.MEDIA_ROOT)