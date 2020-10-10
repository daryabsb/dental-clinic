from django.shortcuts import render, HttpResponse

from .models import User, Address, Doctor, Patient, Appointment, Schedule
from .forms import DoctorForm, PatientForm, DoctorScheduleForm

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class Home(ListView):
    model = User
    template_name = "index.html"

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/doctors_list.html'

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctors_create.html'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctors/doctors_detail.html'

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctors_create.html'


# PATIENT VIEW CLASSES
class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patients_list.html'

class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patients_create.html'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patients/patients_detail.html'

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patients_create.html'


# SCHEDULE VIEWS

class DoctorScheduleListView(ListView):
    model = Schedule
    template_name = 'doctors/doctors_schedule_list.html'

class DoctorScheduleCreateView(CreateView):
    model = Schedule
    form_class = DoctorScheduleForm
    template_name = 'doctors/doctors_schedule_create.html'

class DoctorScheduleUpdateView(UpdateView):
    model = Schedule
    form_class = DoctorScheduleForm
    template_name = 'doctors/doctors_schedule_list.html'

class DoctorScheduleDeleteView(DeleteView):
    model = Schedule

    