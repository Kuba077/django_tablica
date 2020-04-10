from django import forms


class UserLoginForm(forms.Form):
    login = forms.CharField(
        label="Twój login:",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    haslo = forms.CharField(
        label="Twoje hasło:",
        max_length=39,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'})
    )
