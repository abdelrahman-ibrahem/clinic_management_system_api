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

class CustomReviewAdminView(admin.ModelAdmin):
    list_display = [
        'owner',
        'rate',
        'content',
        'clinic'
    ]

admin.site.register(Clinic, CustomClinicAdminView)
admin.site.register(ClinicImage)
admin.site.register(Appointment)
admin.site.register(Review, CustomReviewAdminView)
admin.site.register(AppointmentReschedule)
