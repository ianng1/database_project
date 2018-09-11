from django.contrib import admin
from .models import Student, Teacher, Instrument, StudentInstrument
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Instrument)
admin.site.register(StudentInstrument)
