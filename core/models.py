from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from django.apps import apps
from multiselectfield import MultiSelectField


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.conf import settings

from django.db.models import Sum


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        # Creates and save a new user
        if not email:
            raise ValueError('Users must have an email address!')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # Creates and save a new superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin, AbstractBaseUser):
    # Custom user model supports email instead of username
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

GENDER = (
    ('male', 'MALE'),
    ('female', 'FEMAIL'),
)

class Doctor(models.Model):
    name = models.CharField(max_length=60)
    degree = models.CharField(max_length=60)
    dob = models.DateField()
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    address = models.ForeignKey(
        'Address', on_delete=models.SET_NULL, 
        null=True, blank=True)
    phone = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField(max_length=60)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('doctors_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('doctors_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('doctors_delete', args=(self.pk,))


class Address(models.Model):
    address_line1 = models.CharField(max_length=60)

    def __str__(self):
        return self.address_line1



WEEKDAYS = (
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
)

class Timetable(models.Model):
    name = models.CharField(max_length=60)
    weekdays = MultiSelectField(choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
        # return f'{self.name} - {self.weekdays}'

class Schedule(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    timetable = models.ForeignKey('Timetable', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    note = models.TextField(blank=True, null=True)


    def __str__(self):
        return f'{self.doctor.name} - {self.timetable.name}'

    def get_update_url(self):
        return reverse('doctors_schedule_update', args=(self.pk,))

    def get_delete_url(self):
        return reverse('doctors_schedule_delete', args=(self.pk,))

class Patient(models.Model):
    name = models.CharField(max_length=60)
    dob = models.DateField()
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    address = models.ForeignKey(
        'Address', on_delete=models.SET_NULL, 
        null=True, blank=True)
    phone = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField(max_length=60)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    doctor = models.ForeignKey(
        'Doctor', on_delete=models.SET_NULL, 
        null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('patients_detail', kwargs={'pk': self.pk})

class Appointment(models.Model):
    patient = models.ForeignKey(
        'Patient', on_delete=models.SET_NULL, 
        null=True, blank=True)
    appointment_date = models.DateTimeField()

    def __str__(self):
        return f'{self.patient} - {self.appointment_date}'

