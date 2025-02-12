from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
