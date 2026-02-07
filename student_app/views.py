from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def home(request):
    student_profile = request.user.studentprofile
    context = {
        'student_id': student_profile.student_id,
        'username': request.user.username,
        'email': request.user.email,
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