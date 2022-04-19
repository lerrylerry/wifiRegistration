from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    tupid = models.CharField(max_length=12, verbose_name="Student No", unique=True, null=True)
    email = models.EmailField(max_length=50, unique=True, verbose_name="Email", primary_key=True)
    userType = models.CharField(max_length=10, blank=True)
    decision = models.CharField(max_length=10, blank=True)

class CommonInfo(models.Model):
    names = models.CharField(max_length=50, verbose_name="Name",unique=True)
    Device = [
                ('' , 'Choose device'),
                ('Smartphone' , 'Smartphone'),
                ('Laptop' , 'Laptop'),
                ('Tablet' , 'Tablet'),
                ('PC' , 'PC'),
                ('Desktop' , 'Desktop')
            ]

    device = models.CharField(max_length=15, choices=Device, verbose_name="Device")
    otherDevice = models.CharField(max_length=15, null=True, blank=True, verbose_name="Others")
    macadd = models.CharField(max_length=17, verbose_name="MAC Address", unique=True)
    phoneNum = models.BigIntegerField(verbose_name="Phone No.", unique=True)
    signature = models.ImageField(verbose_name="Signature", upload_to='uploads/')
    agreement = models.BooleanField(default=False)  
    userType = models.CharField(max_length=10)
    decision = models.CharField(max_length=10)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user

    class Meta:
        abstract = True

class Student(CommonInfo):
    Course = [#first column: database // second column: forms
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

    course = models.CharField(max_length=50, choices=Course, verbose_name="Course")
    Semester = [
                ('' , 'Choose Semester'),
                ('First Semester','1st Semmester'),
                ('Second Semester','2nd Semester'),
                ('Others...','Others...')
    ]
    semester = models.CharField(max_length=20, choices=Semester, verbose_name="Semester")
    orNum = models.IntegerField(verbose_name="O.R #",unique=True)
    residAdd = models.CharField(max_length=200, verbose_name="Residence Address")

class Faculty(CommonInfo):
    department = models.CharField(max_length=50, verbose_name="Department")
    designation = models.CharField(max_length=50, verbose_name="Designation")
    facultyName = models.CharField(max_length=10, verbose_name="Faculty Name")

class History(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, related_name='students', null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, related_name='faculties', null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateEvaluated = models.DateTimeField(blank=True,null=True)