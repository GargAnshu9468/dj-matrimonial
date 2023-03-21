from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import ProfileHome
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ("groom_name","bride_name","image")

admin.site.register(ProfileHome)