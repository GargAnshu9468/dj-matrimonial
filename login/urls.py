from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignIn.as_view(), name='signin'),
]
