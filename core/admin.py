# locator/admin.py
from django.contrib import admin
from .models import EwasteLocation

@admin.register(EwasteLocation)
class EwasteLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'latitude', 'longitude', 'timings')
    search_fields = ('name', 'city', 'state', 'address', 'accepted_items')
