from django.test import TestCase
from .models import Clinic, Appointment, AppointmentReschedule, Review
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()
# TEST MODELS 

class ClinicTesting(TestCase):
    def setUp(self):
        self.docter = User.objects.create(username="abdelrahman", email="abdelrahman@gmail.com",
                                        password="password", role="docter")
        
        self.user = User.objects.create(username="abdo", email="abdo@gmail.com",
                                        password="password", role="user")
        
        self.clinic = Clinic.objects.create(name="clinic1", price=120, docter=self.docter,
                                       descrption="this is clinic1")
    
    # TEST CLINIC MODEL
    def test_clinic_model(self):
        clinic = Clinic.objects.create(name="clinic1", price=120, docter=self.docter,
                                       descrption="this is clinic1")
        self.assertEqual(clinic.name, "clinic1")
        self.assertEqual(clinic.price, 120)
        self.assertEqual(clinic.docter, self.docter)
        self.assertEqual(clinic.descrption, "this is clinic1")
    
    # TEST APPOINTMENT MODEL
    def test_appointment_model(self):
        appointment = Appointment.objects.create(user=self.user, clinic=self.clinic,
                                                    date=datetime(2023, 2, 24) , time=datetime.now().strftime('%H:%M:%S'))
        self.assertEqual(appointment.user, self.user)
        self.assertEqual(appointment.clinic, self.clinic)
        self.assertEqual(appointment.date, datetime(2023, 2, 24))
        self.assertEqual(appointment.time, datetime.now().strftime('%H:%M:%S'))
    
    # TEST REVIEW MODEL
    def test_review_model(self):
        review = Review.objects.create(owner= self.user, rate=5, 
                                        content="good clinic", clinic=self.clinic)
        
        self.assertEqual(review.owner, self.user)
        self.assertEqual(review.clinic, self.clinic)
        self.assertEqual(review.rate, 5)
        self.assertEqual(review.content, "good clinic")
        