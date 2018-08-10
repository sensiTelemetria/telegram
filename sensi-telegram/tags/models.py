from django.db import models

# Create your models here.
class tag(models.Model):
    mac = models.CharField(max_length= 20)
    localizacao = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.localizacao)