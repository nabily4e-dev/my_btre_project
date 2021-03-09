
from django.shortcuts import redirect, render


def register(request):
    """"""
    
    if request.method == 'POST':
        # Register User
        print('SUBMITTED REG')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    """"""
    
    if request.method == 'POST':
        # Login User
        print('SUBMITTED REG')
        return redirect('register')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    """"""
    
    return redirect(request, 'index')


def dashboard(request):
    """"""
    
    
    return render(request, 'accounts/dashboard.html')


