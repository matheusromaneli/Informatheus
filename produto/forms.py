from django import forms

from produto.models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('nome', 'imagem', 'valor', 'desconto') 

    nome = forms.CharField(
        error_messages={
            'required': "Campo obrigatório",
            'unique': "Já existe"
        }
    )    
    #Error message keys: 
    # required, 
    # invalid, 
    # max_value, 
    # min_value, 
    # max_digits, 
    # max_decimal_places, 
    # max_whole_digits, 
    # step_size
    valor = forms.DecimalField(
        error_messages={
            'required': "Campo obrigatório"
        }
    )

    desconto = forms.IntegerField(
        error_messages={
            'required': "Campo obrigatório",
            'max_value': "Insira um valor entre 0 e 100",
            'min_value': "Insira um valor entre 0 e 100"
        }
    )