from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 255)
    content = models.TextField ()

class propietario(models.Model):
    codigo = models.CharField(max_length= 255)
    nombre = models.TextField ()
    apellido = models.TextField ()
    cedula = models.TextField ()
    usuario = models.TextField ()
    contrasena = models.TextField ()

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
    local= models.TextField()
    punto = models.TextField()
    numero = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=4, decimal_places=4)
    observacion = models.TextField()
    codigo_estado= models.ForeignKey('estado',on_delete=models.CASCADE)

class cliente(models.Model):
    codigo = models.CharField(max_length=50)
    cedula= models.TextField()
    cliente= models.TextField()
    servicio = models.TextField()
    codigo_estado = models.ForeignKey('estado',on_delete=models.CASCADE)

class contrato_cabecera(models.Model):
    codigo = models.TextField()
    numero_contrato= models.TextField()
    fecha = models.DateField()

class plan_velocidad(models.Model):
    codigo = models.TextField()
    descripcion= models.TextField()
    velocidad= models.IntegerField()
    estado= models.ForeignKey('estado',on_delete=models.CASCADE)


class contrato_detalle(models.Model):
    codigo_detalle = models.TextField()
    codigo_cabecera= models.ForeignKey('contrato_cabecera',on_delete=models.CASCADE)
    codigo_producto=models.ForeignKey('producto',on_delete=models.CASCADE) 
    codigo_estado= models.ForeignKey('estado',on_delete=models.CASCADE)

class producto(models.Model):
    codigo = models.TimeField()
    descripcion = models.TextField()
    codigo_estado = models.ForeignKey('estado',on_delete=models.CASCADE)
    precio = models.IntegerField()
    codigo_plan_velocidad = models.ForeignKey('plan_velocidad',on_delete=models.CASCADE)

class localidad(models.Model):
    codigo = models.TextField()
    direccion= models.TextField()
    referencia = models.TextField()
    codigo_estado= models.ForeignKey('estado',on_delete=models.CASCADE)
    altitud = models.FloatField()
    longitud = models.FloatField()

class estado(models.Model):
    codigo = models.TextField()
    estado_descripcion = models.TextField()
    estado_vigencia = models.TextField()

class telefono_localidad(models.Model):
    codigo = models.TextField()
    telefono = models.TextField()
    codigo_estado = models.ForeignKey('estado',on_delete=models.CASCADE)
    codigo_localidad = models.ForeignKey('localidad',on_delete=models.CASCADE)
