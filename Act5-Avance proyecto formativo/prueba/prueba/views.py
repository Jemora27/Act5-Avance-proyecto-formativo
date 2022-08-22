from django.shortcuts import render

#Index

def index(request):
    return render (request, 'index.html', {
        
    })

#Categorias index

def bio(request):
    return render (request, 'cbio.html', {

    })

def bag(request):
    return render (request, 'cbolsas.html', {

    })

def clutery(request):
    return render (request, 'ccubiertos.html', {

    })

def packing(request):
    return render (request, 'cempaques.html', {

    })

def plates(request):
    return render (request, 'cplatos.html', {

    })

def cups(request):
    return render (request, 'cvasos.html', {

    })

def some(request):
    return render (request, 'cvarios.html', {

    })

#Interfaz cliente

def clien(request):
    return render (request, 'InterClien.html', {

    })

#Categorias Cliente

def bio_clien(request):
    return render (request, 'cbioc.html', {
        
    })

def bag_clien(request):
    return render (request, 'cbolsasc.html', {

    })

def clutery_clien(request):
    return render (request, 'ccubiertosc.html',{

    })

def packing_clien(request):
    return render (request, 'cempaquesc.html', {

    })

def plates_clien(request):
    return render (request, 'cplatosc.html', {

    })

def cups_clien(request):
    return render (request, 'cvasosc.html', {

    })

def some_clien(request):
    return render (request, 'cvariosc.html', {

    })

#Calificacion servicios

def qualification(request):
    return render (request, 'cal.html', {

    })

def success_quali(request):
    return render (request, 'exitocal.html', {

    })

#Perfil cliente

def profile(request):
    return render (request, 'perfil.html', {

    })

#Compras de clientes

def info_ped(request):
    return render (request, 'infoped.html', {

    })

def buy(request):
    return render (request, 'contcom.html', {

    })

def success(request):
    return render (request, 'exito.html', {

    })

#Interfaz administrador

def admin(request):
    return render (request, 'InterAdmin.html', {

    })

#Procesos

#Inventario
def enter_products(request):
    return render (request, 'Iv2.html', {

    })

def list_products(request):
    return render (request, 'listaProductos.html', {

    })

def delete_product(request):
    return render (request, 'confirmacionprod.html', {

    })


#Registro de ventas

def register_sale(request):
    return render (request, 'FormularioRegistro.html', {

    })

def register_table(request):
    return render (request, 'TablaRV.html', {

    })

def register_order(request):
    return render (request, 'Informacion de pedido.html', {

    })

#Gestion de compras

def purchase_table(request):
    return render (request, 'gestionCotab.html', {

    })

def make_purchase(request):
    return render (request, 'gestionCo.html', {

    })

#Busqueda de usuarios

def user(request):
    return render (request, 'buscar.html', {

    })

def confirmation(request):
    return render (request, 'confirmacion.html', {

    })

#Edicion de categorias

def edit_cat(request):
    return render (request, 'editcat.html', {

    })

def edit_cat_tab(request):
    return render (request, 'editcatrab.html', {

    })

def delete_cat(request):
    return render (request, 'confirmacioncat.html', {

    })