from django.db import models

# Create your models here.

class Paciente(models.Model):

    ID=models.AutoField(primary_key=True)
    Paciente = models.CharField(max_length=250)
    Direccion = models.CharField(max_length=250)
    Telefono = models.IntegerField(max_length=11)
    FotoPaciente = models.ImageField(upload_to='imagenes', verbose_name='Imagen', null=True)
    Realiza = models.TextField(verbose_name='', null=True)


    def __str__(self):
        fila = 'Nombre:'+self.Paciente + "-" + "Realiza:" + self.Realiza
        return fila
    
    def Borrar(self, using=None, keep_parents=False):
        self.FotoPaciente.storage.delete(self.FotoPaciente.name)
        super().delete




