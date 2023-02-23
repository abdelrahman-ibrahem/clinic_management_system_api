from django.urls import path 
from . import views

urlpatterns = [
    path('', views.ListCreateClinics.as_view()),
    path('appointments/', views.ViewAllAppointments.as_view()),
    path('appointments/<int:pk>', views.RetrevieDeleteAppointment.as_view()),
    path('appointments/create/', views.CreateAppointment.as_view()),
    path('reviews/', views.ListCreateReview.as_view()),
    path('reviews/<int:pk>', views.RetrevieDeleteUpdateReview.as_view()),
]
