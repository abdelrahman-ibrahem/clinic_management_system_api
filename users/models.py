from django.db import models
from django.contrib.auth.models import AbstractUser


ROLE = (
    ('user', 'user'),
    ('docter', 'docter')
)
class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    phone = models.CharField(max_length=11)
    role = models.CharField(choices=ROLE, max_length=120, default='user')
    
