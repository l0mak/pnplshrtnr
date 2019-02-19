from django import forms

from .validators import url_validate

class SubmitURLForm(forms.Form):
    url = forms.CharField(
                    label='', 
                    validators=[url_validate],
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': 'Improperly long URL',
                            'class': 'form-control'
                        }
                    )
                )
