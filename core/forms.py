from django import forms
from core.models import User, Address, Doctor, Patient, Timetable, Schedule
# from django_select2.forms import Select2Widget,ModelSelect2Widget
# from contact.models import Customer
# from product.models import ProductVariant
from django.forms.models import inlineformset_factory


class DoctorForm(forms.ModelForm):
    
    class Meta:
        model = Doctor
        fields = [
            'name', 'degree','dob','gender', 'description', 'address', 'phone',
            'email', 'status' 
         
        ]

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = [
            'name', 'doctor', 'dob', 'gender', 'description', 'address', 'phone',
            'email', 'status' 
         
        ]

class DoctorScheduleForm(forms.ModelForm):
    
    class Meta:
        model = Schedule
        fields = [
            'doctor', 'timetable','start_date','end_date', 'note' 
        ]



class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'

# InvoiceItemFormSet=inlineformset_factory(Address,Sale,
#     fields=('invoice','item','quantity','unit_price','total',),extra=5,can_delete=True)

