from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests

@login_required(login_url='login')
def home(request):
    student_profile = request.user.studentprofile

    library_app_data = requests.get(f'http://127.0.0.1:8000/api/library/{student_profile.student_id}/').json()

    context = {
        'student_id': student_profile.student_id,
        'username': request.user.username,
        'email': request.user.email,
        'course': student_profile.course,
        'year_level': student_profile.year_level,
        'has_fines': library_app_data['has_fines'],
        'amount_due': library_app_data['amount_due']
    }
    return render(request, 'student_app/home.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['student-id']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect('login')

    return render(request, 'student_app/login.html')

@login_required(login_url='login')
def academics(request):
    return render(request, 'student_app/academics.html')


@login_required(login_url='login')
def library(request):
    return render(request, 'student_app/library.html')

@login_required(login_url='login')
def finance(request):
    return render(request, 'student_app/finance.html')

@login_required(login_url='login')
def settings(request):
    context = {
        "name" : request.user.username,
        "email": request.user.email
    }
    return render(request, 'student_app/settings.html', context)