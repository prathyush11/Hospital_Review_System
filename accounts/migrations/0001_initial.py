# Generated by Django 3.1.5 on 2021-04-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=150)),
                ('LastName', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=150)),
                ('DateOfBirth', models.CharField(max_length=150)),
                ('MobileNumber', models.CharField(max_length=10)),
            ],
        ),
    ]
