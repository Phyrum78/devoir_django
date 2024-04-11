from django.contrib import admin
from django.urls import path
from .views import index, recette_detail, create_recette, add_comment

urlpatterns = [
    path('', index, name="recette_index"),
    path('<int:recette_id>/', recette_detail, name='recette_detail'),
    path('createRecette/', create_recette, name='create_recette'),
    path('<int:recette_id>/addComment/', add_comment, name='add_comment'),
]