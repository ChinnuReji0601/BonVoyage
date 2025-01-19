from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Package(models.Model):
    name = models.CharField(max_length=200)
    package_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    features = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="documents",default="image.jpg")
    details = models.TextField()

class TablePayment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    payment_method = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=7)  # YYYY-MM format
    cvv = models.CharField(max_length=3)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the record is created
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line

    def __str__(self):
        return f"Payment for {self.package.name} by {self.first_name} {self.last_name}"
class Aboutus(models.Model):
    description=models.TextField()
class Contactus(models.Model):
    phone=models.IntegerField()
    email = models.EmailField()
    address=models.TextField()

class Terms(models.Model):
    description=models.TextField()

class Enquiry(models.Model):
    email = models.EmailField()
    enquiry = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.email} on {self.submitted_at.strftime('%Y-%m-%d %H:%M:%S')}"


class Register(models.Model):
    us=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=50)
    phone=models.IntegerField()

