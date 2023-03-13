from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

class SignIn(View):
    def get(self, request):
        return render(request, 'login/signin.html')

    def post(self, request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                return redirect('home')

            else:
                error_message = 'Invalid username or password'
        else:
            error_message = None

        return render(request, 'login/signin.html', {'error_message': error_message})


class SignUp(View):
    def get(self, request):
        return render(request, 'login/signup.html')

    def post(self, request):
        username = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')

        if password != confirm_password:
            return render(request, 'login/signup.html', {'msg':'Password is does not match!'})

        has_pass = make_password(password)

        user = User(first_name=first_name, last_name=last_name, email=email, password=has_pass, username=username)
        user.save()
        return redirect('/')
