from django.shortcuts import render, HttpResponse

from .models import User, Address, Doctor, Patient, Appointment, Schedule
from .forms import DoctorForm, PatientForm, DoctorScheduleForm

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class Home(ListView):
    model = User
    template_name = "index.html"

class DoctorListView(ListView):
    # title = Doctors
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctors_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DoctorListView, self).get_context_data(*args, **kwargs)
        form = DoctorForm()
        context['form'] = form

        return context

class DoctorCreateView(CreateView):
    title = 'Create'
    page_head = 'Add a new Doctor'
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctors_create.html'
    

    def get_success_url(self):
        return reverse('doctors_list')


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctors/doctors_detail.html'

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctors_create.html'

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctors/doctors_delete.html'
    success_url = '/doctors/'



# PATIENT VIEW CLASSES
class PatientListView(ListView):
    title = 'Create'
    page_head = 'Add a new Doctor'
    model = Patient
    template_name = 'patients/patients_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PatientListView, self).get_context_data(*args, **kwargs)
        form = PatientForm()
        context['form'] = form

        return context

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

    