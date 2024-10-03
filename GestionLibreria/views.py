from django.shortcuts import render
from .models import Libro
from .models import Empleado
from .models import Revista

# Create your views here.
def menu(request):
    return render(request,'GestionLibreria/menu.html',{})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request,'GestionLibreria/lista_libros.html',{'mostrar_libros': libros})

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request,'GestionLibreria/lista_empleados.html',{'mostrar_empleados': empleados})


def lista_revistas(request):
    revistas = Revista.objects.all()
    return render(request,'GestionLibreria/lista_revistas.html',{'mostrar_revistas': revistas})
