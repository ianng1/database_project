
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher, Instrument, StudentInstrument
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from django.conf import settings
from django.core.mail import send_mail
import json
import urllib
import urllib.request



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
            student.date_enrolled = request.POST['date_enrolled']
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
    teachers = Teacher.objects.all().order_by('name')
    instruments = Instrument.objects.all().order_by('instrument')
    if request.method == 'POST':
        if request.POST['namequery'] or request.POST['parent'] or request.POST['instrument'] or request.POST['instructor']:
            searchname = request.POST['namequery']
            parent = request.POST['parent']

            if request.POST['instrument'] or request.POST['instructor']:
                studentInstruments = StudentInstrument.objects.all()
                if request.POST['instrument']:
                    instrumentObj = get_object_or_404(Instrument, pk=request.POST['instrument'])
                    if instrumentObj:
                        studentInstruments = studentInstruments.filter(instrument=instrumentObj)
                if request.POST['instructor']:
                    teacherObj = get_object_or_404(Teacher, pk=request.POST['instructor'])
                    if teacherObj:
                        studentInstruments = studentInstruments.filter(teacher=teacherObj)
                students_name = Student.objects.filter(pk__in=studentInstruments.values('student'), full_name__icontains=searchname, parent_full_name__icontains=parent)
            else:
                students_name = Student.objects.filter(full_name__icontains=searchname, parent_full_name__icontains=parent)
            return render(request, 'students/home.html', {'students_name': students_name, 'searchfired': True, 'teachers': teachers, 'instruments': instruments})
        else:
            return render(request, 'students/home.html', {'teachers': teachers, 'instruments': instruments})
    else:
        return render(request, 'students/home.html', {'teachers': teachers, 'instruments': instruments })



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
            student.date_enrolled = request.POST['date_enrolled']
            student.full_name = student.first_name + " " + student.last_name
            student.parent_full_name = student.parent_first_name + " " + student.parent_last_name
            student.save()
    teachers = Teacher.objects.all().order_by('name')
    instruments = Instrument.objects.all().order_by('instrument')

    return render(request, 'students/data.html', {'student': student, 'teacher_name': teachers, 'instrument_name': instruments, 'studentinstruments': studentinstruments})


@login_required
def refresh(request):
    student = Student.objects.filter(pk = request.POST['ID'])
    studentinstrument = StudentInstrument.objects.filter(student_id = request.POST['ID'])
    teachers = Teacher.objects.all().order_by('name')
    instruments = Instrument.objects.all().order_by('instrument')
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
    if  request.POST['studentinstrument_id']:
        studentinstrument = get_object_or_404(StudentInstrument, pk=request.POST['studentinstrument_id'])
        student = studentinstrument.student
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


def register(request):
    if request.method == 'POST':

        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:

            student = Student()
            if request.POST['first name'] and request.POST['last name'] and request.POST['birthday'] and request.POST['email']:
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
                subject = 'New student registration -' + ' ' + student.first_name + ' ' + student.last_name
                send_mail(subject, '', '', [settings.DEFAULT_TO_EMAIL], fail_silently=True)
                return render(request, 'students/register_complete.html')

            else:
                return render(request, 'students/register.html', {'error': 'Did not fill in all fields'})
        else:
            return render(request, 'students/register.html', {'error': 'Did not complete reCAPTCHA'})

    else:
        return render(request, 'students/register.html')


@login_required
def delete(request):
    print(request.POST['ID'])
    if request.method == 'POST':

        if request.POST['ID']:
            student = get_object_or_404(Student, pk = request.POST['ID'])
        if student:
            student.delete()
            return render(request, 'students/home.html')
