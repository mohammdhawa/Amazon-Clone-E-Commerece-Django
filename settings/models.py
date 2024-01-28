from django.db import models

# Create your models here.

class Settings(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='settings')
    subtitle = models.TextField(max_length=500)
    call_us = models.CharField(max_length=25)
    email_us = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phones = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    android_app = models.URLField(null=True, blank=True)
    ios_app = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    pinterest = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
