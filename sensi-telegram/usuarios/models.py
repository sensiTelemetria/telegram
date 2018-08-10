from django.db import models

# Create your models here.
from alarmes import models as alarmes_models

class usuario(models.Model):
    nome = models.CharField(max_length= 20,verbose_name='Nome do Usuário')
    email = models.EmailField(verbose_name='E-mail')
    telefone = models.IntegerField(verbose_name='Telefone')
    chat_id = models.IntegerField(verbose_name='ID Telegram')

    def __str__(self):
        return self.nome