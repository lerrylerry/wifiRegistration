from os import system
from django.db import models

# Create your models here.
class Faculty(models.Model):
    names = models.CharField(max_length=50, verbose_name='Name')
    department = models.CharField(max_length=50, verbose_name='Department')
    designation = models.CharField(max_length=50, verbose_name='Designation')
    macadd = models.CharField(max_length=14, verbose_name='Mac Address')
    Device = [
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    system = models.CharField(max_length=15, choices=Device, verbose_name='Device')
    others = models.CharField(max_length=15, null=True, blank=True, verbose_name='Specify')
    email = models.EmailField(primary_key=True, max_length=50, unique=True, verbose_name='Email')
    phone = models.DecimalField(max_digits=11, decimal_places=0, unique=True, verbose_name='Phone No')
    facultys = models.CharField(max_length=10, verbose_name='Faculty Name')
    upload = models.ImageField(height_field=None, width_field=None, verbose_name='Signature')
    date = models.DateTimeField(auto_now_add=True)