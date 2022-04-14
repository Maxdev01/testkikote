from builtins import print
from cgitb import reset
from hashlib import algorithms_available
from unittest import result
from django.shortcuts import render, redirect , get_object_or_404
from .models import CreationCategories , Texte , categoriesPost, ArticlePost, Reply, UserIp, UserIpText
from django.core.paginator import Paginator , EmptyPage
from django.views.generic import ListView
from .forms import CommentForm, ReplyForm
from django.db.models import Q

# hitcount for ip adress
#from hitcount.views import HitCountDetailView 


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
        'form': form,
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

# pati sa se pou detay sou chak atik
# ladan ap gen 
# -- commentaire 
# -- kantite fwa yo we 
# -- django social share 
# -- epi tout detay yo 

def DetailsArticle(request, id=id):
    d = get_object_or_404(ArticlePost, id=id)
    d.views = d.views + 1
    d.save()

    if request.method == 'POST':
        formreply = ReplyForm(request.POST)
        if formreply.is_valid():
            c = formreply.save(commit=False)
            c.articles = d
            c.save()
    
    # fonksyon pou nou we nombre vizite yo
    def get_ip(request):
        adress = request.META.get('HTTP_X_FOWARDED_FOR')

        if adress:
            ip = adress.slit(',')[1].strip()

        else:
            ip = request.META.get('REMOTE_ADDR')
            return ip
    ip = get_ip(request)
    u = UserIp(user=ip)
    print(ip)

    result = UserIp.objects.filter(Q(user__icontains=ip))

    if len(result) == 1:
        print('user exist ')
        

    
    elif len(result) > 10:
        print('user exit more....')
    else:
        u.save()
        print('user is unique')
    
    

    countip = UserIp.objects.all().count()
    

    formreply = ReplyForm

    context = {'d': d, 'formreply': formreply, 'countip': countip }
    return render(request, 'article/details.html', context)



# class PostDetailView(HitCountDetailView):
#     model = ArticlePost
#     template_name = 'article/details.html'
#     slug_field = 'slug'
#     count_hit = True



# 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