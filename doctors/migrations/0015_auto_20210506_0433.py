# Generated by Django 3.1.5 on 2021-05-05 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0014_auto_20210506_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='MobileNumber',
            field=models.CharField(default='Not available', max_length=13),
        ),
    ]
