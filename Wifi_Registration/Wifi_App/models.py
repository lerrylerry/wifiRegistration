from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.db.models.signals import post_save
#from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractUser):
    userType = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=50, unique=True, verbose_name="Email", primary_key=True)
    
    def __str__(self):
        return self.username + ' ' + self.email

class Student(models.Model):    
    tupid = models.CharField(max_length=50, primary_key=True, verbose_name="Student No.")
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
    status = models.CharField(max_length=10, default='none')
    dateCreated = models.DateTimeField(blank=True,null=True)
    emails = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.tupid

    class Meta:
        ordering = ['-dateCreated']

class Faculty(models.Model):
    department = models.CharField(max_length=50, verbose_name="Department")
    designation = models.CharField(max_length=50, verbose_name="Designation")
    facultyName = models.CharField(max_length=50, verbose_name="Faculty Name")
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
    status = models.CharField(max_length=10, default='none')
    dateCreated = models.DateTimeField(blank=True,null=True)
    emails = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.emails

    class Meta:
        ordering = ['-dateCreated']

class History(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT,null=True, related_name='faculties')
    student = models.ForeignKey(Student, on_delete=models.PROTECT,null=True, related_name='students')
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateEvaluated = models.DateTimeField(blank=True,null=True)

    class Meta:
        ordering = ['-dateCreated']

'''
@receiver(post_save, sender=CustomUser)
def create_faculty_link(sender, instance, created, **kwargs):
    if created:
        Faculty.objects.create(emails=instance)

@receiver(post_save, sender=CustomUser)
def save_faculty_link(sender, instance, **kwargs):
    instance.email.save()
'''