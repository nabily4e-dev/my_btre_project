from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    """"""

    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('register')
            else:
                # Create User
                user = User.objects.create_user(username=username,
                                                password=password,
                                                email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                # Login after register
                # auth.login(request, user)
                # messages.success(request, 'Logedin success')
                # redirect('index')
                
                user.save()
                messages.success(request, 'You are now registered and can log in')
                return redirect('login')
                
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')

        # # Register User
        # messages.error(request, 'Testing error message')
        # return redirect('register')
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
