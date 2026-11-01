from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        DOCTOR = 'doctor', 'پزشک'
        PATIENT = 'patient', 'بیمار'

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.PATIENT)
    phone = models.CharField(max_length=15, blank=True)

class PatientProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='patient_profile',
    )
    national_id = models.CharField(max_length=10, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username