from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)


class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel/')
    tagline = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.tagline