from django.db import models

class Carro(models.Model):
    CAMBIOS = [
        ('Automático', 'Automático'),
        ('Manual', 'Manual'),
        ('Dupla embreagem', 'Dupla embreagem'),
    ]

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    km = models.PositiveIntegerField(default=0)
    cor = models.CharField(max_length=40)
    potencia_cv = models.PositiveIntegerField()
    velocidade_max = models.PositiveIntegerField(help_text='km/h')
    zero_a_cem = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True, help_text='segundos'
    )
    cambio = models.CharField(max_length=20, choices=CAMBIOS, default='Automático')
    cidade = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='carros/', blank=True, null=True)
    destaque = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-destaque', '-criado_em']

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano})'