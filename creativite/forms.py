from django import forms
from .models import Commentaire


class CommentForm(forms.ModelForm):
    class Meta:
        model =  Commentaire
        fields = ('name','body',)

        widgets = {
            'name' : forms.TextInput(attrs={'id': 'inputnamecoms', 'placeholder':'votre pseudo '} ),
            'body' : forms.Textarea(attrs={'id':'inputcomment', 'placeholder': 'votre commenter'}),
        }