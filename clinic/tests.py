from django.test import TestCase
from .models import Clinic, Appointment, AppointmentReschedule, Review
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()
# TEST MODELS 

class ClinicTesting(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="abdelrahman", email="abdelrahman@gmail.com",
                                        password="password", role="docter")
        
        clinic = Clinic.objects.create(name="clinic1", price=120, docter=self.user,
                                       descrption="this is clinic1")
    
    # TEST CLINIC MODEL
    def test_clinic_model(self):
        clinic = Clinic.objects.create(name="clinic1", price=120, docter=self.user,
                                       descrption="this is clinic1")
        self.assertEqual(clinic.name, "clinic1")
        self.assertEqual(clinic.price, 120)
        self.assertEqual(clinic.docter, self.user)
        self.assertEqual(clinic.descrption, "this is clinic1")
    
    # TEST APPOINTMENT MODEL
    def test_appointment_model(self):
        pass
    
    # TEST REVIEW MODEL
    def test_review_model(self):
        pass