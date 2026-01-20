# Gestionnaire de Stock – Application Django

Application web de gestion de stock développée avec Django.
Elle permet de gérer des produits, suivre les quantités disponibles, effectuer des recherches et consulter des statistiques globales.

Ce projet a été réalisé dans un cadre pédagogique, avec une structure et des pratiques proches d’un projet professionnel, afin de servir de base évolutive pour une application métier.

---

## Présentation du projet

Le gestionnaire de stock permet :

* La gestion complète des produits
* Le suivi des niveaux de stock
* L’identification des produits en seuil critique
* L’analyse des données via un tableau de bord

Le projet respecte l’architecture MVT (Model – View – Template) de Django et utilise l’ORM pour l’accès aux données.

---

## Fonctionnalités

* Ajout, modification et suppression de produits
* Recherche de produits par nom
* Filtrage par catégorie
* Gestion des seuils d’alerte de stock
* Ajustement rapide des quantités
* Tableau de bord statistique :

  * Nombre total de produits
  * Quantité totale en stock
  * Valeur totale du stock
  * Nombre de produits en stock bas
  * Répartition des produits par catégorie
* Interface d’administration Django

---

## Technologies utilisées

* Python 3
* Django 5
* HTML5
* CSS3
* SQLite (base de données par défaut)
* Git et GitHub

---

## Structure du projet

```
gestion_stock/
├── config/                Configuration principale du projet
├── stock/                 Application métier
│   ├── models.py          Modèles de données
│   ├── views.py           Logique métier
│   ├── forms.py           Formulaires Django
│   ├── urls.py            Routage de l’application
│   └── templates/stock/   Templates HTML
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation et exécution en local

### Prérequis

* Python 3.10 ou plus
* Git

### Étapes d’installation

Cloner le dépôt :

```bash
git clone https://github.com/TON_USERNAME/gestion_stock.git
cd gestion_stock
```

Créer et activer un environnement virtuel :

```bash
python -m venv venv
```

Sous Windows :

```bash
venv\Scripts\activate
```

Sous Linux ou macOS :

```bash
source venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Appliquer les migrations :

```bash
python manage.py makemigrations
python manage.py migrate
```

Créer un compte administrateur :

```bash
python manage.py createsuperuser
```

Lancer le serveur :

```bash
python manage.py runserver
```

Accès à l’application :

* Application : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Administration : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Bonnes pratiques mises en œuvre

* Séparation claire des responsabilités (MVT)
* Utilisation des ModelForms
* Validation des données côté serveur
* Code structuré et lisible
* Templates réutilisables
* Utilisation des outils standards de Django

---

## Évolutions possibles

* Authentification et gestion des rôles utilisateurs
* Historique des mouvements de stock
* Export des données (PDF, Excel)
* API REST avec Django REST Framework
* Tests unitaires et fonctionnels
* Déploiement sur un serveur de production

---

## Contribution

Les contributions sont acceptées.

Processus recommandé :

1. Fork du dépôt
2. Création d’une branche dédiée
3. Commit clair et documenté
4. Soumission d’une Pull Request

---

## Auteur

Junior
Étudiant en ingénierie
Développement logiciel
Bénin

---

## Licence

Projet open-source à vocation pédagogique.
Utilisation libre avec attribution.
