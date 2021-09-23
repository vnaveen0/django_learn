from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth 


# Create your views here.
def register(request):
    # return HttpResponse("Hello World")
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['userid']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email id  taken')
                return redirect('register')
            else: 
                user = User.objects.create_user(username=username, password= password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password Taken')
            return redirect('register')

    else: 
        return render(request, 'register.html')

# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST['userid']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else: 
            messages.error(request,'Incorrect Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')