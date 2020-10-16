from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

class TestDoctor(APITestCase):
    def test_get(self):
        res = self.client.get("/doctor/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create(self):
        data = {
            "doctor_name": "Juan Pablo Ascencio",
            "doctor_email": "juanpa@yema.mx"
        }
        res = self.client.post("/doctor/", data)

class TestPatient(APITestCase):
    def test_get(self):
        res = self.client.get("/patient/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create(self):
        data = {
            "patient_name": "Juan Pablo Ascencio",
            "patient_email": "juanpa@test.mx"
        }
        res = self.client.post("/patient/", data)

class TestAppointment(APITestCase):
    def test_get(self):
        res = self.client.get("/appointment/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create(self):
        data = {
            "doctor": "1", 
            "patient": "1", 
            "comments": "We love them testssss", 
            "date": "2020-10-28", 
            "hour": "01:17"
        }
        res = self.client.post("/appointment/", data)