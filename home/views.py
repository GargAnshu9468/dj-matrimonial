from django.views.generic import View
from django.shortcuts import render


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "components/home.html")

class About(View):
    def get(self,request):
        return render(request,'components/about.html')
    
class Story(View):
    def get(self,request):
        return render(request,'components/story.html')
    
class Gallery(View):
    def get(self,request):
        return render(request,'components/gallery.html')