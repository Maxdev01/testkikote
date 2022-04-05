from django.shortcuts import render, redirect , get_object_or_404
from .models import CreationCategories , Texte , categoriesPost, ArticlePost
from django.core.paginator import Paginator , EmptyPage
from django.views.generic import ListView
from .forms import CommentForm
from django.db.models import Q


# Create your views here.

def ListTextes(request ,categ=None):
    # teks yo li plis yo 
    more_read = Texte.objects.all().order_by("-view")[:5]
    all_posts = Texte.objects.filter(status=True).order_by("-date")

    if 'q' in request.GET:
        rep = request.GET['q']
        all_posts = Texte.objects.filter(Q(author__icontains=rep) | Q(title__icontains=rep))

    else:
        all_posts = Texte.objects.filter(status=True).order_by('-date')

    all_categs = CreationCategories.objects.all()

    if categ:
        all_posts = all_posts.filter(categorie__slug=categ)


    pg = Paginator(all_posts, 12)
    nb_paj = request.GET.get('page', 1)

    try:
        page = pg.page(nb_paj)
    except EmptyPage:
        page = p.page(1)


    

    context = {'all_posts': all_posts, 'more_read':  more_read, 'all_categs': all_categs, 
               'all_posts': page }

    return render(request, 'creative/alltext.html', context)

def DetailTexte(request, id=id):
    detail_texts = get_object_or_404(Texte, id=id)
    detail_texts.view = detail_texts.view +1 
    detail_texts.save()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.post = detail_texts
            c.save()
    
    form = CommentForm

    context ={
        'detail_texts': detail_texts,
        'form': form
    }

    return render(request, 'creative/details.html', context)



def Allposts(request, catego=None):
    all_articles = ArticlePost.objects.all()

    all_category = categoriesPost.objects.all()
    if catego:
        all_articles = all_articles.filter(category__slug=catego)
    
    all = None
    
    if all_articles:
        p = Paginator(ArticlePost.objects.all(), 2)
        page = request.GET.get('page')
        all = p.get_page(page)

    
    
        
    context = {'all_articles' : all_articles,  'all_category': all_category, 'all' : all,}

    return render(request, 'article/posts.html', context)


# class ArticlePostListView(ListView):
#     model = ArticlePost
#     ordering = ['id']
#     template_name = 'article/posts.html'
#     paginate_by = 3
#     #queryset = ArticlePost.objects.all()