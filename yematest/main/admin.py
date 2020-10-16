from django.contrib import admin
from .models import Doctor, Patient, Appointment
from django.core.mail import send_mail

# Hello devs from YEMA!!
# in order to get this demo running you will need to update the 3rd 
# params from the send_mail function
# put your own gmail account in there and also at the ending of
# settings.py :)

# Register your models here.
YOUR_EMAIL = "" # edit this variables as well, use the same email you added in settings.py

models = [Doctor, Patient]

class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    fields = ["doctor", "patient", "date"]

    actions = ["send_email"]

    def send_email(self, request, queryset):
        queryset.update()

        print("##########")
        for appointment in queryset:

            send_mail(
                "Cita confirmada!",
                "Cita agendada a las " + appointment.hour + " del dia " 
                + appointment.date + " Comentarios adicionales: " + appointment.comments ,
                YOUR_EMAIL,
                [
                    Doctor.objects.get(id=appointment.doctor.id).doctor_email, 
                    Patient.objects.get(id=appointment.patient.id).patient_email
                ]
            )

admin.site.register(models)
admin.site.register(Appointment, AppointmentAdmin)