# Generated by Django 4.0.3 on 2022-03-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wifi_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='fchecked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='fupload',
            field=models.ImageField(upload_to='uploads/', verbose_name='Signature'),
        ),
    ]
