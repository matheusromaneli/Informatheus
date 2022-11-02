from django import forms
from django import forms
from django.forms import TextInput


class QuantidadeForm(forms.Form):
    
    produto_id = forms.CharField(widget=forms.HiddenInput)

    quantidade = forms.IntegerField(
        min_value=0,
        max_value=99,
        widget=forms.TextInput(attrs={'class': 'form-control btn-secondary quantidade',
                                      'style': 'text-align: center; width:70px;',
                                      'readonly': 'readonly'}),
        required=True
    )
    