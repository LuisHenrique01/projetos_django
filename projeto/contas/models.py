from django.db import models

# Create your models here.
class Conta(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
class Transacoa(models.Model):
    data = models.DateTimeField(auto_now_add=False)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Conta, on_delete=models.CASCADE)
    observacao = models.TextField(blank=True)
    
    def __str__(self):
        return self.descricao