from django.db import models
from django.core.validators import MinValueValidator
from produto.models import Produto

# Create your models here.
class Item(models.Model):
    product = models.ForeignKey(Produto, related_name='produtos', on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[
        MinValueValidator(1)
    ])

    class Meta:
        db_table = 'item'

    def __str__(self):
        return self.product.nome