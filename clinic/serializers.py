from rest_framework import serializers
from .models import (Appointment, Clinic, Review,
                      AppointmentReschedule, APPOINTMENTS_STATUS)
from users.serializers import UserSerializer

# CREATE MODELS SERIALIZERS

class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

class ClinicSerializer(serializers.ModelSerializer):
    docter = CustomUserSerializer(read_only=True)

    class Meta:
        model = Clinic
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    clinic = ClinicSerializer(read_only=True)
    class Meta:
        model = Appointment
        fields = [
            'id',
            'user',
            'clinic',
            'date',
            'time',
            'status'
        ]

class ReviewSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    clinic = ClinicSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'clinic',
            'owner',
            'rate',
            'content'
        ]

# CREATE SERIALIZER FOR RESCHUDEL APPOINTMENT 
class ApponintmentReschudleSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer(read_only=True)
    class Meta:
        model = AppointmentReschedule
        fields = [
            'appointment',
            'date',
            'time',
            'status'
        ]
