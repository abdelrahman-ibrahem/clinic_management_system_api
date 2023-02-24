from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (AppointmentSerializer, ClinicSerializer,
                            ReviewSerializer, ApponintmentReschudleSerializer)
from .models import Appointment, Clinic, Review, AppointmentReschedule
from django_filters.rest_framework import DjangoFilterBackend

class ListCreateClinics(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class RetrevieDeleteAppointment(generics.RetrieveDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class RetrevieUpdateAppointment(generics.RetrieveUpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAdminUser]

class ViewAllAppointments(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'date', 'status']

class CreateAppointment(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ListCreateReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RetrevieDeleteUpdateReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ListReschudelAppointments(generics.ListAPIView):
    queryset = AppointmentReschedule.objects.all()
    serializer_class = ApponintmentReschudleSerializer
    permission_classes = [permissions.IsAdminUser]


class ReschudelAppointment(generics.CreateAPIView):
    queryset = AppointmentReschedule.objects.all()
    serializer_class = ApponintmentReschudleSerializer
    permission_classes = [permissions.IsAuthenticated]

class UpdateReschudelAppointment(generics.RetrieveUpdateAPIView):
    queryset = AppointmentReschedule.objects.all()
    serializer_class = ApponintmentReschudleSerializer
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        try:
            data = request.data
            appointment_reschudle = AppointmentReschedule.objects.get(id=kwargs["pk"])
            appointment = Appointment.objects.get(id=appointment_reschudle.appointment.id)
            appointment.status = data["status"]
            if data["status"] == 'approve':
                appointment.date = data["date"]
                appointment.time = data["time"]
            
            appointment.save()
            return Response({
                "message": "Appointment status is updated"
            })
        except:
            return Response({
                "Message": "Something is wrong"
            }, status=status.HTTP_400_BAD_REQUEST)