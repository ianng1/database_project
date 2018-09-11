from django.db import models


class Student(models.Model):
    first_name = models.CharField(default="", max_length = 35)
    last_name = models.CharField(default="", max_length = 35)
    email = models.EmailField(default="")
    phone_number = models.CharField(default="", max_length = 25)
    birthday = models.DateField(null=True)
    school = models.CharField(default="", max_length = 35)
    parent_first_name = models.CharField(default="", max_length = 35)
    parent_last_name = models.CharField(default="", max_length = 35)
    parent_phone_number = models.CharField(default="", max_length = 25)
    street = models.CharField(default="", max_length = 70)
    street2 = models.CharField(default="", max_length = 70)
    city = models.CharField(default="", max_length = 35)
    zipcode = models.CharField(default="", max_length = 10)
    parent_email = models.EmailField(default="")
    level = models.CharField(default="", max_length = 3)
    full_name = models.CharField(default="", max_length = 80)
    parent_full_name = models.CharField(default="", max_length = 80)
    enrolled = models.BooleanField(default=False)
    comment = models.TextField(default="")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('data', args=[str(self.id)])



# Create your models here.


class Teacher(models.Model):
    name = models.CharField(null=True, max_length = 50)
    email = models.EmailField(null=True)




class Instrument(models.Model):
    instrument = models.CharField(null=True, max_length = 50)




class StudentInstrument(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
