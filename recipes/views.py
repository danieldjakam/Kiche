from django.shortcuts import redirect, render, get_object_or_404
from .models import Recipe

# Create your views here.
def all_recipes(req):
    return render(req, 'pages/list_recipes.html', {})

def favorites_recipes(req):
    return render(req, 'pages/favorites.html', {})

def add_recipe(req):

    is_finish_action = False
    fields = {
        "name": '',
        "description": '',
        "nbre_of_plates": '',
        "time_preparation": '',
        "time_cuisson": '',
        "status": '',
    }

    if 'action' in req.GET and req.GET['action'] == 'finish' and 'recipe' in req.GET and req.GET['recipe'] != '':
        is_finish_action = True
        beginned_recipe = get_object_or_404(Recipe, pk=req.GET['recipe'])

        fields = {
            "ingredients": '',
            "preparation_step": '',
            "cuisson_step": '',                
        }

        if req.method == 'POST':
            errors = []

            ingredients = req.POST['ingredients']
            preparation_step = req.POST['preparation_step']
            cuisson_step = req.POST['cuisson_step']

            fields = {
                "ingredients": ingredients,
                "preparation_step": preparation_step,
                "cuisson_step": cuisson_step,                
            }

            if not ingredients or ingredients.__len__() < 3 :
                errors.append('invalid ingredients')
            elif not preparation_step or preparation_step.__len__() < 3 :
                errors.append('invalid preparation step')
            elif req.FILES.__len__() < 1:
                errors.append('Image necessaire')    

            if errors:
                return render(req, 'pages/add_recipe.html', {"is_finish_action": is_finish_action, "errors": errors, "fields": fields})
            else:
                
                recipe = Recipe.objects.get(pk=req.GET['recipe'])
                recipe.ingredients = ingredients
                recipe.preparation_step = preparation_step       
                recipe.picture = req.FILES['picture'] 
                
                if cuisson_step:
                    if cuisson_step.__len__() < 10:
                        errors.append('Invalid cuisson step')
                    else:
                        recipe.cuisson_step = cuisson_step

                if errors:
                    return render(req, 'pages/add_recipe.html', {"is_finish_action": is_finish_action, "errors": errors, "fields": fields})
                else:
                    recipe.save()
                    return redirect(f'landing')

        return render(req, 'pages/add_recipe.html', {"is_finish_action": is_finish_action, "recipe": beginned_recipe})

    if req.method == 'POST':
        errors = []

        name = req.POST['name']
        description = req.POST['description']
        nbre_of_plates = req.POST['nbre_of_plates']
        time_preparation = req.POST['time_preparation']
        time_cuisson = req.POST['time_cuisson']
        status = req.POST['status']

        fields = {
            "name": name,
            "description": description,
            "nbre_of_plates": nbre_of_plates,
            "time_preparation": time_preparation,
            "time_cuisson": time_cuisson,
            "status": status,
        }

        if not name or name.__len__() < 3 :
            errors.append('invalid name')
        elif not nbre_of_plates or not nbre_of_plates.isdigit() or int(nbre_of_plates) < 1  :
            errors.append('invalid number of plates')
        elif not time_preparation or not time_preparation.isdigit() or int(time_preparation) < 5:
            errors.append('invalid time preparation')
        elif not status or status.__len__() < 3 :
            errors.append('invalid status')
            
        if errors:
            return render(req, 'pages/add_recipe.html', {"is_finish_action": is_finish_action, "errors": errors, "fields": fields})
        else:
            
            recipe = Recipe()
            recipe.name = name
            recipe.creator = req.user
            recipe.nbre_of_plates = int(nbre_of_plates)
            recipe.time_preparation = int(time_preparation)
            recipe.status = status

            if description:
                if description.__len__() < 10:
                    errors.append('Invalid description')
                else:
                    recipe.description = description
                    
            if time_cuisson:
                if not time_cuisson.isdigit() or int(time_cuisson) < 10:
                    errors.append('Invalid time cuisson')
                else:
                    recipe.time_cuisson = int(time_cuisson)

            if errors:
                return render(req, 'pages/add_recipe.html', {"is_finish_action": is_finish_action, "errors": errors, "fields": fields})
            else:
                recipe.save()
                recipe_id = recipe.id
                return redirect(f'/recipes/add_recipe?action=finish&recipe={recipe_id}')

    return render(req, 'pages/add_recipe.html', {"is_finish_action": is_finish_action, "fields": fields})

def one_recipe(req, id):
    recipe = Recipe.objects.get(pk=id)
    return render(req, 'pages/see_recipe.html', {'recipe' : recipe})