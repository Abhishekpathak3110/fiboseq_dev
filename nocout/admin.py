from django.contrib import admin
from .models import *
# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ['name', 'email', 'subject', 'message']
    list_filter = ['name', 'email']

class CarouselItemsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ['image', 'tagline', 'description']

admin.site.register(ContactUs,ContactUsAdmin)
admin.site.register(CarouselItem)

