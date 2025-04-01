from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(max_length=255,null=False,blank=False)
    password = models.CharField(max_length=100,null=False, blank=False)
    def __str__(self):
        return self.name

from django.contrib.auth.hashers import make_password

class Contact3(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.name
class Nav(models.Model):
    img = models.CharField(max_length=100,null=True)
    texts = models.EmailField(max_length=255,null=True)
    s_texts = models.EmailField(max_length=255,null=True)
    
    
    def __str__(self):
        return self.img
    
class Forms(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return f"{self.name} - {self.phone}"
