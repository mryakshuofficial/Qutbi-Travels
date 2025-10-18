from django.db import models

class Booking(models.Model):
    name = models.CharField("Full name", max_length=150)
    phone = models.CharField("Contact number", max_length=20)
    persons = models.PositiveSmallIntegerField("Number of persons", default=1)
    travel_start_date = models.DateField("Travel start date")
    travel_end_date = models.DateField("Travel end date")
    description = models.TextField("Additional info", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='new')  # new/confirmed/cancelled

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.travel_start_date}"
