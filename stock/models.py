from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantite = models.PositiveIntegerField(default=0)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.CharField(max_length=50)
    seuil_alerte = models.PositiveIntegerField(default=5)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def stock_bas(self):
        return self.quantite < self.seuil_alerte

    def valeur_stock(self):
        return self.quantite * self.prix

    def __str__(self):
        return f"{self.nom} ({self.quantite} en stock)"

    class Meta:
        ordering = ['nom']
