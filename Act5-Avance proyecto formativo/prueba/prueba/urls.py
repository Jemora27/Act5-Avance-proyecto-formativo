"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('usuario/', views.user, name='user'),
    path('calificacion/', views.qualification, name='cal'),
    path('biodegradables/', views.bio, name='bio'),
    path('biodegradablesc/', views.bio_clien, name='bioc'),
    path('bolsas/', views.bag, name='bol'),
    path('bolsasc/', views.bag_clien, name='bolc'),
    path('cubiertos/', views.clutery, name='cubi'),
    path('cubiertosc/', views.clutery_clien, name='cubic'),
    path('cliente/', views.clien, name='InterClien'),
    path('admins/', views.admin, name='InterAdmin'),
    path('empaques/', views.packing, name='emp'),
    path('empaquesc/', views.packing_clien, name='empc'),
    path('platos/', views.plates, name='platos'),
    path('platosc/', views.plates_clien, name='platosc'),
    path('vasos/', views.cups, name='vasos'),
    path('vasosc/', views.cups_clien, name='vasosc'),
    path('varios/', views.some, name='varios'),
    path('variosc/', views.some_clien, name='variosc'),
    path('mi-perfil/', views.profile, name='perfil'),
    path('informacion-compras/', views.info_ped, name='infoped'),
    path('continuar-compra/', views.buy, name='contcom'),
    path('compra-realizada/', views.success, name='exito'),
    path('calificacion-relizada/', views.success_quali, name='exitocal'),
    path('ingresar-producto/', views.enter_products, name='Iv2'),
    path('productos/', views.list_products, name='list'),
    path('registrar-venta/', views.register_sale, name='reg'),
    path('ventas/', views.register_table, name='regtb'),
    path('registrar-pedido/', views.register_order, name='infped'),
    path('realizar-compra/', views.make_purchase, name='ges'),
    path('tabla-de-compras/', views.purchase_table, name='gestb'),
    path('agregar-categoria/', views.edit_cat, name='editcat'),
    path('categorias/', views.edit_cat_tab, name='editcatrab'),
    path('confirmacion-eliminar-categoria/', views.delete_cat, name='confcat'),
    path('confirmacion-eliminar-usuario/', views.confirmation, name='conf'),
    path('confirmacion-eliminar-producto/', views.delete_product, name='confprod'),
]
