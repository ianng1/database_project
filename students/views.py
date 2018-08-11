from django.shortcuts import render, redirect
from .models import Student




# Create your views here.
def create(request):
    if request.method == 'POST':
        if request.POST['first name'] and request.POST['last name'] and request.POST['birthday'] and request.POST['email']:
            student = Student()
            student.first_name = request.POST['first name']
            student.last_name = request.POST['last name']
            student.birthday = request.POST['birthday']
            student.email = request.POST['email']
            student.save()
            print("reached")
            return redirect('create')
        else:
            return render(request, 'students/create.html', {'error': 'Did not fill in all fields'})
    else:
        return render(request, 'students/create.html')
