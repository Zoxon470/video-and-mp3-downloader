from django import forms
from .models import Link


class LinkForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(attrs={
        'id': 'input_text',
        'class': 'url',
        'placeholder': 'Enter url video from which you want to download mp3'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'email',
        'class': 'email',
        'placeholder': 'Enter your email address' }))

    class Meta:
        model = Link
        fields = "__all__"