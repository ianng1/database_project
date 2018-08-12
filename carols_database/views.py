from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts.login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')
