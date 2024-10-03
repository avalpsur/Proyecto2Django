from django.contrib import admin
from .models import Libro
from .models import Empleado
from .models import Revista

# Register your models here.

admin.site.register(Libro)
admin.site.register(Empleado)
admin.site.register(Revista)

