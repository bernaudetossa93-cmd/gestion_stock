from django import forms
from .models import Produit


class ProduitForm(forms.ModelForm):


    class Meta:
        model = Produit
        fields = ['nom', 'description', 'quantite', 'prix',
          'categorie', 'seuil_alerte']
        widgets = {
    'nom': forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Nom du produit'
    }),
    'description': forms.Textarea(attrs={
        'class': 'form-input',
        'rows': 3
    }),
    'quantite': forms.NumberInput(attrs={
        'class': 'form-input',
        'min': 0
    }),
    'prix': forms.NumberInput(attrs={'class': 'form-input',
'step': '0.01',
'min': 0
}),
'categorie': forms.TextInput(attrs={
'class': 'form-input',
'placeholder': 'Ex: Électronique'
}),
'seuil_alerte': forms.NumberInput(attrs={
'class': 'form-input',
'min': 0
}),
}
