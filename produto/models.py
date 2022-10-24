from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=70, db_index=True, unique=True)
    slug = models.SlugField(max_length=70)
    imagem = models.CharField(max_length=70, blank=True)
    valor = models.DecimalField(max_digits=6,decimal_places=2)
    desconto = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    class Meta:
        db_table = 'produto'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
    