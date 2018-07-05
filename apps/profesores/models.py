from django.db import models
from django.db.models import Min
from django.core.validators import validate_comma_separated_integer_list
# Create your models here.

class Grupos(models.Model):
    Descripcion = models.TextField(primary_key=True)
    def __str__(self):
        return self.Descripcion
class Estudiantes(models.Model):
    Matricula = models.TextField(max_length=8, primary_key=True)
    ApellidoPaterno = models.TextField()
    ApellidoMaterno = models.TextField()
    Nombres = models.TextField()
    Grupo = models.ManyToManyField(Grupos)
    Uno = models.BooleanField(default=False)
    Dos = models.BooleanField(default=False)
    Tres = models.BooleanField(default=False)
    Cuatro = models.BooleanField(default=False)
    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)
    def __str__(self):
        return self.NombreCompleto()
class Intentos(models.Model):
        Matricula = models.ForeignKey(Estudiantes,null=True, blank=False, on_delete=models.CASCADE)
        Tiempo = models.DurationField(null=True, blank=False,)
        CantInstrucciones = models.PositiveIntegerField()
class Profesor(models.Model):
    Matricula = models.TextField(max_length=8, primary_key=True)
    ApellidoPaterno = models.TextField()
    ApellidoMaterno = models.TextField()
    Nombres = models.TextField()
    Grupo = models.ManyToManyField(Grupos)
    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)
    def __str__(self):
        return self.NombreCompleto()
class Problemas(models.Model):
    Descripcion = models.TextField()
    VectorEntrada = models.TextField(validators=[validate_comma_separated_integer_list])
    VectorSalida = models.TextField(validators=[validate_comma_separated_integer_list])
    VectorPiso = models.TextField(validators=[validate_comma_separated_integer_list])
    IDIntentos = models.ManyToManyField(Intentos)
    def __str__(self):
        return self.Descripcion
    def MenorInstruc(self):
        if self.IDIntentos.all().exists():
            return self.IDIntentos.order_by("CantInstrucciones")[0].Matricula.NombreCompleto(), self.IDIntentos.order_by("CantInstrucciones")[0].CantInstrucciones
        else:
            return None, None
    def Menortiempo(self):
        if self.IDIntentos.all().exists():
            return self.IDIntentos.order_by("Tiempo")[0].Matricula.NombreCompleto(), self.IDIntentos.order_by("Tiempo")[0].Tiempo
        else:
            return None, None
    def Menortiempop(self,Matricula):
        if self.IDIntentos.filter(Matricula=Matricula).exists():
            return self.IDIntentos.order_by("Tiempo")[0].Tiempo
        else:
            return None
    def MenorInstrucp(self, Matricula):
        if self.IDIntentos.filter(Matricula=Matricula).exists():
            return self.IDIntentos.filter(Matricula=Matricula).order_by("CantInstrucciones")[0].CantInstrucciones
        else:
            return None
