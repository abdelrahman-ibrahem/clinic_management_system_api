from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import AppointmentSerializer, ClinicSerializer, ReviewSerializer
from .models import Appointment, Clinic, Review

class ListCreateClinics(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class RetrevieDeleteAppointment(generics.RetrieveDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ViewAllAppointments(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class CreateAppointment(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ListCreateReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RetrevieDeleteUpdateReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
