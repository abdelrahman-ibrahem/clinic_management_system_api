from rest_framework import serializers
from .models import Appointment, Clinic, Review
from users.serializers import UserSerializer

# CREATE MODELS SERIALIZERS

class ClinicSerializer(serializers.ModelSerializer):
    docter = UserSerializer(read_only=True)

    class Meta:
        model = Clinic
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'user',
            'clinic',
            'date',
            'time'
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'clinic',
            'owner',
            'rate',
            'content'
        ]