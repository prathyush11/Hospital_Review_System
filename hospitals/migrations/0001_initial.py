# Generated by Django 3.1.5 on 2021-04-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HospitalName', models.CharField(max_length=150)),
                ('HospitalRegisterationNumber', models.CharField(max_length=150)),
                ('HospitalLicense', models.FileField(upload_to='HospitalDocuments/')),
                ('HospitalPhoto', models.FileField(blank=True, upload_to='HospitalPhotos/')),
                ('Email', models.CharField(max_length=150)),
                ('Username', models.CharField(max_length=150)),
                ('HospitalEshtablishDate', models.DateField()),
                ('HospitalDescription', models.TextField(blank=True, max_length=250)),
                ('Town', models.CharField(max_length=150)),
                ('City', models.CharField(max_length=150)),
                ('Pincode', models.CharField(max_length=150)),
                ('State', models.IntegerField(choices=[(1, 'Andhra Pradesh'), (2, 'Arunachal Pradesh'), (3, 'Assam'), (4, 'Bihar'), (5, 'Chhattisgarh'), (6, 'Goa'), (7, 'Gujarat'), (8, 'Harayana'), (9, 'Himachal Pradesh'), (10, 'Jharkhand'), (11, 'Karnataka'), (12, 'Kerala'), (13, 'Madhya Pradesh'), (14, 'Maharashtra'), (15, 'Manipur'), (16, 'Meghalaya'), (17, 'Mizoram'), (18, 'Nagaland'), (19, 'Odisha'), (20, 'Punjab'), (21, 'Rajasthan'), (22, 'Sikkim'), (23, 'Tamil Nadu'), (24, 'Telangana'), (25, 'Tripura'), (26, 'Uttarakhand'), (27, 'Uttar Pradesh'), (28, 'West Bengal')], default=1)),
                ('ChiefMedicalOfficer', models.CharField(max_length=150)),
                ('ChiefMedicalOfficerCertificate', models.FileField(upload_to='ChiefDoctorDocuments/')),
                ('ChiefMedicalOfficerPhoto', models.FileField(blank=True, upload_to='ChiefDoctorPhotos/')),
                ('CheifMedicalOfficerDescription', models.CharField(blank=True, max_length=250)),
                ('PhoneNumber', models.CharField(max_length=20)),
                ('Achievements1', models.CharField(blank=True, max_length=50)),
                ('Achievements2', models.CharField(blank=True, max_length=50)),
                ('Achievements3', models.CharField(blank=True, max_length=50)),
                ('Achievements4', models.CharField(blank=True, max_length=50)),
                ('Achievements5', models.CharField(blank=True, max_length=50)),
                ('Achievements6', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
