from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Clinic(models.Model):
    '''
        Clinic just Contains the information of the clinic 
    '''
    name = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    docter = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    descrption = models.TextField(max_length=300)
    image = models.ImageField(upload_to='clinic/', blank=True, null=True)

    def __str__(self):
        return str(self.name)

class ClinicImage(models.Model):
    image = models.ImageField(upload_to='clinic_sub_image/', null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True, blank=True)

class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=1)
    content = models.CharField(max_length=120)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content)


APPOINTMENTS_STATUS = (
    ('cancel', 'cancel'),
    ('approve', 'approve'),
    ('missed', 'missed'),
    ('finished', 'finished'),
)

class Appointment(models.Model):
    '''
        Appointments contain the clinic id, user information 
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    status = models.CharField(choices=APPOINTMENTS_STATUS, max_length=120, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.clinic.name)

