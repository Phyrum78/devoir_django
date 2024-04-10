from django.shortcuts import render, redirect
from .models import Recette

# Create your views here.

def index(request):
    recettes = Recette.objects.all()
    context = {
        'recettes': recettes,
    }
    return render(request, 'index.html', context=context)

def recette_detail(request, recette_id):
    recette = Recette.objects.get(id=recette_id)
    context = {
        'recette': recette,
    }
    return render(request, 'Recettes/detailsRecettes.html', context=context)

def create_recette(request):
    if request.method == 'POST':
        nomRecette = request.POST.get('nomRecette')
        ingredients = request.POST.get('ingredients')
        etapes = request.POST.get('etapes')
        author = request.POST.get('author')
        imageURL = request.POST.get('imageURL')
        notes = request.POST.get('notes')

        new_recette = Recette(
            nomRecette=nomRecette,
            ingredients=ingredients,
            etapes=etapes,
            author=author,
            imageURL=imageURL,
            notes=notes
        )
        new_recette.save()

        return redirect('home_index')

    return render(request, 'Recettes/createRecettes.html')