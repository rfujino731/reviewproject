from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

def signupview(request):
    if request.method == 'POST':
        username_date = request.POST['username_data']
        password_date = request.POST['password_data']
        try:
            user = User.objects.create_user(username_date, '', password_date)
        except IntegrityError:
            return render(request, 'reviewpost/signup.html', {'error': '既に登録されています。'})
    else:
        #print(User.objects.all())
        return render(request, 'reviewpost/signup.html', {})
    return render(request, 'reviewpost/signup.html', {})

def loginview(request):
    if request.mrthod == 'POST':
        username_date = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_date, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')
