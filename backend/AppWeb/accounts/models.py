from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .helpers import profile_image_path

class Profile(models.Model):
    """An extension of user model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, null=True)
    cant_km = models.IntegerField('cantidad de km', null=True,  blank=True)
    weight = models.IntegerField('peso', null=True,  blank=True)
    height = models.IntegerField('altura en cm', null=True,  blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username's name."""
        return f'{self.user.username} profile'

