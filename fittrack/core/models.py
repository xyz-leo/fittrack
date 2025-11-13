# core/models.py
from django.db import models

class Student(models.Model):
    """
    Student model holds basic user information.
    This is a prototype — passwords are stored in plaintext for simplicity, which is NOT secure.
    """
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    OBJECTIVE_CHOICES = [
        ('mass_gain', 'Mass Gain'),
        ('fat_loss', 'Fat Loss'),
        ('maintenance', 'Maintenance'),
    ]

    full_name = models.CharField(max_length=200)  # student's full name
    email = models.EmailField(unique=True)        # unique email (used as login)
    password = models.CharField(max_length=128)   # plaintext for prototype (INSECURE)
    height_cm = models.PositiveIntegerField(null=True, blank=True)  # height in cm
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # weight in kg
    age = models.PositiveIntegerField(null=True, blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    frequency_per_week = models.PositiveIntegerField(default=3)  # training freq per week
    objective = models.CharField(max_length=20, choices=OBJECTIVE_CHOICES, default='maintenance')
    created_at = models.DateTimeField(auto_now_add=True)


    def first_name(self):
        return self.full_name.split(" ")[0]


    def __str__(self):
        return f"{self.full_name} <{self.email}>"

