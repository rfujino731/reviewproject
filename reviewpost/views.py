from django.shortcuts import render

def signupview(request):
    if request.method == 'POST':
        print("OK")
       # username_date = request.POST['username_data']
       # password_date = request.POST['password_data']
       # user = User.object.create_user(username_date, '', password_date)
    else:
        render(request, 'reviewpost/signup.html', {})
    return render(request, 'reviewpost/signup.html', {})
