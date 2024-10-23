from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    state = models.CharField(max_length=50, default="")
    district = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    interests = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    quality = models.CharField(max_length=100, choices=[
        ('Organic', 'Organic'),
        ('High', 'High Quality'),
        ('Medium', 'Medium Quality'),
        ('Low', 'Low Quality'),
        ('Other', 'Other'),
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField(null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)  # Make sure this field is present

    def __str__(self):
        return self.name

    def is_expired(self):
        """Checks if the product is expired."""
        return now().date() > self.expiry_date
