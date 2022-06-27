from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class User(AbstractUser):
    """User Model Definition"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(null=True, blank=True)
    birthday = models.DateField(null=True)
    phone = PhoneNumberField(
        null=True,
        blank=False,
        unique=True,
    )
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )

    rewards = models.BooleanField(default=False)
