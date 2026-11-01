from django.conf import settings
from django.db import models
from django.db.models import Q

from doctors.models import DoctorProfile


class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'در انتظار تأیید'
        CONFIRMED = 'confirmed', 'تأیید شده'
        CANCELLED = 'cancelled', 'لغو شده'
        DONE = 'done', 'انجام شده'

    doctor = models.ForeignKey(
        DoctorProfile,
        on_delete=models.PROTECT,
        related_name='appointments',
    )
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='appointments',
    )
    date = models.DateField()
    start_time = models.TimeField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'start_time']
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'date', 'start_time'],
                condition=~Q(status='cancelled'),
                name='unique_active_appointment_per_slot',
            ),
        ]

    def __str__(self):
        return f'{self.patient} → {self.doctor} ({self.date} {self.start_time})'