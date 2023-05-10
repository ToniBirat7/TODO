from django.shortcuts import render, redirect
from main_app.models import TODO
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

# Create your views here.
def Register(request):
    if request.method == 'GET':
         return render(request,'auth_app/register.html')
    else: 
         fn = request.POST['first_name']
         ln = request.POST['last_name']
         email = request.POST['email']
         username = request.POST['username']
         password = request.POST['password']
         User.objects.create_user(first_name=fn,last_name=ln,email=email,username=username,password=password)
         return redirect('home')

def Login(request):
     if request.method == 'GET':
          return render(request, 'auth_app/login.html')
     else:
          username = request.POST['username']
          password = request.POST['password']
     user = authenticate(request,username=username,password=password)
     if user is not None:
          login(request,user)
          return redirect('home')
     else:
          return redirect('login')

def Logout(request):
     logout(request)
     return redirect('login')