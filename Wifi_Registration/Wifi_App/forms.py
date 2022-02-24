import re
from django import forms
from Wifi_App.models import Faculty, Student
from django.core.exceptions import ValidationError

class facultyform(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['fnames','fdepartment','fdesignation','fmacadd','fsystem','fothers','femail','fphone','ffacultys','fupload']

    def clean_fnames(self):
        pattern_with_text = "\\d+"
        data = self.cleaned_data['fnames'] 

        if len(data) < 8:
            raise ValidationError("Name must be 8 characters long")
        if re.findall(pattern_with_text,data):
            raise ValidationError("Name must contain A-Z/a-z")
        return data

    def clean_fdepartment(self):
        pattern_with_text = "\\d+"
        data2 = self.cleaned_data['fdepartment']
        if len(data2) < 8:
            raise ValidationError("Department must be 8 characters long")
        if re.findall(pattern_with_text,data2):
            raise ValidationError("Department must contain A-Z/a-z")
        return data2

    def clean_fdesignation(self):
        pattern_with_text = "\\d+"
        data3 = self.cleaned_data['fdesignation']
        if len(data3) < 8:
            raise ValidationError("Designation must be 8 characters long")
        if re.findall(pattern_with_text,data3):
            raise ValidationError("Designation must contain A-Z/a-z")
        return data3

    def clean_fmacadd(self):
        pattern_with_mac = "^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"
        data4 = self.cleaned_data['fmacadd']
        if not re.search(pattern_with_mac,data4):
            raise ValidationError("Please use valid mac address")
        return data4

    def clean_femail(self):
        pattern_with_email = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
        data5 = self.cleaned_data['femail']
        if not re.search(pattern_with_email,data5):
            raise ValidationError("Please use valid email")
        return data5
    
    def clean_fphone(self):
        pattern_with_phone = "[6][3][9][0-9]{9}"
        data6 = self.cleaned_data['fphone']
        if len(str(data6)) <= 11:
            raise ValidationError("Insufficient numbers")
        if not re.match(pattern_with_phone,str(data6)):
            raise ValidationError("Please enter PH numbers")
        return data6

    def clean_ffacultys(self):
        pattern_with_text = "\\d+"
        data8 = self.cleaned_data['ffacultys']
        if len(data8) < 8:
            raise ValidationError("Faculty Name must be 8 characters long")
        if re.findall(pattern_with_text,data8):
            raise ValidationError("Faculty Name must contain A-Z/a-z")
        return data8
'''
    def clean_fupload(self):
        pattern_with_upload = "(\.jpg|\.jpeg|\.png)$"
        data9 = self.cleaned_data['fupload']
        if not re.match(pattern_with_upload,data9):
            raise ValidationError("Please submit an image file")
        return data9        
'''

class studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['snames','scourse','ssemester','stupid','sornum','sphone','ssystem','sothers','smacadd','semail','sresidAdd','supload']
        
    def clean_snames(self):
        pattern_with_text = "\\d+"
        data = self.cleaned_data['snames'] 

        if len(data) < 8:
            raise ValidationError("Name must be 8 characters long")
        if re.findall(pattern_with_text,data):
            raise ValidationError("Name must contain A-Z/a-z")
        return data
    
    def clean_stupid(self):
        pattern_with_tupid = "[T][U][P][C]-[0-9]{2}-[0-9]{4}"
        data4 = self.cleaned_data['stupid'] 

        if not re.search(pattern_with_tupid,data4):
            raise ValidationError("Please enter valid TUP ID")
        return data4

    def clean_sornum(self):
        #pattern_with_or = ""
        data5 = self.cleaned_data['sornum'] 

        if len(str(data5)) < 6:
            raise ValidationError("OR number must be 6 digits long")
        return data5

    def clean_sphone(self):
        pattern_with_phone = "[6][3][9][0-9]{9}"
        data6 = self.cleaned_data['sphone'] 

        if len(str(data6)) <= 11:
            raise ValidationError("Insufficient numbers")
        if not re.search(pattern_with_phone,str(data6)):
            raise ValidationError("Please enter valid PH number")
        return data6

    def clean_smacadd(self):
        pattern_with_mac = "^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"
        data9 = self.cleaned_data['smacadd'] 

        if not re.search(pattern_with_mac,data9):
            raise ValidationError("Please use valid mac address")
        return data9

    def clean_semail(self):
        pattern_with_email = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
        data10 = self.cleaned_data['semail']
        if not re.search(pattern_with_email,data10):
            raise ValidationError("Please use valid email")
        return data10

    def clean_sresidAdd(self):
        data11 = self.cleaned_data['snames'] 

        if len(data11) < 15:
            raise ValidationError("Name must be 15 characters long")
        return data11

'''
    def clean_supload(self):
        pattern_with_upload = "(\.jpg|\.jpeg|\.png)$"
        data12 = self.cleaned_data['supload']
        if not re.match(pattern_with_upload,data9):
            raise ValidationError("Please submit an image file")
        return data12        
'''