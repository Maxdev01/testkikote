from django import path
from . import views 

urlpatterns = [
    path('detay-sou-achiv-lan/<int:id>/', views.detailArchive, name='detailscomp'),
]