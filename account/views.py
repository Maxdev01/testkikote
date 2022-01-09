from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout 
from account.forms import UserForm 
from portefolio.models import Profile

# Create your views here.


def dashboard_paj(request):
    return render(request, 'dashboard.html')



def enskripsyon(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            myuser = form.save(commit=False)
            myuser.set_password(data.get('password'))
            myuser.save()
            profil_user_auto = Profile(user=myuser, name="vid", last_name='vid',phone='123456', email='kikote@gmail.com', description='vid',
                                        school="vid", universite="vid", profesional_school="vid", ville="vid")

            profil_user_auto.save()

            return redirect("firststep")

        else:
            print("kont ou an pa sovgade")
        
    else:
        form = UserForm()
    context = {'form': form}

    return render(request, 'enskri.html', context)


def koneksyon_user(request):

    if request.method == "POST":
        data = request.POST    
        myform = authenticate(request, username=data['username'], password=data['password'])

        if myform is not None:
            login(request, myform)
            return redirect("dash")

        else:
            print("Vous n'avez pas de compte")
            myform = UserForm()
            context = {'myform': myform}
            messages.error(request, 'Verifiez vos informations')
            return render(request, 'konekte.html', context)
    else:
        myform = UserForm()
    
    konteks = {"myform": myform}
    return render(request, 'konekte.html', konteks)

# fonksyon sa pemet ou moun lan dekonekte 
def dekonekte_user(request):
    logout(request)
    return redirect("firststep")


#email = models.EmailField(max_length=100,null=True, blank=True)

#email='kikote@gmail.com',