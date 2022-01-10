from django.shortcuts import render , redirect , get_object_or_404
from django.db.models.fields import files
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from archives.models import PlaceCategory , ArchivesPlace
from .models import Profile , JobPerso , JobEntreprise , ProjectUser, Category
from portefolio.forms import ProfileForm , JobEntrepriseForm , ProjectForm
from .forms import JobPersoForm 
from django.core.paginator import Paginator , EmptyPage

# Create your views here.

# sa se paj index lan 
def index(request, catego=None):
    most_visit = ArchivesPlace.objects.all().order_by("-views")[:5]
    work = JobPerso.objects.all()
    categories = PlaceCategory.objects.all()
    places = ArchivesPlace.objects.all().order_by("-created")


    if catego:
        places = places.filter(categorie__slug=catego)

    pg = Paginator(places, 10)
    nbr_page = request.GET.get('page', 1)
    try:
        page = pg.page(nbr_page)

    except EmptyPage:
        page = pg.page(1)

    context = {'work': work, 'categories' : categories , 'places': places ,
                 'places': page, 'most_visit': most_visit}
                
    return render(request, 'index.html', context )

    
# pati sa se pouw ka we potfolio yon user
def detailPotfo(request, id=None):
    potfos = get_object_or_404(ProjectUser, id=id)
    potfos.eyes = potfos.eyes + 1
    potfos.save()

    context = {'potfo': potfos}
    return render(request, 'portefolio/detailpotfos.html', context)

def profilDetail(request, id=None):
    user = get_object_or_404(User,  id=id)
    myprofil = get_object_or_404(Profile, user=user)

    potfolio_list = user.projects.all()

    konteks = {'myprofil': myprofil, 'potfolio_list': potfolio_list}
    return render(request, 'profil-detail.html', konteks)

def detailArchive(request, id=None):

    details = get_object_or_404(ArchivesPlace, id=id)

    context = {'details': details }

    return render(request, 'archives/detailscompany.html', context)


# page sa ap pemet ou we tout user yo
# tout sa ki enskri sou platform lan

def listUser(request):
    allcategory = Category.objects.all()
    userproject = ProjectUser.objects.all()
    users = User.objects.all()

    # tout potfolio yo
    allportefolio = ProjectUser.objects.all()

    # pou paginate paj nou yo
    pg = Paginator(users, 20)
    nb_paj = request.GET.get('page', 1)

    try:
        page = pg.page(nb_paj)

    except EmptyPage:
        page = p.page(1)

    

    if 'q' in request.GET:
        q = request.GET['q']
        allportefolio = ProjectUser.objects.filter(name__icontains=q)
    else:
        allportefolio = ProjectUser.objects.all()



    konteks = {'user': page, 'allcategory': allcategory,
                'userproject': userproject, 'allportefolio': allportefolio}
    return render(request, 'all-user.html', konteks)

# lap ka mete profil si selman li konekte
@login_required(login_url='connexion')
def modifProfil(request):
    if request.method == "POST": # pouw pran done nan fomile an
        formprofil = ProfileForm(data=request.POST, files= request.FILES)
        if formprofil.is_valid(): # si reket lan valide

            mypro = request.user.profile 
            mypro.name = request.POST.get('name')
            mypro.last_name = request.POST.get('last_name')
            mypro.photo = request.FILES.get('photo')
            mypro.email = request.POST.get('email')
            mypro.description = request.POST.get('description')
            mypro.school = request.POST.get('school')
            mypro.universite = request.POST.get('universite')
            mypro.profesional_school = request.POST.get('profesional_school')
            mypro.ville = request.POST.get('ville')




            
            mypro.save()
            return redirect("dash")

        else:
            print("profil ou an pa save")

    else:
        formprofil = ProfileForm()
    konteks = {'formprofil': formprofil}
    return render(request, 'profil-modifye.html', konteks)


def jobList(request):
    return render(request, 'travay-list.html')

def jobUser(request):
    if request.method == "POST":
        jobform = JobPersoForm(data=request.POST)
        if jobform.is_valid():
            jobform.cleaned_data.get("title")
            jobform.cleaned_data.get("description")
            jobform.cleaned_data.get("categorie")
            jobform.cleaned_data.get("ville")
            jobform.cleaned_data.get("email")
            jobform.cleaned_data.get("phone_1")
            jobform.cleaned_data.get("phone_2")
            jobform.cleaned_data.get("date_to")

            job = jobform.save(commit=False)
            job.user = request.user
            job.save()
            jobform.save_m2m()

            return redirect("dash")

        else:
            print("ou pa mete yon bagay gade byen")

    else:
        jobform = JobPersoForm()

    konteks = {'jobform': jobform}
    return render(request, 'formjobuser.html', konteks)
            

# le yon antreprise ap bay travay

@login_required(login_url='connexion')
def antreprizJob(request):
    if request.method == "POST":
        myform = JobEntrepriseForm(data=request.POST , files=request.FILES)

        if myform.is_valid():
            myform.cleaned_data.get("name")
            myform.cleaned_data.get("title")
            myform.cleaned_data.get("description")
            myform.cleaned_data.get("categorie")
            myform.cleaned_data.get("date_to")
            myform.cleaned_data.get("email")
            myform.cleaned_data.get("ville")
            myform.cleaned_data.get("adresse")
            myform.cleaned_data.get("phone_1")
            myform.cleaned_data.get("phone_2")

            form = myform.save(commit=False)
            form.user = request.user
            form.save()
            myform.save_m2m()
            return redirect("dash")

        else:
            print('fomile an mal ranpli')

    else:
        myform = JobEntrepriseForm()
    konteks = {'myform': myform}

    return render(request, 'form-entreprise.html', konteks)


def detailJob(request, id=None):
    detail_work = get_object_or_404(JobPerso, id=id)
    detail_work.view = detail_work.view + 1
    detail_work.save()

    
    context = {'detail_work': detail_work}

    return render(request, 'detail-job.html', context)


# project for these user on the platform
# login_required the user must login 
# use m2m after you save the project
# let's go

@login_required(login_url='connexion')
def projectUser(request):

    if request.method == "POST":
        myform = ProjectForm(data= request.POST)

        if myform.is_valid():
            myform.cleaned_data.get('name')
            myform.cleaned_data.get('categorie')
            myform.cleaned_data.get('description')
            myform.cleaned_data.get('experience')
            myform.cleaned_data.get('phone')
            myform.cleaned_data.get('mail')

            mypro = myform.save(commit=False)
            mypro.user = request.user
            mypro.save()

            myform.save_m2m()

            return redirect("dash")

        else:
            print("projet an pa save")

    else:
        myform = ProjectForm()

    context = {'myform': myform}
    return render(request, 'formproject.html', context)


# pati sa se pou user an ka fe prop potfolio li
# epi efase li sil vle


@login_required(login_url='connexion')
def viewpotfolio(request):
    mypotfolios = request.user.projects.all()
    # varyab sa gen tout potfolio user sat

    context = {'mypotfolios': mypotfolios}

    return render(request, 'potfolio/potfolio-user.html', context)


#pou efase yon potfolio
# fok moun lan konekte
@login_required(login_url='connexion')
def delpotfolio(request, id=None):

    ProjectUser.objects.get(id=id).delete()
    return redirect('mypotfolios')


def about(request):
    return render(request, 'aboutus.html')