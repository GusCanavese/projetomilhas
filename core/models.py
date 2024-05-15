from django.db import models


class Membro(models.Model):
    nome        = models.CharField(max_length=150,    default='null')
    data        = models.DateField()  
    curso       = models.CharField(max_length=150,    default='null')
    matricula   = models.CharField(max_length=12,     default='null')
    email       = models.EmailField(max_length=150,   default='null')
    entrada     = models.DateField()  
    saida       = models.DateField()  
    pontos      = models.CharField(max_length=2,      default='null')
    cargo       = models.CharField(max_length=150,    default='null')
    info        = models.CharField(max_length=300,    default='null')
    foto        = models.ImageField(upload_to="foto", default='foto')
    certificado = models.CharField(max_length=3,      default='null', null=True, blank=False)


    def __str__(self) -> str:
        return self.nome 
