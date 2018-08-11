from django.db import models


class Student(models.Model):
    first_name = models.CharField(null=True, max_length = 25)
    last_name = models.CharField(null=True, max_length = 25)
    email = models.EmailField(null=True)
    birthday = models.DateField(null=True)

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(null=True, max_length = 25)
    last_name = models.CharField(null=True, max_length = 25)
    email = models.EmailField(null=True)
