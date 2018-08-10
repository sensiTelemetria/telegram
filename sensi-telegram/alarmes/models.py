from django.db import models

from tags import models as tags_models
from usuarios import models as usuarios_models


# Create your models here.
class alarme(models.Model):
    tags = models.ManyToManyField(tags_models.tag)
    usuarios = models.ManyToManyField(usuarios_models.usuario)
    trigger = models.FloatField(verbose_name='Valor do Trigger')

    def __str__(self):
        return str(self.id) + ' | ' + str(self.trigger)
