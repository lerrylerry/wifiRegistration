from pyexpat import model
from re import T
from select import select
from statistics import mode
from django.db import models

# Create your models here.
def faculty(Model):
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