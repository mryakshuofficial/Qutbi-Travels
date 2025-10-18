from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'persons', 'travel_start_date', 'travel_end_date', 'description']
        widgets = {
            'travel_start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'travel_end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
