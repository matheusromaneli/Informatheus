from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=70, db_index=True)
    pages_used = models.CharField(max_length=70, db_index=True)
    short_description = models.CharField(max_length=70, db_index=True)

    class Meta:
        db_table = 'card'
        ordering = ('title',)

    def __str__(self):
        return self.title