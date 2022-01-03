from .models import CreationCategories

# pati sa se li kap pemet mwen jwenn tout texte ki  anndan yon kategorie

def list_categories(request):
    all_ = CreationCategories.objects.all()

    return {'my_categorie': all_[:5], 'all_categoory': all_}