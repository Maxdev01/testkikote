from django.urls import path
from . import views


urlpatterns = [
    path('tout-ev-itilizate-nou-yo', views.ListTextes ,name="alltextes"),
    path('lis-teks-nan-kategori/<categ>', views.ListTextes, name="bycateg"),
    path('detay-sou-text-lan/<int:id>/', views.DetailTexte, name="detailtextes"),
    path('article-dans-la-categorie/<catego>', views.Allposts, name='onecatego'),
    path('liste-de-nos-articles', views.Allposts, name="artposts" ),
    path('details-sur-l-article/<int:id>/', views.DetailsArticle, name='detailarticle'), 
     
]