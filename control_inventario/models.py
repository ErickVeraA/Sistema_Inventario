from django.db import models

# Create your models here.

##------------------Bodega--------------------------------------##
class bodega (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=256)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta:
        db_table = 'tp_bodega'

class Categoria_producto ( models.Model ) :
    nombre = models.CharField ( max_length= 50 )
    descripcion = models.CharField ( max_length=256)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta :
        db_table = 'tp_categoria_producto'
        verbose_name = "Categoria Producto"
        verbose_name_plural = "Categorias Productos"

    def __str__(self):
        return "{}{}{}".format(self.nombre, "    ", self.descripcion)


class Marca (models.Model):
    nombre = models.CharField(max_length=50)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = 'tp_marca'
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return "{}".format(self.nombre)


class unidad_medida (models.Model):
    nombre = models.CharField(max_length=50)
    medida = models.CharField(max_length=100)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_unidad_medida'
        verbose_name = "Unidad De Medida"
        verbose_name_plural = "Unidades de Medidas"

    def __str__(self):
        return "{}{}{}".format(self.nombre, "    ", self.medida)

class rol_persona (models.Model):
    cargo = models.CharField(max_length=50)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_rol_persona'
        verbose_name = "Rol Persona"
        verbose_name_plural = "Roles De Personas"

    def __str__(self):
        return "{}".format(self.cargo)


class ingreso_cabecera (models.Model):
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=120)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=1)

    class Meta :
        db_table = 'tp_ingreso_cabecera'


class Egreso_cabecera ( models.Model ) :
    codigo = models.CharField ( max_length= 50 )
    descripcion = models.CharField ( max_length=120)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta :
        db_table = 'tp_egreso_cabecera'

class Persona (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    direccion = models.CharField(max_length=250)
    cedula =models.CharField(max_length=10)
    correo =models.EmailField(null= True, blank= True)
    Rol_persona = models.ForeignKey(rol_persona, on_delete=models.CASCADE)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default= 1)

    class Meta:
        db_table = 'tp_persona'
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return "{}{}{}".format(self.nombre, "    ",self.apellido)


class producto (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    marca_1 = models.ForeignKey(Marca, on_delete=models.CASCADE)
    persona_1 = models.ForeignKey(Persona, on_delete=models.CASCADE)
    unidad_medida_1 = models.ForeignKey(unidad_medida, on_delete=models.CASCADE)
    categoria_producto_1 = models.ForeignKey(Categoria_producto, on_delete=models.CASCADE)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_producto'
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return "{}{}{}".format(self.nombre, "    ", self.descripcion)

class Devolucion ( models.Model ) :
    detalle = models.CharField ( max_length= 256 )


    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta :
        db_table = 'tp_devolucion'

class proveedor (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    direccion = models.CharField(max_length=250)
    celular = models.CharField(max_length=10)
    correo = models.EmailField(null= True, blank= True)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = 'tp_proveedor'



class Bodega_producto (models.Model):
    cantidad = models.CharField(max_length= 5)
    unidad  = models.CharField(max_length=10)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default= 1)

    class Meta:
        db_table = 'tp_bodega_producto'



class ingreso_detalle (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_ingreso_detalle'


class Egreso_detalle ( models.Model ) :
    cantidad = models.CharField(max_length= 50)
    precio = models.CharField(max_length=5)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta :
        db_table = 'tp_egreso_detalle'