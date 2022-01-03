
from django.shortcuts import render, redirect , get_object_or_404
from .models import ArchivesPlace, PlaceCategory
from django.core.paginator import Paginator , EmptyPage

# Create your views here.

# def detailArchive(request, id=None):

#     details = get_object_or_404(ArchivesPlace, id=id)

#     context = {'details': details }

#     return render(request, 'detailscompany.html', context)
