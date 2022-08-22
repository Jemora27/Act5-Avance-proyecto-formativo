# Generated by Django 4.1 on 2022-08-22 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_brand_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='Cantidad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='diameter',
            field=models.CharField(blank='True', max_length=150, null='True', verbose_name='Diametro'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.CharField(blank='True', max_length=150, null='True', verbose_name='Material'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank='True', max_length=150, null='True', verbose_name='Tamaño'),
            preserve_default='True',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
