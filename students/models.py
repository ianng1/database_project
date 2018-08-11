from django.db import models
class Student(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length = 200)
# Create your models here.


class Teacher(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length = 200)
