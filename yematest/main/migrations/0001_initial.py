# Generated by Django 2.2 on 2020-10-13 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=254)),
                ('doctor_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=254)),
                ('patient_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Patient')),
            ],
        ),
    ]
