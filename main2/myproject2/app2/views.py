from django.contrib import auth
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import student
def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password != password1:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(username=username, email=email, password=password)
            my_user.save()
            return redirect('login')

    return render(request, 'register.html')


def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('new')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')
def logout_view(request):
    auth.logout(request)
    return redirect('/')
def application_form(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        dob = request.POST.get('dob',)
        age = request.POST.get('age',)
        gender=request.POST.get('gender',)
        phonenumber = request.POST.get('phone number',)
        email= request.POST.get('email',)
        department = request.POST.get('department',)
        purpose = request.POST.get('purpose',)
        materialsprovided = request.POST.get('materials provided',)
        reg_form = student(name=name, email=email, dob=dob,age=age,phonenumber=phonenumber,department=department,purpose=purpose,materialsprovided=materialsprovided)
        reg_form.save()
        return redirect('success')
    return render(request,'admi.html')
def ba(request):
    return render(request,"ba.html")
def bsc(request):
    return render(request,"bsc.html")
def commerce(request):
    return render(request,"commerce.html")
def computer(request):
    return render(request,"computer.html")
def bed(request):
    return render(request,"bed.html")
def new(request):
    return render(request,"new.html")
def success(request):
    return render(request,"success.html")
