# Generated by Django 4.0.3 on 2022-04-22 14:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userType', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('department', models.CharField(max_length=50, verbose_name='Department')),
                ('designation', models.CharField(max_length=50, verbose_name='Designation')),
                ('facultyName', models.CharField(max_length=50, verbose_name='Faculty Name')),
                ('names', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('device', models.CharField(choices=[('', 'Choose device'), ('Smartphone', 'Smartphone'), ('Laptop', 'Laptop'), ('Tablet', 'Tablet'), ('PC', 'PC'), ('Desktop', 'Desktop')], max_length=15, verbose_name='Device')),
                ('otherDevice', models.CharField(blank=True, max_length=15, null=True, verbose_name='Others')),
                ('macadd', models.CharField(max_length=17, unique=True, verbose_name='MAC Address')),
                ('phoneNum', models.BigIntegerField(unique=True, verbose_name='Phone No.')),
                ('signature', models.ImageField(upload_to='uploads/', verbose_name='Signature')),
                ('agreement', models.BooleanField(default=False)),
                ('status', models.CharField(default='none', max_length=10)),
                ('dateCreated', models.DateTimeField(blank=True, null=True)),
                ('emails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-dateCreated'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('tupid', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Student No.')),
                ('course', models.CharField(choices=[('', 'Choose course'), ('BSCE', 'BACHELOR OF SCIENCE IN CIVIL ENGINEERING'), ('BSEE', 'BACHELOR OF SCIENCE IN ELECTRICAL ENGINEERING'), ('BSME', 'BACHELOR OF SCIENCE IN MECHANICAL ENGINEERING'), ('BET-ET', 'BET-ELECTRICAL TECHNOLOGY'), ('BET-ESET', 'BET-INDUSTRIAL AUTOMATION TECHNOLOGY'), ('BET-COET', 'BET-COMPUTER ENGINEERING TECHNOLOGY'), ('BET-CT', 'BET-CIVIL TECHNOLOGY'), ('BET-AT', 'BET-AUTOMOTIVE TECHNOLOGY'), ('BET-MT', 'BET-MECHANICAL ENGINEERING TECHNOLOGY'), ('BET-PPT', 'BET-POWER PLANT TECHNOLOGY'), ('BET-ICT', 'BSIE-INFORMATION COMPUTER TECHNOLOGY'), ('BET-HE', 'BSIE-HOME ECONOMICS'), ('BET-AU', 'BTTE-AUTOMOTIVE'), ('BET-EI', 'BTTE-ELECTRICAL'), ('BET-E', 'BTTE-ELECTRONICS'), ('BET-HVACT', 'BTTE-AIR CONDITIONING'), ('BET-CP', 'BTTE-COMPUTER PROGRAMMING')], max_length=50, verbose_name='Course')),
                ('semester', models.CharField(choices=[('', 'Choose Semester'), ('First Semester', '1st Semmester'), ('Second Semester', '2nd Semester'), ('Others...', 'Others...')], max_length=20, verbose_name='Semester')),
                ('orNum', models.IntegerField(unique=True, verbose_name='O.R #')),
                ('residAdd', models.CharField(max_length=200, verbose_name='Residence Address')),
                ('names', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('device', models.CharField(choices=[('', 'Choose device'), ('Smartphone', 'Smartphone'), ('Laptop', 'Laptop'), ('Tablet', 'Tablet'), ('PC', 'PC'), ('Desktop', 'Desktop')], max_length=15, verbose_name='Device')),
                ('otherDevice', models.CharField(blank=True, max_length=15, null=True, verbose_name='Others')),
                ('macadd', models.CharField(max_length=17, unique=True, verbose_name='MAC Address')),
                ('phoneNum', models.BigIntegerField(unique=True, verbose_name='Phone No.')),
                ('signature', models.ImageField(upload_to='uploads/', verbose_name='Signature')),
                ('agreement', models.BooleanField(default=False)),
                ('status', models.CharField(default='none', max_length=10)),
                ('dateCreated', models.DateTimeField(blank=True, null=True)),
                ('emails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-dateCreated'],
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateEvaluated', models.DateTimeField(blank=True, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='students', to='Wifi_App.student')),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='faculties', to='Wifi_App.faculty')),
            ],
            options={
                'ordering': ['-dateCreated'],
            },
        ),
    ]
