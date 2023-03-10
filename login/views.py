from django.shortcuts import render, redirect
from django.views.generic import View


class SignIn(View):
    def get(self, request):
        return render(request, 'login/signin.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        return redirect('home')


class SignUp(View):
    def get(self, request):
        pass
