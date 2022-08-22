from tabnanny import verbose
from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    amount = models.IntegerField(verbose_name='Cantidad')
    material = models.CharField(max_length=150, verbose_name='Material', null='True', blank='True')
    size = models.CharField(max_length=150, verbose_name='Tamaño', null='True', blank='True')
    diameter = models.CharField(max_length=150, verbose_name='Diametro', null='True', blank='True')
    price = models.IntegerField(verbose_name='Precio')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']

