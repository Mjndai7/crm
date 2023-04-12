from django.db import models
import datetime
from PIL import Image
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(default=datetime.date.today)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # email is already required, no need to add

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.email

# Employees profile
class employeeProfile(models.Model):
    image = models.ImageField(default='default.png',upload_to='media')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="employee_profile")
    phone_no = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    date_employed = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user.name

    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs) 

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



# Employee HR detail

class employeeDetails(models.Model):
    Department_Choices = (
        ('Finance', 'Finance'),
        ('HR', 'HR'),
        ('Customer Care', 'Customer Care'),
        ('Sales', 'Sales'),
        ('Marketing', 'Marketing'),
        ('IT', 'IT'),
        ('Accounting', 'Accounting'),
        ('Executive', 'Executive'),
        ('Cleaning', 'Cleaning'),
        ('Logistics', 'Logistics'),

    )

    Title_Choices = (
        ('CEO', 'CEO'),
        ('CFO', 'CFO'),
        ('CTO', 'CTO'),
        ('HR Manager', 'HR Manager'),
        ('Sr Developer', 'Sr Developer'),
        ('Jnr Developer', 'Jnr Developer'),
        ('Accountant', 'Accountant'),
        ('Consultant', 'Consultant'),
        ('Sales Executive', 'Sales Executive'),
        ('DevOps Engineer', 'DevOps Engineer') ,
        ('Managing Partner', 'Managing Partner'),
        ('Head of Logistics', 'Head of Logistics'),
    )


    name = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=10, blank=True, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    department = models.CharField(max_length=20, choices=Department_Choices)
    job_title = models.CharField(max_length=20, choices=Title_Choices)
    salary = models.IntegerField()
    date_employed = models.DateField(default=datetime.date.today)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.name

