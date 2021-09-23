from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
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

        user = User.objects.create_user(username=username, password= password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('/')
    else: 
        return render(request, 'register.html')
    