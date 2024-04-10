from django.shortcuts import render
from GestionRecettes.models import Recette

def index(request):
    recettes = Recette.objects.all()
    context = {
        'recettes': recettes,
    }
    return render(request, 'index.html', context=context)

