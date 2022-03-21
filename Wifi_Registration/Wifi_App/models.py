from django.db import models

# Create your models here.

class Faculty(models.Model):
    fnames = models.CharField(max_length=50, verbose_name="Name")
    fdepartment = models.CharField(max_length=50, verbose_name="Department")
    fdesignation = models.CharField(max_length=50, verbose_name="Designation")
    fmacadd = models.CharField(max_length=17, verbose_name="MAC Address")
    Device = [
                ('' , 'Choose device'),
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    fsystem = models.CharField(max_length=15, choices=Device, verbose_name="Device")
    fothers = models.CharField(max_length=15, null=True, blank=True, default="", verbose_name="Others")
    femail = models.EmailField(max_length=50, unique=True, primary_key=True, verbose_name="Email")
    fphone = models.DecimalField(max_digits=12, decimal_places=0, unique=True, verbose_name="Phone No.")
    fchecked = models.BooleanField(default=False)
    ffacultys = models.CharField(max_length=10, verbose_name="Faculty Name")
    fupload = models.ImageField(verbose_name="Signature", upload_to='uploads/', blank=False, null=False)
    #fdate = models.DateTimeField(auto_now_add=True)
    ftype = models.CharField(max_length=10)
    fmark = models.CharField(max_length=10)

class Student(models.Model):
    snames = models.CharField(max_length=50, verbose_name="Name")
    #first column: database // second column: forms
    Course = [
                ('' , 'Choose course'),
                ('BSCE','BACHELOR OF SCIENCE IN CIVIL ENGINEERING'),
                ('BSEE','BACHELOR OF SCIENCE IN ELECTRICAL ENGINEERING'),
                ('BSME','BACHELOR OF SCIENCE IN MECHANICAL ENGINEERING'),
                ('BET-ET','BET-ELECTRICAL TECHNOLOGY'),
                ('BET-ESET','BET-INDUSTRIAL AUTOMATION TECHNOLOGY'),
                ('BET-COET','BET-COMPUTER ENGINEERING TECHNOLOGY'),
                ('BET-CT','BET-CIVIL TECHNOLOGY'),
                ('BET-AT','BET-AUTOMOTIVE TECHNOLOGY'),
                ('BET-MT','BET-MECHANICAL ENGINEERING TECHNOLOGY'),
                ('BET-PPT','BET-POWER PLANT TECHNOLOGY'),
                ('BET-ICT','BSIE-INFORMATION COMPUTER TECHNOLOGY'),
                ('BET-HE','BSIE-HOME ECONOMICS'),
                ('BET-AU','BTTE-AUTOMOTIVE'),
                ('BET-EI','BTTE-ELECTRICAL'),
                ('BET-E','BTTE-ELECTRONICS'),
                ('BET-HVACT','BTTE-AIR CONDITIONING'),
                ('BET-CP','BTTE-COMPUTER PROGRAMMING')
    ]

    scourse = models.CharField(max_length=50, choices=Course, verbose_name="Course")
    Semester = [
                ('' , 'Choose Semester'),
                ('First Semester','1st Semmester'),
                ('Second Semester','2nd Semester'),
                ('Others...','Others...')
    ]

    ssemester = models.CharField(max_length=20, choices=Semester, verbose_name="Semester")
    stupid = models.CharField(max_length=12, verbose_name="Student No")
    sornum = models.DecimalField(max_digits=8, decimal_places=0,verbose_name="O.R #")
    sphone = models.DecimalField(max_digits=12, decimal_places=0,unique=True, verbose_name="Phone")
    Device = [
                ('' , 'Choose device'),
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    ssystem = models.CharField(max_length=15, choices=Device, verbose_name="Device")
    sothers = models.CharField(max_length=15, null=True, blank=True, verbose_name="Others")
    smacadd = models.CharField(max_length=17, verbose_name="MAC Address")
    semail = models.EmailField(max_length=50, unique=True, primary_key=True, verbose_name="Email")
    sresidAdd = models.CharField(max_length=200, verbose_name="Residence Address")
    supload = models.ImageField(verbose_name="Signature", upload_to="uploads2/")
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
    username = models.CharField(max_length=50, default="admin")
    adminpw = models.CharField(max_length=20, default=1234)
