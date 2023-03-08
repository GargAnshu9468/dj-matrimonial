from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/',views.About.as_view(),name="about"),
    path('story/',views.Story.as_view(),name="story"),
    path('gallery/',views.Gallery.as_view(),name="gallery"),
    # path('about/',views.About.as_view(),name="about"),
    # path('about/',views.About.as_view(),name="about")
]
