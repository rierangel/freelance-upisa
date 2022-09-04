# Generated by Django 4.1 on 2022-09-04 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_categoria_remove_product_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sub_categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.categoriasub'),
            preserve_default=False,
        ),
    ]