from django.db import models

class Marca(models.Model):
    Nombre = models.TextField(default="")
    def __str__(self):
        return self.Nombre
class movimieto(models.Model):
    velocidad = models.PositiveIntegerField(default=0)
    def frenar(self):
        self.velocidad = 0
    def __str__(self):
        return "La velocidad es " + str(self.velocidad)
class Carro(models.Model):
    vin = models.TextField(max_length=21, primary_key=True)
    marca = models.ForeignKey(Marca,null=True, blank=False, on_delete=models.CASCADE)
    modelo = models.TextField(max_length = 20)
    puertas = models.PositiveIntegerField()
    velocidad = models.PositiveIntegerField(default=0)
    movimiento = models.ForeignKey(movimieto,null=True, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.vin