from decimal import Decimal

from django.core.management.base import BaseCommand

from carros.models import Carro


class Command(BaseCommand):
    help = 'Cadastra carros de exemplo'

    def handle(self, *args, **kwargs):
        dados = [
            dict(marca='Fiat', modelo='Uno Mille com Escada', ano=1998, preco=Decimal('45000'),
                 km=387000, cor='Branco', potencia_cv=58, velocidade_max=999, zero_a_cem=Decimal('0.1'),
                 cambio='Manual', cidade='Concórdia - SC', destaque=True,
                 descricao='O carro mais rápido do mundo, segundo o dono. A escada no teto '
                          'reduz o arrasto aerodinâmico em 300% (dado não verificado). '
                          'Acompanha o pneu careca de edição limitada.'),
            dict(marca='Ferrari', modelo='SF90 Stradale', ano=2023, preco=Decimal('5200000'),
                 km=3200, cor='Rosso Corsa', potencia_cv=1000, velocidade_max=340, zero_a_cem=Decimal('2.5'),
                 cambio='Dupla embreagem', cidade='São Paulo - SP', destaque=True,
                 descricao='Híbrido plug-in com 1.000 cv, o Ferrari de rua mais potente da sua geração.'),
            dict(marca='Koenigsegg', modelo='Jesko', ano=2022, preco=Decimal('21000000'),
                 km=800, cor='Preto Carbono', potencia_cv=1600, velocidade_max=480, zero_a_cem=Decimal('2.5'),
                 cambio='Dupla embreagem', cidade='Rio de Janeiro - RJ', destaque=True,
                 descricao='Hipercarro sueco com câmbio Light Speed Transmission de 9 marchas.'),
            dict(marca='Porsche', modelo='911 GT3 RS', ano=2023, preco=Decimal('3300000'),
                 km=5400, cor='Cinza Gelo', potencia_cv=525, velocidade_max=296, zero_a_cem=Decimal('3.2'),
                 cambio='Dupla embreagem', cidade='Curitiba - PR', destaque=False,
                 descricao='Aerodinâmica ativa de pista e motor 4.0 aspirado que gira até 9.000 rpm.'),
            dict(marca='Aston Martin', modelo='DBS Superleggera', ano=2021, preco=Decimal('3900000'),
                 km=9800, cor='Verde Racing', potencia_cv=725, velocidade_max=340, zero_a_cem=Decimal('3.4'),
                 cambio='Automático', cidade='Florianópolis - SC', destaque=False,
                 descricao='V12 biturbo, elegância britânica e sonoridade inesquecível.'),
            dict(marca='Lamborghini', modelo='Huracán STO', ano=2022, preco=Decimal('4100000'),
                 km=2100, cor='Laranja Arancio', potencia_cv=640, velocidade_max=310, zero_a_cem=Decimal('3.0'),
                 cambio='Dupla embreagem', cidade='Brasília - DF', destaque=False,
                 descricao='Versão de homologação das pistas, com V10 aspirado e tração traseira.'),
            dict(marca='McLaren', modelo='720S', ano=2020, preco=Decimal('3600000'),
                 km=12000, cor='Cinza Chumbo', potencia_cv=720, velocidade_max=341, zero_a_cem=Decimal('2.9'),
                 cambio='Dupla embreagem', cidade='Porto Alegre - RS', destaque=False,
                 descricao='Monocoque de fibra de carbono e portas em asa de borboleta.'),
            dict(marca='Bugatti', modelo='Chiron Sport', ano=2019, preco=Decimal('19500000'),
                 km=4300, cor='Azul e Preto', potencia_cv=1500, velocidade_max=420, zero_a_cem=Decimal('2.4'),
                 cambio='Dupla embreagem', cidade='São Paulo - SP', destaque=False,
                 descricao='Motor W16 quadriturbo. Cada pedal é uma decisão importante.'),
        ]

        criados = 0
        for d in dados:
            _, novo = Carro.objects.get_or_create(
                marca=d['marca'], modelo=d['modelo'], defaults=d
            )
            criados += int(novo)

        self.stdout.write(self.style.SUCCESS(f'{criados} carro(s) cadastrado(s).'))