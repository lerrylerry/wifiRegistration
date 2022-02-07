from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Faculty(models.Model):
    fnames = models.CharField(max_length=50)
    fdepartment = models.CharField(max_length=50)
    fdesignation = models.CharField(max_length=50)
    fmacadd = models.CharField(max_length=14)
    Device = [
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    fsystem = models.CharField(max_length=15, choices=Device)
    fothers = models.CharField(max_length=15, null=True, blank=True, default="None")
    femail = models.EmailField(max_length=50, unique=True, primary_key=True)
    fphone = models.IntegerField(unique=True)
    #fchecked = models.BooleanField()
    ffacultys = models.CharField(max_length=10)
    fupload = models.ImageField()
    fdate = models.DateTimeField(auto_now_add=True)
    ftype = models.CharField(max_length=10)
    fmark = models.CharField(max_length=10)

class Student(models.Model):
    snames = models.CharField(max_length=50)
    Course = [
                ('BSCE','BSCE'),
                ('BSEE','BSEE'),
                ('BSME','BSME'),
                ('BET-ET','BET-ET'),
                ('BET-ESET','BET-ESET'),
                ('BET-COET','BET-COET'),
                ('BET-CT','BET-CT'),
                ('BET-AT','BET-AT'),
                ('BET-MT','BET-MT'),
                ('BET-PPT','BET-PPT'),
                ('BET-ICT','BET-ICT'),
                ('BET-HE','BET-HE'),
                ('BET-AU','BET-AU'),
                ('BET-EI','BET-EI'),
                ('BET-E','BET-E'),
                ('BET-HVACT','BET-HVACT'),
                ('BET-CP','BET-CP')
    ]

    scourse = models.CharField(max_length=50, choices=Course)
    Semester = [
                ('First Semester','First Semester'),
                ('Second Semester','Second Semester'),
                ('Others...','Others...')
    ]

    ssemester = models.CharField(max_length=20, choices=Semester)
    stupid = models.CharField(max_length=12)
    sornum = models.IntegerField()
    sphone = models.IntegerField(unique=True)
    Device = [
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    ssystem = models.CharField(max_length=15, choices=Device)
    sothers = models.CharField(max_length=15, null=True, blank=True)
    smacadd = models.CharField(max_length=14)
    semail = models.EmailField(max_length=50, unique=True, primary_key=True)
    sresidAdd = models.CharField(max_length=200)
    supload = models.ImageField()
    #schecked = models.BooleanField()
    stype = models.CharField(max_length=10)
    smark = models.CharField(max_length=10)
    
class History(models.Model):
    names2 = models.CharField(max_length=50)
    email2 = models.EmailField(max_length=50, unique=True)
    macadd2 = models.CharField(max_length=14)
    kind = models.CharField(max_length=8)
    marked = models.CharField(max_length=8)
    timed = models.DateTimeField(auto_now_add=True)
    #start = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, null=True)
    #last = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)

class adminlogin(models.Model):
    username = models.CharField(max_length=50)
    adminpw = models.CharField(max_length=20)
