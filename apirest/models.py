from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 255)
    content = models.TextField ()

class propietario(models.Model):
    codigo = models.CharField(max_length= 255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cedula = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)

class corresponsales(models.Model):
    codigo = models.CharField(max_length=255)
    codigo_corresponsales=models.CharField(max_length=255)
    nombre= models.CharField(max_length=255)
    fecha= models.DateField()
    codigo_propietario= models.ForeignKey('propietario',on_delete=models.CASCADE)
    codigo_localidad=models.ForeignKey('localidad',on_delete=models.CASCADE)

class cobros(models.Model):
    codigo = models.CharField(max_length=255)
    codigo_factura=models.ForeignKey('factura',on_delete=models.CASCADE)
    fecha=models.DateField()
    valor=models.IntegerField()
    adjunto_foto=models.ImageField()
    fecha_anulacion=models.DateField()
    codigo_corresponsales=models.ForeignKey('corresponsales',on_delete=models.CASCADE)
    codigo_estado=models.ForeignKey('estado',on_delete=models.CASCADE)

class factura(models.Model):
    codigo= models.CharField(max_length=255)
    codigo_cliente= models.ForeignKey('cliente',on_delete=models.CASCADE)
    local= models.CharField(max_length=255)
    punto = models.CharField(max_length=255)
    numero = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=4, decimal_places=4)
    observacion = models.TextField()
    codigo_estado= models.ForeignKey('estado',on_delete=models.CASCADE)

class cliente(models.Model):
    codigo = models.CharField(max_length=50)
    cedula= models.CharField(max_length=50)
    cliente= models.CharField(max_length=255)
    servicio = models.CharField(max_length=255)
    codigo_estado = models.ForeignKey('estado',on_delete=models.CASCADE)

class contrato_cabecera(models.Model):
    codigo = models.CharField(max_length= 255)
    numero_contrato= models.CharField(max_length= 255)
    fecha = models.DateField()

class plan_velocidad(models.Model):
    codigo = models.CharField(max_length= 255)
    descripcion= models.TextField()
    velocidad= models.IntegerField()
    estado= models.ForeignKey('estado',on_delete=models.CASCADE)


class contrato_detalle(models.Model):
    codigo_detalle = models.CharField(max_length= 255)
    codigo_cabecera= models.ForeignKey('contrato_cabecera',on_delete=models.CASCADE)
    codigo_producto=models.ForeignKey('producto',on_delete=models.CASCADE) 
    codigo_estado= models.ForeignKey('estado',on_delete=models.CASCADE)

class producto(models.Model):
    codigo = models.CharField(max_length= 255)
    descripcion = models.TextField()
    codigo_estado = models.ForeignKey('estado',on_delete=models.CASCADE)
    precio = models.IntegerField()
    codigo_plan_velocidad = models.ForeignKey('plan_velocidad',on_delete=models.CASCADE)

class localidad(models.Model):
    codigo = models.CharField(max_length= 255)
    direccion= models.TextField()
    referencia = models.TextField()
    codigo_estado= models.ForeignKey('estado',on_delete=models.CASCADE)
    altitud = models.FloatField()
    longitud = models.FloatField()

class estado(models.Model):
    codigo = models.CharField(max_length= 255)
    estado_descripcion = models.TextField()
    estado_vigencia = models.CharField(max_length= 255)

class telefono_localidad(models.Model):
    codigo = models.CharField(max_length= 255)
    telefono = models.CharField(max_length= 255)
    codigo_estado = models.ForeignKey('estado',on_delete=models.CASCADE)
    codigo_localidad = models.ForeignKey('localidad',on_delete=models.CASCADE)
