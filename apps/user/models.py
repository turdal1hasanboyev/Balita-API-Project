from django.db import models

from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

from datetime import date

from apps.common.models import BaseModel
from .managers import CustomUserManager


class CustomUser(BaseModel, AbstractUser):
    GENDER = (
        ('Male', ('Male')),
        ('Female', ('Female')),
    )
    username = None
    email = models.EmailField(unique=True, null=True, blank=True, max_length=225, db_index=True)
    description = RichTextField(null=True, blank=True)
    note = models.CharField(max_length=80, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, db_index=True)
    image = models.ImageField(upload_to='images', default='img/default-user.png', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    gender = models.CharField(max_length=25, choices=GENDER, null=True, blank=True)
    adress = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'phone_number',
        'first_name',
        'last_name',
        ]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def age(self):
        # If birth_date does not exist or is in the wrong format, we return None
        if not isinstance(self.birthday, date):
            return None
        today = date.today()
        age = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
        return age

    def __str__(self):
        if self.get_full_name():
            return f"{self.get_full_name()}"
        if self.email:
            return f"{self.email}"
