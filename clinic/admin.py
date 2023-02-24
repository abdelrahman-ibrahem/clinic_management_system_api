from django.contrib import admin
from .models import (Appointment, Clinic, ClinicImage,
                        Review, AppointmentReschedule)

class ReviewInlineView(admin.TabularInline):
    model = Review

class ImagesInlineView(admin.TabularInline):
    model = ClinicImage

class CustomClinicAdminView(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
    ]
    inlines = [
        ReviewInlineView,
        ImagesInlineView
    ]



admin.site.register(Clinic, CustomClinicAdminView)
admin.site.register(ClinicImage)
admin.site.register(Appointment)
admin.site.register(Review)
admin.site.register(AppointmentReschedule)
