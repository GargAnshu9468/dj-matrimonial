from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


class SignIn(View):
    def get(self, request):
        return render(request, 'login/signin.html')

    def post(self, request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'home')
                if next_url:
                    return redirect(next_url)

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

def log_out(request):
    logout(request)
    return redirect("/")

@login_required(login_url='/')
def change_password(request):
    if request.method == 'POST':
        passwd = request.POST.get("old_password")
        user  = User.objects.filter(password=passwd)
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'login/change_password.html', {'form': form})
