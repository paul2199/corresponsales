from django.contrib import admin
from apirest.models import *
# Register your models here.
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display=['id','title']

@admin.register(propietario)
class propietario(admin.ModelAdmin):
    list_display=['codigo','nombre','apellido','cedula','usuario','contrasena']

@admin.register(cobros)
class cobros(admin.ModelAdmin):
    list_display=['codigo','codigo_factura','fecha','valor','adjunto_foto','fecha_anulacion','codigo_corresponsales','codigo_estado']

@admin.register(corresponsales)
class corresponsales(admin.ModelAdmin):
    list_display=['codigo','codigo_corresponsales','nombre','fecha','codigo_propietario','codigo_localidad']
