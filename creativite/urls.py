from django.urls import path
from . import views


urlpatterns = [
    path('tout-ev-itilizate-nou-yo', views.ListTextes ,name="alltextes"),
    path('lis-teks-nan-kategori/<categ>', views.ListTextes, name="bycateg"),
    path('detay-sou-text-lan/<int:id>/', views.DetailTexte, name="detailtextes")
]