from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100, verbose_name= 'Nombre del empleado')
    idcorreo = models.EmailField(primary_key=True, verbose_name= 'Correo')
    contrasena_hashed = models.CharField(max_length=128,verbose_name= 'Contraseña') 

    def __str__(self):
        return self.nombre

