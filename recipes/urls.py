from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.all_recipes, name='all'),
    path('favorites', views.favorites_recipes, name='favorites'),
    path('add_recipe', views.add_recipe, name='add'),
    path('<int:id>', views.one_recipe, name='one'),
]