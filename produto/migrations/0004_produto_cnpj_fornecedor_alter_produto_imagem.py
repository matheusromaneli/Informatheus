# Generated by Django 4.1.2 on 2022-11-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produto_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='cnpj_fornecedor',
            field=models.CharField(default='11111111111111', max_length=14),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='./static/images'),
        ),
    ]
