from django.db import models
from django.core.validators import MinLengthValidator

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=14,
        validators=[MinLengthValidator(11)]
    )
    email = models.EmailField()
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
