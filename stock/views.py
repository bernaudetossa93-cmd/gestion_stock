from django.http import HttpResponse


def accueil(request):
    return HttpResponse("Bienvenue dans le gestionnaire de stock !")


from django.shortcuts import render
from .models import Produit


def liste_produits(request):
    produits = Produit.objects.all()

    # Récupérer les paramètres de recherche (GET)
    recherche = request.GET.get('recherche', '')
    categorie = request.GET.get('categorie', '')

    # Appliquer les filtres
    if recherche:
        produits = produits.filter(nom__icontains=recherche)
    if categorie:
        produits = produits.filter(categorie=categorie)

    # Liste des catégories pour le dropdown
    categories = Produit.objects.values_list('categorie', flat=True).distinct()

    return render(request, 'stock/liste.html', {
        'produits': produits,
        'categories': categories,
        'recherche': recherche,
        'categorie_selectionnee': categorie,
    })


from django.shortcuts import render
from django.db.models import Sum, Avg, Count, F
from .models import Produit


def statistiques(request):
    produits = Produit.objects.all()

    stats = {
        'total_produits': produits.count(),
        'total_articles': produits.aggregate(Sum('quantite'))['quantite__sum'] or 0,
        'valeur_stock': sum(p.valeur_stock() for p in produits),
        'prix_moyen': produits.aggregate(Avg('prix'))['prix__avg'] or 0,
        'produits_stock_bas': produits.filter(quantite__lt=F('seuil_alerte')).count(),
        'par_categorie': produits.values('categorie').annotate(
            count=Count('id'),
            total_quantite=Sum('quantite')
        ).order_by('-count'),
    }

    return render(request, 'stock/statistiques.html', {'stats': stats})


from django.shortcuts import get_object_or_404, redirect
from .models import Produit


def ajuster_stock(request, pk, action):
    produit = get_object_or_404(Produit, pk=pk)

    if action == 'plus':
        produit.quantite += 1
    elif action == 'moins' and produit.quantite > 0:
        produit.quantite -= 1

    produit.save()
    return redirect('liste_produits')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produit
from .forms import ProduitForm


def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit ajouté avec succès !')
            return redirect('liste_produits')
    else:
        form = ProduitForm()

    return render(request, 'stock/formulaire.html', {
        'form': form,
        'titre': 'Ajouter un produit'
    })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produit
from .forms import ProduitForm


def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)

    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, f'Produit "{produit.nom}" modifié !')
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)

    return render(request, 'stock/formulaire.html', {
        'form': form,
        'titre': f'Modifier : {produit.nom}'
    })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produit


def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)

    if request.method == 'POST':
        nom = produit.nom
        produit.delete()
        messages.success(request, f'Produit "{nom}" supprimé !')
        return redirect('liste_produits')

    return render(request, 'stock/confirmer_suppression.html', {
        'produit': produit
    })
