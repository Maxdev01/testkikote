from django import forms
from .models import Commentaire


class CommentForm(forms.ModelForm):
    class Meta:
        model =  Commentaire
        fields = ('name','body',)

        widgets = {
            'name' : forms.TextInput(attrs={'id': 'inputnamecoms', 'placeholder':'Mete non ou '} ),
            'body' : forms.Textarea(attrs={'id':'inputcomment', 'placeholder': 'comments'}),
        }