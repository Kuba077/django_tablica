from django import forms


class PostForm(forms.Form):
    tresc = forms.CharField(
        label="Treść:",
        max_length=1024
    )
