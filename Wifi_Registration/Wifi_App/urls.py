from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
#from Wifi_App.views import FacultyView
#from Wifi_App.views import HomeView, DataHistoryView
#from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.index, name='home'),
    path('print/',views.print_view, name='Ppdf'),
    path('faculty/', views.faculty, name='faculty'),
    path('student/', views.student, name='student'),
    path('ds/', views.readStudent, name='datastudent'),
    path('df/', views.readFaculty, name='datafaculty'),
    #path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page = 'home'), name='logout'),
    #path('datahistory/',DataHistoryView.as_view(), name="datahistory"),
    path('dh/', views.readHistory, name='datahistory'),
    path('faculty/success.html/', views.success, name='success'),
    path('student/success.html/', views.success, name='success'),
    path('acceptFaculty/<faculty_pk>', views.acceptFaculty, name='acceptFaculty'),
    path('rejectFaculty/<faculty2_pk>', views.rejectFaculty, name='rejectFaculty'),
    path('acceptStudent/<student_pk>', views.acceptStudent, name='acceptStudent'),
    path('rejectStudent/<student2_pk>', views.rejectStudent, name='rejectStudent'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
        #urlpatterns += static(settings.MEDIA_URL,
                              #document_root=settings.MEDIA_ROOT)