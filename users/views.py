from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions, generics
from .serializers import UserSerializer, CustomRegisterSerializer
from django.contrib.auth import get_user_model


