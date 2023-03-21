from django.db import models

class ProfileHome(models.Model):
    groom_name = models.CharField(max_length=20)
    bride_name = models.CharField(max_length=20)
    image  = models.ImageField(upload_to="media")
    class Meta:
        app_label = "home"

    def __str__(self):
        return self.groom_name
