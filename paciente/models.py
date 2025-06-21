from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome
