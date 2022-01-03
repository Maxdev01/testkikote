from django import forms
from portefolio.models import Profile , JobEntreprise, JobPerso , ProjectUser
from django.core.exceptions import ValidationError

# class pou profile lan

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'last_name', 'photo','phone', 'email', 'description', 'school', 
                    'profesional_school', 'universite', 'ville')

class JobPersoForm(forms.ModelForm):
    class Meta:
        model = JobPerso
        fields = ('title', 'description', 'categorie', 'ville', 'email', 'phone_1', 'phone_2', 'date_to')
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder': 'KI SA OU BEZWEN  * ?'}),
            'description': forms.Textarea(attrs={'placeholder': 'eksplike sa ou genyen an'}),
            'categorie' : forms.SelectMultiple(attrs={'placeholder': 'NAN KI VIL OU YE ? ', 'class': 'categ-design'}),
            'ville' : forms.TextInput(attrs={'placeholder': 'NAN KI VIL OU YE ? '}),
            'email' : forms.TextInput(attrs={'placeholder' :'METE IMEL OU TANPRI '}),
            'phone_1': forms.TextInput(attrs={'placeholder': 'METE NUMERO TELEFON OU *'}),
            'phone_2': forms.TextInput(attrs={'placeholder': 'METE YON DEZYEM'}),
            'date_to': forms.TextInput(attrs={'placeholder': 'DAT LIMIT ? ANE-MWA-JOU  EKZANP - 2021-10-11'}),

        }

        def clean(self):

            cleanned_data = super().clean()

            title = cleanned_data.get('title')

            if "vole" in title:
                raise ValidationError("ou pa dwe ekri mo sa")



class JobEntrepriseForm(forms.ModelForm):
    class Meta:
        model = JobEntreprise
        fields = ('name', 'title', 'description', 'categorie', 'date_to', 'email', 'ville', 'adresse', 'phone_1', 'phone_2')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'KI NON ANTREPRIZ OU AN ? *'}),
            'title': forms.TextInput(attrs={'placeholder': 'KI SA OU BEZWEN ? *'}),
            'description': forms.Textarea(attrs={'placeholder': 'EKSPLIKASYON AK DETAY *'}),
            'categorie': forms.SelectMultiple(attrs={'placeholder': ''}),
            'date_to': forms.TextInput(attrs={'placeholder': 'DAT LIMIT ? (ANE-MWA-JOU) 2021-10-19 * '}),
            'email': forms.TextInput(attrs={'placeholder': 'IMEL ANTREPRIZ LAN *'}),
            'ville': forms.TextInput(attrs={'placeholder': 'NAN KI VIL ANTREPRIZ SA YE ? *'}),
            'adresse': forms.TextInput(attrs={'placeholder': 'ADRES ANTREPRIZ LAN ? '}),
            'phone_1': forms.TextInput(attrs={'placeholder': 'NIMERO TELEFON ANTREPRIZ LAN ? *'}),
            'phone_2': forms.TextInput(attrs={'placeholder': 'DEZYEM NIMERO TELEFON ANTREPRIZ LAN '}),


        }
class ProjectForm(forms.ModelForm):

    class Meta:
        model = ProjectUser
        fields = ('name', 'categorie', 'description', 'experience', 'phone', 'mail')