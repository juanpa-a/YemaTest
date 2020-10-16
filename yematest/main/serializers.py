from rest_framework import serializers
from .models import Doctor, Patient, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("id", "doctor_name", "doctor_email")

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("id", "patient_name", "patient_email")

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("id", "doctor", "patient", "comments", "date", "hour")