from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile')
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars/')
    company = models.CharField(max_length=255, null=True, blank=True)
    subname = models.CharField(max_length=255, null=True, blank=True)
    family_name = models.CharField(max_length=255, blank=True, null=True)
    site_web = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_a_proffessional_account = models.BooleanField(default=False, blank=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'Profil de {self.user.username}'