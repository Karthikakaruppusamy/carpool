# Generated by Django 4.1.7 on 2023-05-09 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='cust',
        ),
    ]
