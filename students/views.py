from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher, Instrument, StudentInstrument
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
import json




# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['ID']:
            student = get_object_or_404(Student, pk = request.POST['ID'])
        else:
            student = Student()
        if request.POST['first name'] and request.POST['last name'] and request.POST['parent first name'] and request.POST['parent last name'] and request.POST['birthday'] and request.POST['email']:
            student.first_name = request.POST['first name']
            student.last_name = request.POST['last name']
            student.parent_first_name = request.POST['parent first name']
            student.parent_last_name = request.POST['parent last name']
            student.birthday = request.POST['birthday']
            student.email = request.POST['email']
            student.parent_email = request.POST['parent email']
            student.phone_number = request.POST['phone number']
            student.parent_phone_number = request.POST['parent phone number']
            student.level = request.POST['level']
            student.school = request.POST['school']
            student.street = request.POST['street']
            student.street2 = request.POST['street2']
            student.city = request.POST['city']
            student.zipcode = request.POST['zipcode']
            # student.level = request.POST['enrolled']
            student.comment = request.POST['comment']
            student.full_name = student.first_name + " " + student.last_name
            student.parent_full_name = student.parent_first_name + " " + student.parent_last_name
            student.save()
            if request.is_ajax():
                data = [{
                    }]
                return HttpResponse(json.dumps(data), content_type="application/json")
            else:
                return redirect('/data/' + str(student.id))
        else:
            return render(request, 'students/create.html', {'error': 'Did not fill in all fields'})
    else:
        teachers = Teacher.objects.all()
        return render(request, 'students/create.html', {'teacher_name': teachers})



@login_required
def home(request):
    if request.method == 'POST':
        if request.POST['namequery']:
            searchname = request.POST['namequery']
            students_name = Student.objects.filter(full_name__icontains=searchname)

            return render(request, 'students/home.html', {'students_name': students_name, 'searchfired': True})
        else:
            return render(request, 'students/home.html')
    else:
        return render(request, 'students/home.html')



@login_required
def data(request, student_id):
    if student_id:
        student = get_object_or_404(Student, pk = student_id)
        studentinstruments = StudentInstrument.objects.filter(student_id = student_id)


    if request.method == 'POST':
        student = get_object_or_404(Student, pk = request.POST['ID'])
        if request.POST['first name'] and request.POST['last name'] and request.POST['birthday'] and request.POST['email1']:
            student.first_name = request.POST['first name']
            student.last_name = request.POST['last name']
            student.parent_first_name = request.POST['parent first name']
            student.parent_last_name = request.POST['parent last name']
            student.birthday = request.POST['birthday']
            student.email = request.POST['email']
            student.parent_email = request.POST['parent email']
            student.phone_number = request.POST['phone number']
            student.parent_phone_number = request.POST['parent phone number']
            student.level = request.POST['level']
            student.school = request.POST['school']
            student.street = request.POST['street']
            student.street2 = request.POST['street2']
            student.city = request.POST['city']
            student.zipcode = request.POST['zipcode']
            # student.enrolled = request.POST['enrolled']
            student.comment = request.POST['comment']
            student.full_name = student.first_name + " " + student.last_name
            student.parent_full_name = student.parent_first_name + " " + student.parent_last_name
            student.save()
    teachers = Teacher.objects.all()
    instruments = Instrument.objects.all()

    return render(request, 'students/data.html', {'student': student, 'teacher_name': teachers, 'instrument_name': instruments, 'studentinstruments': studentinstruments})


@login_required
def refresh(request):
    student = Student.objects.filter(pk = request.POST['ID'])
    studentinstrument = StudentInstrument.objects.filter(student_id = request.POST['ID'])
    teachers = Teacher.objects.all()
    instruments = Instrument.objects.all()
    studentinstrumentlist = []
    for i in studentinstrument:
        fields = {}
        fields["studentinstrument_id"] = i.id
        fields["student_id"] = i.student.id
        fields["instrument_id"] = i.instrument.id
        fields["instrument"] = i.instrument.instrument
        fields["teacher_id"] = i.teacher.id
        fields["teacher_name"] = i.teacher.name
        studentinstrumentlist.append(fields)

    studentjson = serializers.serialize("json", student)
    studentinstrumentjson = serializers.serialize("json", studentinstrument)
    teachersjson = serializers.serialize("json", teachers)
    instrumentsjson = serializers.serialize("json", instruments)

    data = [{
        'student':studentjson,
        'studentinstrument':studentinstrumentjson,
        'teachers':teachersjson,
        'instrument':instrumentsjson,
        'studentinstrumentlist': studentinstrumentlist
        }]
    return HttpResponse(json.dumps(data), content_type="application/json")

@login_required
def delitem(request):
    if request.POST['student_id']:
        student = get_object_or_404(Student, pk=request.POST['student_id'])
    if  request.POST['studentinstrument_id']:
        studentinstrument = get_object_or_404(StudentInstrument, pk=request.POST['studentinstrument_id'])
        if studentinstrument:
            studentinstrument.delete()
    if request.is_ajax():
        data = [{
                }]
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return redirect('/data/' + str(student.id))


@login_required
def additem(request):
    if request.POST['student_id']:
        student = get_object_or_404(Student, pk=request.POST['student_id'])
        instrument = get_object_or_404(Instrument, pk= request.POST.get('instrument'))
        teacher = get_object_or_404(Teacher, pk= request.POST.get('teacher'))
        if Instrument and Teacher:
            studentinstrument = StudentInstrument()
            studentinstrument.student = student
            studentinstrument.instrument = instrument
            studentinstrument.teacher = teacher
            studentinstrument.save()
        if request.is_ajax():
            data = [{
                }]
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            return redirect('/data/' + str(student.id))
