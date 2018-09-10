from django import forms
from .models import Link


class LinkForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(attrs={
        'id': 'input_text', 'class': 'url',
        'name': 'url',
        'placeholder': 'Enter url video from youtube.com'
    }))

    class Meta:
        model = Link
        fields = "__all__"