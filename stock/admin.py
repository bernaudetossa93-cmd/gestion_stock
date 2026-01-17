from django.contrib import admin
from .models import Produit


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):


    list_display = ['nom', 'categorie', 'quantite', 'prix', 'stock_bas']
    list_filter = ['categorie']
    search_fields = ['nom', 'description']
