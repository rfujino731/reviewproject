from django.shortcuts import render

def signupview(request):
    if request.method == 'POSt':
       print('POST method')
    else:
        print("GET method probably")
    return render(request, 'reviewpost/signup.html', {})
