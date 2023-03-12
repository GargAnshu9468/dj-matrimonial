from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignIn.as_view(), name='signin'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
