from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'persons', 'travel_start_date', 'travel_end_date', 'status', 'created_at')
    list_filter = ('status', 'travel_start_date')
    search_fields = ('name', 'phone')
