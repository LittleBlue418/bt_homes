from django.shortcuts import render, redirect

"""
    Log in user, redirect based on request method.
"""
def login(request):
    if request.method == 'POST':
        print('LOGGED IN')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


"""
    Register an account, redirect based on request method.
"""
def register(request):
    if request.method == 'POST':
        print('SUBMITTES REG')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    return redirect('index.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
