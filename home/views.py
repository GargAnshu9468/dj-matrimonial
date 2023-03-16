from django.views.generic import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='/'), name='dispatch')
class Home(View):
    def get(self, request):
        return render(request, 'components/home.html')

@method_decorator(login_required(login_url='/'), name='dispatch')
class About(View):
    def get(self, request):
        return render(request, 'components/about.html')

@method_decorator(login_required(login_url='/'), name='dispatch')
class Story(View):
    def get(self, request):
        return render(request, 'components/story.html')

@method_decorator(login_required(login_url='/'), name='dispatch')
class Gallery(View):
    def get(self, request):
        return render(request, 'components/gallery.html')

@method_decorator(login_required(login_url='/'), name='dispatch')
class Family(View):
    def get(self, request):
        return render(request, 'components/friends-family.html')

@method_decorator(login_required(login_url='/'), name='dispatch')
class Event(View):
    def get(self, request):
        return render(request, 'components/event.html')

@method_decorator(login_required(login_url='/'), name='dispatch')
class RSVP(View):
    def get(self, request):
        return render(request, 'components/rsvp.html')
