from django.urls import path
from . import views


urlpatterns = [
    path('',views.menu, name='menu'),
    path('libros',views.lista_libros, name='lista_libros'),
    path('empleados',views.lista_empleados, name='lista_empleados'),
    path('revistas',views.lista_revistas,name='lista_revistas'),
]
