from django.views.generic import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from models.home.LatitudeLongitudeCities import LatitudeLongitudeCity
from django.http import HttpResponse,JsonResponse

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

@csrf_exempt
def get_current_city(request):
    cities = LatitudeLongitudeCity().cities

    latitude = float(request.POST.get('latitude', 0))
    longitude = float(request.POST.get('longitude', 0))

    if not latitude and not longitude:
        return JsonResponse({'city': ''})

    cities_dict = {}

    for city, _, latitude_float, longitude_float in cities:
        rank = ((latitude_float - latitude) ** 2 + (longitude_float - longitude) ** 2) ** 0.5
        cities_dict[rank] = {'city': city}

    city = cities_dict[sorted(cities_dict)[0]].get('city')
    return JsonResponse({'city': city})


