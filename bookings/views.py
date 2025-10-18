from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookingForm

# Create your views here.

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking_success')

class BookingSuccessView(TemplateView):
    template_name = 'bookings/success.html'
