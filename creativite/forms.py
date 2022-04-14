
from django import forms
from .models import Commentaire , Reply


class CommentForm(forms.ModelForm):
    class Meta:
        model =  Commentaire
        fields = ('name','body',)

        widgets = {
            'name' : forms.TextInput(attrs={'id': 'inputnamecoms', 'placeholder':'votre pseudo '} ),
            'body' : forms.Textarea(attrs={'id':'inputcomment', 'placeholder': 'Votre commentaire '}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name','body',)

        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Votre nom '} ),
            'body' : forms.Textarea(attrs={'placeholder': 'Votre commentaire ..........'}), 
        }