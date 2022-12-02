from itertools import cycle
from django import forms
from django.forms import ValidationError

from produto.models import Produto

class EditableProductForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('desconto',) 

    produto_id = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['desconto'].widget = forms.TextInput()
        self.fields['desconto'].widget.attrs.update({'style': 'width: 60px'})

        
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'cnpj_fornecedor', 'imagem', 'valor', 'desconto') 
        localized_fields = ('valor',)

    def clean_cnpj_fornecedor(self):
        cnpj = self.cleaned_data['cnpj_fornecedor']

        if len(cnpj) != 14:
            raise ValidationError("CNPJ inválido, tente novamente")

        if cnpj in (c * 14 for c in "1234567890"):
            raise ValidationError("CNPJ inválido, tente novamente")

        cnpj_r = cnpj[::-1]
        for i in range(2, 0, -1):
            cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
            dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
            if cnpj_r[i - 1:i] != str(dv % 10):
                raise ValidationError("CNPJ inválido, tente novamente")

        return cnpj

    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={
            'required': "Campo obrigatório",
            'unique': "Já existe"
        }

        self.fields['valor'].error_messages={
            'required': "Campo obrigatório"
        }
        self.fields['valor'].widget=forms.TextInput(attrs={
            'onkeypress':'return event.charCode >= 48 && event.charCode <= 57'
        })

        self.fields['desconto'].error_messages={
            'required': "Campo obrigatório",
            'max_value': "Insira um valor entre 0 e 100",
            'min_value': "Insira um valor entre 0 e 100"
        }
        self.fields['desconto'].widget=forms.TextInput(attrs={
            'onkeypress':'return event.charCode >= 48 && event.charCode <= 57'
        })

