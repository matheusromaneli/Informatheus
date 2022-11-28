from django import forms

from produto.models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('nome', 'imagem', 'valor', 'desconto') 
        localized_fields = ('valor',)

    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={
            'required': "Campo obrigatório",
            'unique': "Já existe"
        }

        self.fields['valor'].error_messages={
            'required': "Campo obrigatório"
        }

        self.fields['desconto'].error_messages={
            'required': "Campo obrigatório",
            'max_value': "Insira um valor entre 0 e 100",
            'min_value': "Insira um valor entre 0 e 100"
        }
        self.fields['desconto'].widget=forms.TextInput(attrs={
            'onkeypress':'return event.charCode >= 48 && event.charCode <= 57'
        })
