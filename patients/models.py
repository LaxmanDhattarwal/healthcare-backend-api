
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Patient(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patients",
    )

    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)]
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
