from django.db import models

# Create your models here.
class Faculty(models.Model):
    fullname = models.CharField(max_length=50, verbose_name='Name')
    dept = models.CharField(max_length=50, verbose_name='Department')
    design = models.CharField(max_length=50, verbose_name='Designation')
    mac = models.CharField(max_length=14, verbose_name='Mac Address')
    Device = [
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    device = models.CharField(max_length=15, choices=Device, verbose_name='Device')
    others = models.CharField(max_length=15, null=True, blank=True, verbose_name='Specify')
    email = models.EmailField(primary_key=True, max_length=50, unique=True, verbose_name='Email')
    phone = models.DecimalField(max_digits=11, decimal_places=0, unique=True, verbose_name='Phone No')
    facname = models.CharField(max_length=10, verbose_name='Faculty Name')
    upload = models.ImageField(height_field=None, width_field=None, verbose_name='Signature')
    date = models.DateTimeField(auto_now_add=True)