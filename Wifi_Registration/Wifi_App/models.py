from django.db import models

# Create your models here.

class Faculty(models.Model):
    names = models.CharField(max_length=50, unique=True, verbose_name="Name")
    department = models.CharField(max_length=50, verbose_name="Department")
    designation = models.CharField(max_length=50, verbose_name="Designation")
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
    email = models.EmailField(max_length=50, unique=True, primary_key=True, verbose_name="Email")
    macadd = models.CharField(max_length=17, unique=True, verbose_name="MAC Address")
    phoneNum = models.DecimalField(max_digits=15, decimal_places=0, unique=True, verbose_name="Phone No.")
    facultyName = models.CharField(max_length=10, verbose_name="Faculty Name")
    signature = models.ImageField(verbose_name="Signature", upload_to='uploads/', blank=False, null=False)
    agreement = models.BooleanField(default=False)  
    decision = models.CharField(max_length=10)
    dateCreated = models.DateTimeField(auto_now_add=True)
    userType = models.CharField(max_length=10)

    def __str__(self):
        return self.names + '-->' + self.email

class Student(models.Model):
    names = models.CharField(max_length=50, unique=True, verbose_name="Name")
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
    email = models.EmailField(max_length=50, unique=True, primary_key=True, verbose_name="Email")
    macadd = models.CharField(max_length=17, unique=True, verbose_name="MAC Address")
    phoneNum = models.DecimalField(max_digits=15, decimal_places=0, unique=True, verbose_name="Phone No.")
    semester = models.CharField(max_length=20, choices=Semester, verbose_name="Semester")
    tupid = models.CharField(max_length=12, verbose_name="Student No")
    orNum = models.DecimalField(max_digits=8, decimal_places=0, unique=True, verbose_name="O.R #")
    residAdd = models.CharField(max_length=200, verbose_name="Residence Address")
    signature = models.ImageField(verbose_name="Signature", upload_to='uploads/', blank=False, null=False)
    agreement = models.BooleanField(default=False)  
    userType = models.CharField(max_length=10)
    decision = models.CharField(max_length=10)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.names + '-->' + self.email
    
class History(models.Model):  
    names = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    macadd = models.CharField(max_length=17)
    userType = models.CharField(max_length=10)
    decision = models.CharField(max_length=10)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateEvaluated = models.DateTimeField(blank=True,null=True)
    #data_of_Faculty = models.ManyToManyField(Faculty)
    #data_of_Student = models.ManyToManyField(Student)