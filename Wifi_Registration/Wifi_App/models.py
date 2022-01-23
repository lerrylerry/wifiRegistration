from pyexpat import model
from re import T
from select import select
from statistics import mode
from django.db import models

# Create your models here.

def facultyDB(Model):
    fullname = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    design = models.CharField(max_length=50)
    mac = models.CharField(max_length=14)
    device = [
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    device = models.CharField(max_length=15, choices=device, default='')
    others = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(primary_key=True, max_length=50, unique=True)
    phone = models.DecimalField(max_digits=11, decimal_places=0, unique=True)
    check = models.BooleanField()
    facname = models.CharField(max_length=10)
    upload = models.ImageField(height_field=None, width_field=None)
    date = models.DateField()

def studentDB(Model):
    fullname = models.CharField(max_length=50)
    course = [
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

    course = models.CharField(max_length=50, choices=course)
    semes = [
                ('First Semester','First Semester'),
                ('Second Semester','Second Semester'),
                ('Others...','Others...')
    ]

    semes = models.CharField(max_length=20, choices=semes)
    tupid = models.IntegerField(primary_key=True, unique=True)
    ornum = models.IntegerField()
    phone = models.DecimalField(max_digits=11, decimal_places=0, unique=True)
    device = [
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    device = models.CharField(max_length=15, choices=device, default='')
    others = models.CharField(max_length=15, null=True, blank=True)
    mac = models.CharField(max_length=14)
    email = models.EmailField(max_length=50, unique=True)
    residAdd = models.CharField(max_length=200)
    check = models.BooleanField()
    uname = models.CharField(max_length=10)
    upass = models.CharField(max_length=10)


    def login(Model):
        pass