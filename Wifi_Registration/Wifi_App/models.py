from tabnanny import check
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
    femail = models.EmailField(primary_key=True, max_length=50, unique=True)
    fphone = models.DecimalField(max_digits=11, decimal_places=0, unique=True, verbose_name='Phone No')
    fchecked = models.BooleanField()
    ffacultys = models.CharField(max_length=10)
    fupload = models.ImageField()
    fdate = models.DateTimeField(auto_now_add=True)
    ftype = models.CharField(max_length=10)
    fmark = models.CharField(max_length=10, blank=True, null=True ,default="Pending")

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
    stupid = models.IntegerField(primary_key=True)
    sornum = models.IntegerField()
    sphone = models.DecimalField(max_digits=11, decimal_places=0, unique=True)
    Device = [
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    ssystem = models.CharField(max_length=15, choices=Device, default='')
    sothers = models.CharField(max_length=15, null=True, blank=True)
    smacadd = models.CharField(max_length=14)
    semail = models.EmailField(max_length=50, unique=True)
    sresidAdd = models.CharField(max_length=200)
    schecked = models.BooleanField()
    stype = models.CharField(max_length=10)
    smark = models.CharField(max_length=10, blank=True, null=True ,default="Pending")
    
class History(models.Model):
    names2 = models.CharField(max_length=50)
    email2 = models.EmailField(max_length=50, unique=True)
    macadd2 = models.CharField(max_length=14)
    kind = models.CharField(max_length=8)
    marked = models.CharField(max_length=8)
    timed = models.DateTimeField(auto_now_add=True)

class adminlogin(models.Model):
    pass
