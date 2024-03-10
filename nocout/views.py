from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        payload = request.POST
        name = payload.get('name')
        email = payload.get('email')
        subject = payload.get("subject")
        message = payload.get("message")
        data = ContactUs(name=name, email=email, subject=subject, message=message)
        print("***********",settings.EMAIL_HOST_USER)
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['info@fiboseq.com'],
            fail_silently=False,
        )
        print("email send successfully")
        data.save()
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def team(request):
    return render(request, "team.html")

def testimonials(request):
    return render(request, "testimonials.html")

def contact(request):
    if request.method == 'POST':
        payload = request.POST
        name = payload.get('name')
        email = payload.get('email')
        subject = payload.get("subject")
        message = payload.get("message")
        data = ContactUs(name=name, email=email, subject=subject, message=message)
        data.save()
    return render(request, "contact.html")