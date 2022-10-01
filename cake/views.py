from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Profile
from recipes.models import Recipe

def landing(req):

    if req.user.is_authenticated:
        recipes = Recipe.objects.filter(creator=req.user)
        profile = Profile.objects.get(user=req.user)
        return render(req, 'pages/home.html', {'recettes': recipes, "profile": profile})


    return render(req, 'pages/landing.html')

def download(req):

    resp = HttpResponse('d', headers={'Content-Type': 'application/txt', 'Content-Disposition': 'attachment; filename="Application.exe"'})

    return resp

def help(req):
    profile = Profile.objects.get(user=req.user)
    return render(req, 'pages/help.html', {"profile": profile})