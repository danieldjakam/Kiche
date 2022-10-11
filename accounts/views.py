from django.shortcuts import render, redirect
from .forms import RegisterForm, EditProfileForm
from django.utils.translation import get_language, activate
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def register(req):
    if req.user.is_authenticated:
        return redirect('landing')
    if req.method == 'POST':
        form = RegisterForm(req.POST)

        if form.is_valid():
            user = form.save(commit=False)
            profile = Profile()
            
            profile.user = user
            user.save()
            profile.save()
            return redirect('accounts:login')

    else:
        form = RegisterForm()

    return render(req, 'auth_pages/register.html', {'form': form})

@login_required
def settings(req):
    profile = Profile.objects.get(user=req.user)
    return render(req, 'pages/settings.html', {"profile": profile})

@login_required
def profile(req):
    recipes = [
        {
            "id": 1,
            "name": 'Fried rice', 
            "picture": "images/recettes/rs.png", 
            "is_private": True
        },
        {
            "id": 1,
            "name": 'Hamburger', 
            "picture": "images/recettes/h.png", 
            "is_private": False
        },
        {
            "id": 1,
            "name": 'Crescent', 
            "picture": "images/recettes/c.png", 
            "is_private": False},
        {
            "id": 1,
            "name": 'Crescent', 
            "picture": "images/recettes/c.png", 
            "is_private": True
        },
        {
            "id": 1,
            "name": 'Crescent', 
            "picture": "images/recettes/c.png", 
            "is_private": False
        },
    ]


    profil = Profile.objects.get(user=req.user)
    is_recipe_page = False
    if 'tab' in req.GET and req.GET['tab'] == 'recipes':
        is_recipe_page = True

    if req.method == 'POST':
        form = EditProfileForm(req.POST, req.FILES, instance=profil)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('landing')
        else:
            return redirect('accounts:settings')
    else:
        form = EditProfileForm(instance=profil)

    return render(req, 'pages/profile/index.html', {"recipes": recipes, "is_recipe_page": is_recipe_page, "form": form, "profile": profil})

def translate(language):
    cur_lang = get_language()
    try:
        activate(language)
    finally: 
        activate(cur_lang)

def downloadList(req):
    tmp_path = 'pdf/userList.html'
    users = Profile.objects.all()
    context = {'profiles': users}

    resp = HttpResponse(content_type='application/pdf')
    resp['Content-Disposition'] = 'filename="report.pdf"'

    tmp = get_template(tmp_path)
    html = tmp.render(context)

    pisa_status = pisa.CreatePDF(html, dest=resp,)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre> ' + html + '</pre>')
    return resp