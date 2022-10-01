from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from .models import Profile

admin.site.unregister(Group)
admin.site.register(Profile)
