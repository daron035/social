from django import forms

from .models import *


class TweetsForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(
        attrs={
            "placeholder": "Tweet something...",
            "class": "textarea is-info is-medium",
        }),
        label="",)

    class Meta:
        model = Tweets
        exclude = ('user',)
