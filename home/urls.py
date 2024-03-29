from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('story/', views.Story.as_view(), name='story'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('family/', views.Family.as_view(), name='family'),
    path('event/', views.Event.as_view(), name='event'),
    path('rsvp/', views.RSVP.as_view(), name='rsvp'),
    path('ajax/get_current_city/', views.get_current_city, name='get-current-city'),
]
