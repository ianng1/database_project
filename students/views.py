from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['first name'] and request.POST['last name'] and request.POST['parent first name'] and request.POST['parent last name'] and request.POST['birthday'] and request.POST['email'] and request.POST['phone number'] and request.POST['instrument'] and request.POST['teacher']:
            student = Student()
            student.first_name = request.POST['first name']
            student.last_name = request.POST['last name']
            student.parent_first_name = request.POST['parent first name']
            student.parent_last_name = request.POST['parent last name']
            student.birthday = request.POST['birthday']
            student.email = request.POST['email']
            student.parent_email = request.POST['parent email']
            student.phone_number = request.POST['phone number']
            student.parent_phone_number = request.POST['parent phone number']
            student.instrument = request.POST['instrument']
            student.teacher = request.POST['teacher']
            student.full_name = student.first_name + " " + student.last_name
            student.save()
            print("reached")
            return redirect('create')
        else:
            return render(request, 'students/create.html', {'error': 'Did not fill in all fields'})
    else:
        return render(request, 'students/create.html')



@login_required
def home(request):
    if request.method == 'POST':
        if request.POST['namequery']:
            searchname = request.POST['namequery']
            students_first_name = Student.objects.filter(first_name__icontains=searchname)
            students_last_name = Student.objects.filter(last_name__icontains=searchname)

            return render(request, 'students/home.html', {'students_first_name': students_first_name, 'students_last_name': students_last_name})
        else:
            return render(request, 'students/home.html')
    else:
        return render(request, 'students/home.html')



@login_required
def data(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/data.html', {'student': student})
