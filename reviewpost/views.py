from django.shortcuts import render
from django.contrib.auth.models import User

def signupview(request):
    if request.method == 'POSt':
        username_date = request.POST['username_date']
        password_date = request.POST['password_date']
        user = User.objects.create_user(username_date, '', password_date)
        print('OK')
    else:
        print("else")
        print(User.objects.all())
        return render(request, 'reviewpost/signup.html', {})
    return render(request, 'reviewpost/signup.html', {})
