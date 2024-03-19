from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)

    def str(self):
        return f'{self.mail} - Activo: {bool(self.activo)}'