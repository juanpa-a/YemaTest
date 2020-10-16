from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=254)
    patient_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.patient_name

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=254)
    doctor_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.doctor_name


class Appointment(models.Model):
    doctor = models.ForeignKey(
        "Doctor", 
        on_delete=models.DO_NOTHING,
    )
    comments = models.TextField()
    patient = models.ForeignKey(
        "Patient", 
        on_delete=models.DO_NOTHING,
    )
    date = models.DateField()
    hour = models.TimeField(
        auto_now=False, 
        auto_now_add=False,
    )