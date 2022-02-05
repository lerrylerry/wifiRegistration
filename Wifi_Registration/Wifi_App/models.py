from tabnanny import check
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Faculty(models.Model):
    names = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    macadd = models.CharField(max_length=14)
    Device = [
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    system = models.CharField(max_length=15, choices=Device)
    others = models.CharField(max_length=15, null=True, blank=True, default="None")
    email = models.EmailField(primary_key=True, max_length=50, unique=True)
    phone = models.DecimalField(max_digits=11, decimal_places=0, unique=True, verbose_name='Phone No')
    checked = models.BooleanField()
    facultys = models.CharField(max_length=10)
    upload = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)

class Student(models.Model):
    names = models.CharField(max_length=50)
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

    course = models.CharField(max_length=50, choices=Course)
    Semester = [
                ('First Semester','First Semester'),
                ('Second Semester','Second Semester'),
                ('Others...','Others...')
    ]

    semester = models.CharField(max_length=20, choices=Semester)
    tupid = models.IntegerField(primary_key=True)
    ornum = models.IntegerField()
    phone = models.DecimalField(max_digits=11, decimal_places=0, unique=True)
    Device = [
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    system = models.CharField(max_length=15, choices=Device, default='')
    others = models.CharField(max_length=15, null=True, blank=True)
    macadd = models.CharField(max_length=14)
    email = models.EmailField(max_length=50, unique=True)
    residAdd = models.CharField(max_length=200)
    checked = models.BooleanField()

class adminlogin(models.Model):
    pass