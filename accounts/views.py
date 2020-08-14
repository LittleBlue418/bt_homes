from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

"""
    Log in user, redirect based on request method.
"""
def login(request):
    if request.method == 'POST':
        # Get login variables
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalic credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


"""
    Register an account, redirect based on request method.
    Capturing errors.
"""
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if not password == password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'That username is taken')
            return redirect('register')

        # Check email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'That email is already in use')
            return redirect('register')

        # Validation Passed
        user = User.objects.create_user(
            username=username, password=password, email=email,
            first_name=first_name, last_name=last_name)

        # Login after register
        # auth.login(request, user)
        # messages.success(request, 'You are now logged in')
        # return redirect('index')

        user.save()
        messages.success(request, 'Your account has been created!')
        return redirect('login')

    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
