from django.urls import path

from django.contrib.auth import views as auth
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth.LoginView.as_view(template_name='auth_pages/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth.LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('downloadlist', views.downloadList, name='download')
]