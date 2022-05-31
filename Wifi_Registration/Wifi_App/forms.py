import re
from django import forms
from .models import Contact, CustomUser, Student, Faculty, Time
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def clean_phoneNum(self):
        pattern_with_phone = "[0][9][0-9]{9}"
        data6 = self.cleaned_data['phoneNum'] 
        zero = '0' + str(data6)
        if len(str(zero)) < 11:
            raise ValidationError("Insufficient numbers")
        if len(str(zero)) > 11:
            raise ValidationError("Limit exceeds")
        if not re.search(pattern_with_phone,str(zero)):
            raise ValidationError("Please enter valid PH number")
        return zero

class TimeForm(forms.ModelForm):
    start = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    end = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Time
        fields = "__all__"

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

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

class FacultyForm(forms.ModelForm):
    names = forms.CharField(error_messages={'required': "Name is required.",'unique':"A user with this name already exists"})
    department = forms.CharField(error_messages={'required': "Department is required."})
    designation = forms.CharField(error_messages={'required': "Designation is required."})
    macadd = forms.CharField(error_messages={'required': "Mac Address is required."})
    device = forms.ChoiceField(error_messages={'required': "Device is required."},choices=Device)
    agreement = forms.BooleanField(error_messages={'required': "required."})
    email = forms.EmailField(error_messages={'required': "Email is required."})
    phoneNum = forms.IntegerField(error_messages={'required': "Phone No. is required."})
    facultyName = forms.CharField(error_messages={'required': "Faculty Name is required."})
    signature = forms.ImageField(error_messages={'required': "Signature is required."})
    class Meta:
        model = Faculty
        fields = ['names','department','designation','macadd','device', 'email','otherDevice','agreement','phoneNum','facultyName','signature']

    def clean_agreement(self):
        dat = self.cleaned_data['agreement']
        if not dat:
            raise forms.ValidationError('This field is required')
        return dat

    def clean_names(self):
        pattern_with_text = "\\d+"
        data = self.cleaned_data['names'] 

        if len(data) < 8:
            raise ValidationError("Name must be 8 characters long")
        if re.findall(pattern_with_text,data):
            raise ValidationError("Name must contain A-Z/a-z")
        return data

    def clean_department(self):
        pattern_with_text = "\\d+"
        data2 = self.cleaned_data['department']
        if len(data2) < 8:
            raise ValidationError("Department must be 8 characters long")
        if re.findall(pattern_with_text,data2):
            raise ValidationError("Department must contain A-Z/a-z")
        return data2

    def clean_designation(self):
        pattern_with_text = "\\d+"
        data3 = self.cleaned_data['designation']
        if len(data3) < 8:
            raise ValidationError("Designation must be 8 characters long")
        if re.findall(pattern_with_text,data3):
            raise ValidationError("Designation must contain A-Z/a-z")
        return data3

    def clean_macadd(self):
        pattern_with_mac = "^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"
        data4 = self.cleaned_data['macadd']
        if not re.search(pattern_with_mac,data4):
            raise ValidationError("Please use valid mac address")
        return data4
    
    def clean_phoneNum(self):
        pattern_with_phone = "[0][9][0-9]{9}"
        data6 = self.cleaned_data['phoneNum']
        zero = '0' + str(data6)
        print(zero)
        if len(str(zero)) < 11:
            raise ValidationError("Insufficient numbers")
        if len(str(zero)) > 11:
            raise ValidationError("Limit exceeds")
        if not re.match(pattern_with_phone,str(zero)):
            raise ValidationError("Please enter PH numbers")
        return zero

    def clean_facultyName(self):
        pattern_with_text = "\\d+"
        data8 = self.cleaned_data['facultyName']
        if len(data8) < 8:
            raise ValidationError("Faculty Name must be 8 characters long")
        if re.findall(pattern_with_text,data8):
            raise ValidationError("Faculty Name must contain A-Z/a-z")
        return data8

class StudentForm(forms.ModelForm):
    names = forms.CharField(error_messages={'required': "Name is required."})
    course = forms.ChoiceField(error_messages={'required': "Course is required."},choices=Course)
    semester = forms.ChoiceField(error_messages={'required': "Semester is required."},choices=Semester)
    macadd = forms.CharField(error_messages={'required': "Mac Address is required."})
    device = forms.ChoiceField(error_messages={'required': "Device is required."},choices=Device)
    agreement = forms.BooleanField(error_messages={'required': "required."})
    email = forms.EmailField(error_messages={'required': "Email is required."})
    phoneNum = forms.IntegerField(error_messages={'required': "Phone No. is required."})
    tupid = forms.CharField(error_messages={'required': "TUPC-ID is required."})
    orNum= forms.IntegerField(error_messages={'required': "OR No. is required."})
    residAdd = forms.CharField(error_messages={'required': "Residence Address is required."})
    signature = forms.ImageField(error_messages={'required': "Signature is required."})
    class Meta:
        model = Student
        fields = ['names','course','semester','phoneNum','device','orNum', 'agreement', 'email' ,'otherDevice','tupid','macadd','residAdd','signature']
        

    def clean_agreement(self):
        dat = self.cleaned_data['agreement']
        if not dat:
            raise forms.ValidationError('This field is required')
        return dat

    def clean_names(self):
        pattern_with_text = "\\d+"
        data = self.cleaned_data['names'] 

        if len(data) < 8:
            raise ValidationError("Name must be 8 characters long")
        if re.findall(pattern_with_text,data):
            raise ValidationError("Name must contain A-Z/a-z")
        return data
    
    def clean_tupid(self):
        pattern_with_tupid = "[T][U][P][C]-[0-9]{2}-[0-9]{4}"
        data4 = self.cleaned_data['tupid'] 

        if not re.search(pattern_with_tupid,data4):
            raise ValidationError("Please enter valid TUP ID")
        return data4

    def clean_orNum(self):
        #pattern_with_or = ""
        data5 = self.cleaned_data['orNum'] 

        if len(str(data5)) < 6:
            raise ValidationError("OR number must be 6 digits long")
        if len(str(data5)) > 10:
            raise ValidationError("Limit exceeds")
        return data5

    def clean_phoneNum(self):
        pattern_with_phone = "[0][9][0-9]{9}"
        data6 = self.cleaned_data['phoneNum'] 
        zero = '0' + str(data6)
        if len(str(zero)) < 11:
            raise ValidationError("Insufficient numbers")
        if len(str(zero)) > 11:
            raise ValidationError("Limit exceeds")
        if not re.search(pattern_with_phone,str(zero)):
            raise ValidationError("Please enter valid PH number")
        return zero

    def clean_macadd(self):
        pattern_with_mac = "^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"
        data9 = self.cleaned_data['macadd']

        if not re.search(pattern_with_mac,data9):
            raise ValidationError("Please use valid mac address")
        return data9

    def clean_email(self):
        pattern_with_email = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
        data10 = self.cleaned_data['email']
        if not re.search(pattern_with_email,data10):
            raise ValidationError("Please use valid email")
        return data10

    def clean_residAdd(self):
        data11 = self.cleaned_data['residAdd'] 
        if len(data11) < 15:
            raise ValidationError("Address must be 15 characters long")
        return data11