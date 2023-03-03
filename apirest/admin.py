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

@admin.register(factura)
class factura(admin.ModelAdmin):
    list_display=['codigo','codigo_cliente','local','punto','numero','saldo','observacion','codigo_estado']

@admin.register(cliente)
class cliente(admin.ModelAdmin):
    list_display=['codigo','cedula','cliente','servicio','codigo_estado']

@admin.register(contrato_cabecera)
class contrato_cabecera(admin.ModelAdmin):
    list_display=['codigo','numero_contrato','fecha']

@admin.register(plan_velocidad)
class contrato_cabecera(admin.ModelAdmin):
    list_display=['codigo','descripcion','velocidad','estado']

@admin.register(contrato_detalle)
class contrato_detalle(admin.ModelAdmin):
    list_display=['codigo_detalle','codigo_cabecera','codigo_producto','codigo_estado']

@admin.register(producto)
class producto(admin.ModelAdmin):
    list_display=['codigo','descripcion','codigo_estado','precio','codigo_plan_velocidad']

@admin.register(localidad)
class localidad(admin.ModelAdmin):
    list_display=['codigo','direccion','referencia','codigo_estado','altitud','longitud']

@admin.register(estado)
class estado(admin.ModelAdmin):
    list_display=['codigo','estado_descripcion','estado_vigencia']

@admin.register(telefono_localidad)
class telefono_localidad(admin.ModelAdmin):
    list_display=['codigo','telefono','codigo_estado','codigo_localidad']
    