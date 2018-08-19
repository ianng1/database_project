from django.db import models


class Student(models.Model):
    first_name = models.CharField(null=True, max_length = 25)
    last_name = models.CharField(null=True, max_length = 25)
    email = models.EmailField(null=True)
    phone_number = models.CharField(null=True, max_length = 25)
    birthday = models.DateField(null=True)
    parent_first_name = models.CharField(null=True, max_length = 25)
    parent_last_name = models.CharField(null=True, max_length = 25)
    parent_phone_number = models.CharField(null=True, max_length = 25)
    parent_email = models.EmailField(null=True)
    instrument = models.CharField(null = True, max_length = 25)
    teacher = models.CharField(null=True, max_length = 25)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('data', args=[str(self.id)])



# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(null=True, max_length = 25)
    last_name = models.CharField(null=True, max_length = 25)
    email = models.EmailField(null=True)
