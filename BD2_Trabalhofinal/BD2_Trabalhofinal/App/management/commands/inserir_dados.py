from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from datetime import datetime
from BD2_Trabalhofinal.App.models import (
    P_Associacao, P_Estadio, P_Posicao, P_Clube, P_Equipa, P_FormatoCompeticao, P_Competicao,
    P_Jogador, P_Jogo, P_Golo, P_Penalti, P_Falta, P_Substituicao,
    Utilizador, P_ClubeFavorito
)


# Usa-se o comando python manage.py inserir_dados
class Command(BaseCommand):
    help = 'Inserts initial data for associations, stadiums, and positions'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                
                # Inserir Associações
                # Inserir Associações
                associacoes_data = [
                    {
                        'nome': "Associação de Futebol de Viseu",
                        'url': "https://afviseu.fpf.pt/",
                        'pais': "Portugal",
                        'imagem': "https://www.zerozero.pt/img/logos/associacoes/17_af_viseu_imgbank.png"
                    }
                    {
                        'nome': "Associação de Futebol de Aveiro",
                        'url': "http://afaveiro.pt",
                        'pais': "Portugal",
                        'imagem': "https://afaveiro.fpf.pt/Portals/19/Logo_AFA3.gif?ver=2019-01-24-120420-670"
                    },
                    {
                        'nome': "Associação de Futebol de Coimbra",
                        'url': "https://afcoimbra.fpf.pt/",
                        'pais': "Portugal",
                        'imagem': "https://afcoimbra.fpf.pt/Portals/5/Logo_Coimbra.png?ver=2015-10-28-094333-600"
                    },
                    {
                        'nome': "Associação de Futebol do Algarve",
                        'url': "http://afalgarve.pt",
                        'pais': "Portugal",
                        'imagem': "https://upload.wikimedia.org/wikipedia/pt/a/a4/AF_Algarve.png"
                    },
                    {
                        'nome': "Associação de Futebol de Angra do Heroísmo",
                        'url': "http://afah.pt",
                        'pais': "Portugal",
                        'imagem': "https://afah.fpf.pt/Portals/18/AF_Angra_Heroismo.png?ver=2016-08-24-100523-877"
                    },
                    {
                        'nome': "Associação de Futebol de Beja",
                        'url': "http://afbeja.com",
                        'pais': "Portugal",
                        'imagem': "https://afbeja.fpf.pt/Portals/12/logo%20afbeja%20novo.jpg?ver=2020-09-04-115900-780"
                    },
                    {
                        'nome': "Associação de Futebol de Braga",
                        'url': "http://afbraga.com",
                        'pais': "Portugal",
                        'imagem': "https://afbraga.fpf.pt/Portals/4/AF_Braga.png?ver=2016-04-26-142900-000"
                    },
                    {
                        'nome': "Associação de Futebol de Bragança",
                        'url': "http://afbraganca.com",
                        'pais': "Portugal",
                        'imagem': "https://afbraganca.fpf.pt/Portals/17/af_-bragan%C3%A7a_150x150.png?ver=2017-01-13-094230-000"
                    },
                    {
                        'nome': "Associação de Futebol de Castelo Branco",
                        'url': "http://afcastelobranco.pt",
                        'pais': "Portugal",
                        'imagem': "https://afcastelobranco.fpf.pt/Portals/6/Logo_Castelo_Branco.png?ver=2016-04-26-142745-913"
                    },
                    {
                        'nome': "Associação de Futebol de Évora",
                        'url': "http://afevora.com",
                        'pais': "Portugal",
                        'imagem': "https://afevora.fpf.pt/Portals/11/Logo_Evora.png?ver=2016-05-06-102004-000"
                    },
                    {
                        'nome': "Associação de Futebol da Guarda",
                        'url': "http://afguarda.pt",
                        'pais': "Portugal",
                        'imagem': "https://afguarda.fpf.pt/Portals/20/LOGO_AFGuarda.png?ver=2018-11-05-143924-137"
                    },
                    {
                        'nome': "Associação de Futebol da Horta",
                        'url': "http://afhorta.com",
                        'pais': "Portugal",
                        'imagem': "https://afhorta.fpf.pt/Portals/13/Logo%20AFH%202022.png?ver=2023-06-30-150218-540"
                    },
                    {
                        'nome': "Associação de Futebol de Leiria",
                        'url': "http://afleiria.com",
                        'pais': "Portugal",
                        'imagem': "https://afleiria.fpf.pt/SimpleImageHandler.ashx?id=99613"
                    },
                    {
                        'nome': "Associação de Futebol de Lisboa",
                        'url': "http://www.afl.pt",
                        'pais': "Portugal",
                        'imagem': "https://afl.pt/wp-content/uploads/2023/12/cropped-Sem-Fundo.png"
                    },
                    {
                        'nome': "Associação de Futebol da Madeira",
                        'url': "http://afmadeira.com",
                        'pais': "Portugal",
                        'imagem': "https://fpfimagehandler.fpf.pt/ScoreImageHandler.ashx?type=Organization&id=878"
                    },
                    {
                        'nome': "Associação de Futebol de Ponta Delgada",
                        'url': "http://afpd.pt",
                        'pais': "Portugal",
                        'imagem': "https://afpd.fpf.pt/Portals/14/Logo_Ponta_Delgada.png?ver=2015-10-15-143459-960"
                    },
                    {
                        'nome': "Associação de Futebol de Portalegre",
                        'url': "http://afportalegre.com",
                        'pais': "Portugal",
                        'imagem': "https://afportalegre.fpf.pt/Portals/10/Logo_Portalegre.png?ver=2015-10-15-141740-000"
                    },
                    {
                        'nome': "Associação de Futebol do Porto",
                        'url': "http://afporto.pt",
                        'pais': "Portugal",
                        'imagem': "https://upload.wikimedia.org/wikipedia/commons/a/a2/Af_porto.png"
                    },
                    {
                        'nome': "Associação de Futebol de Santarém",
                        'url': "http://afsantarem.pt",
                        'pais': "Portugal",
                        'imagem': "https://afsantarem.fpf.pt/Portals/3/AF_Santarem.png?ver=2015-07-21-194208-000"
                    },
                    {
                        'nome': "Associação de Futebol de Setúbal",
                        'url': "http://afsetubal.pt",
                        'pais': "Portugal",
                        'imagem': "https://afsetubal.fpf.pt/Portals/16/logo_afs_brasao%20novo.png?ver=2022-12-13-173718-513"
                    },
                    {
                        'nome': "Associação de Futebol de Viana do Castelo",
                        'url': "http://afvianacastelo.com",
                        'pais': "Portugal",
                        'imagem': "https://afvianacastelo.fpf.pt/Portals/7/AFVC-Logo.png?ver=2016-05-09-164122-000"
                    },
                    {
                        'nome': "Associação de Futebol de Vila Real",
                        'url': "http://afvreal.com",
                        'pais': "Portugal",
                        'imagem': "https://apaf.controlink.pt/images/associacoes/AF%20Vila%20Real.png"
                    },
                ]

                
                associacoes = [P_Associacao.objects.create(**data) for data in associacoes_data]
                self.stdout.write(self.style.SUCCESS(f'{len(associacoes)} Associações created'))

                # Inserir Estádios
                ## Estados: Ativo / Em Obras / Demolido
                estadios_data = [
                    {
                        'nome': "Estádio da Luz",
                        'imagem': "https://www.zerozero.pt/img/estadios/328/214328_estadio_da_luz.jpg.jpg",
                        'pais': "Portugal",
                        'cidade': "São Domingos de Benfica - Lisboa",
                        'inauguracao': 1954,
                        'estado': 'Demolido',
                        'lotacao': 120000
                    },
                    {
                        'nome': "Estádio do Sport Lisboa e Benfica",
                        'imagem': "https://cdn-imgix.headout.com/media/images/e5aa08b27d25e7d82bcbc3aa9517228a-Benfica%20Stadium%20%26%20Museum%201.jpg",
                        'pais': "Portugal",
                        'cidade': "Lisboa",
                        'inauguracao': 2003,
                        'estado': 'Ativo',
                        'lotacao': 64642
                    },
                    {
                        'nome': "Estádio José Alvalade",
                        'imagem': "https://editorial.uefa.com/resources/0282-185d605071d4-06036d20de7f-1000/sporting_cp_v_juventus_quarterfinal_second_leg_-_uefa_europa_league.jpeg",
                        'pais': "Portugal",
                        'cidade': "Lisboa",
                        'inauguracao': 2003,
                        'estado': 'Ativo',
                        'lotacao': 50095
                    },
                    {
                        'nome': "Estádio Municipal José Bento Pessoa",
                        'imagem': "https://mfimages.iol.pt/soccer/venues/600x450/532.jpg",
                        'pais': "Portugal",
                        'cidade': "Figueira da Foz",
                        'inauguracao': 1953,
                        'estado': 'Ativo',
                        'lotacao': 9000
                    },
                    {
                        'nome': "Estádio Municipal do Fontelo",
                        'imagem': "https://www.zerozero.pt/img/estadios/294/1223294_med_estadio_municipal_do_fontelo.jpg.jpg",
                        'pais': "Portugal",
                        'cidade': "Viseu",
                        'inauguracao': 1928,
                        'estado': 'Ativo',
                        'lotacao': 6912
                    },
                    {
                        'nome': "Estádio Municipal de Aveiro",
                        'imagem': "https://upload.wikimedia.org/wikipedia/commons/e/ef/Nt-Aveiro-Estadio_Beira-Mar.jpg",
                        'pais': "Portugal",
                        'cidade': "Aveiro",
                        'inauguracao': 2003,
                        'estado': 'Ativo',
                        'lotacao': 30127
                    },
                    {
                        'nome': "Estádio do Dragão",
                        'imagem': "https://files.app.fcporto.pt/sources/5c90c108c4b3b1J17qAEFdZDq1XiD.jpg",
                        'pais': "Portugal",
                        'cidade': "Porto",
                        'inauguracao': 2003,
                        'estado': 'Ativo',
                        'lotacao': 50033
                    }
                ]
                
                estadios = [P_Estadio.objects.create(**data) for data in estadios_data]
                self.stdout.write(self.style.SUCCESS(f'{len(estadios)} Estádios created'))

                # Inserir Posições
                posicoes_data = [
                    {'nome': "Defesa", 'descricao': "Defesa Direito"},
                    {'nome': "Defesa", 'descricao': "Defesa Central"},
                    {'nome': "Defesa", 'descricao': "Defesa Esquerdo"},
                    {'nome': "Médio", 'descricao': "Médio Defensivo"},
                    {'nome': "Médio", 'descricao': "Médio Ofensivo"},
                    {'nome': "Médio", 'descricao': "Médio Centro"},
                    {'nome': "Avançado", 'descricao': "Extremo Direito"},
                    {'nome': "Avançado", 'descricao': "Ponta de Lança"},
                    {'nome': "Avançado", 'descricao': "Extremo Esquerdo"},
                    {'nome': "Guarda Redes", 'descricao': ""}
                ]
                
                posicoes = [P_Posicao.objects.create(**data) for data in posicoes_data]
                self.stdout.write(self.style.SUCCESS(f'{len(posicoes)} Posições created'))
                
                 # Inserir Clubes
                 ## ano_extinto não pode ser null senão dá erro
                 ## Estado do Clube: Ativo / Suspenso / Extinto
                clubes_data = [
                    {
                        'nome': "CD Santacruzense",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/15069_imgbank_1734620394.png",
                        'ano_fundacao': 1931,
                        'ano_extinto': 0,
                        'pais': "Portugal",
                        'cidade': "Santa Cruz da Trapa - São Pedro do Sul",
                        'estado': "Ativo",
                        'associacao': associacoes[0],  # Associação de Futebol de Viseu
                        'estadio': None
                    },
                    {
                        'nome': "Naval",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/28_imgbank.png",
                        'ano_fundacao': 1893,
                        'ano_extinto': 2017,
                        'alcunhas': "Velhinha Senhora",
                        'pais': "Portugal",
                        'cidade': "Figueira da Foz",
                        'estado': "Extinto",
                        'associacao': associacoes[2],  # Associação de Futebol de Coimbra
                        'estadio': estadios[3]  # Estádio Municipal José Bento Pessoa
                    },
                    {
                        'nome': "Naval 1893",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/215830_imgbank.png",
                        'ano_fundacao': 2017,
                        'ano_extinto': 0,
                        'alcunhas': "Velhinha Senhora",
                        'pais': "Portugal",
                        'cidade': "Figueira da Foz",
                        'estado': "Ativo",
                        'associacao': associacoes[2],  # Associação de Futebol de Coimbra
                        'estadio': estadios[3]  # Estádio Municipal José Bento Pessoa
                    },
                    {
                        'nome': "Sporting",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/16_imgbank_1722518934.png",
                        'ano_fundacao': 1906,
                        'ano_extinto': 0,
                        'alcunhas': "Leões",
                        'pais': "Portugal",
                        'cidade': "Lisboa",
                        'estado': "Ativo",
                        'associacao': associacoes[1],  # Associação de Futebol de Lisboa
                        'estadio': estadios[2]  # Estádio José Alvalade
                    },
                    {
                        'nome': "Benfica",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/4_imgbank_1683238034.png",
                        'ano_fundacao': 1904,
                        'ano_extinto': 0,
                        'alcunhas': "Águias, Encarnados, Glorioso",
                        'pais': "Portugal",
                        'cidade': "Lisboa",
                        'estado': "Ativo",
                        'associacao': associacoes[1],  # Associação de Futebol de Lisboa
                        'estadio': estadios[1]  # Estádio do Sport Lisboa e Benfica
                    }
                ]
                
                clubes = [P_Clube.objects.create(**data) for data in clubes_data]
                self.stdout.write(self.style.SUCCESS(f'{len(clubes)} Clubes created'))
                
                # Inserir Equipas
                ## Estado: Ativa / Suspensa / Extinta
                equipas_data = [
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[4],  # Clube Benfica
                    },
                    {
                        'nome': "Jun.A S19",
                        'estado': "Ativo",
                        'clube': clubes[4],  # Clube Benfica
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[3],  # Clube Sporting
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[2],  # Clube Naval 1893
                    },
                ]
                
                equipas = [P_Equipa.objects.create(**data) for data in equipas_data]
                self.stdout.write(self.style.SUCCESS(f'{len(equipas)} Equipas created'))
                
                # Inserir Formato Competição
                ## Valor de Mercado: se não houver, metes zero (para garantir que não dá erro) e é em milhões
                formatosComp_data = [
                    {
                        'nome': "Liga Portuguesa",
                        'descricao': "Liga Portuguesa",
                        'valor_de_mercado': 1980,
                    },
                ]
                
                formatosComp = [P_FormatoCompeticao.objects.create(**data) for data in formatosComp_data]
                self.stdout.write(self.style.SUCCESS(f'{len(formatosComp)} Formatos Competição created'))
                
                # Inserir Competição
                ## Vencedor: coloca-se None se não houver
                competicoes_data = [
                    {
                        'nome': "Liga Portuguesa",
                        'data_inicio': datetime(2025, 1, 17).date(),
                        'data_fim': datetime(2025, 5, 31).date(),
                        'finalizado': True,
                        'formato': formatosComp[0], # Formato Liga Portuguesa
                        'vencedor': clubes[2], # Clube Naval 1893
                    },
                ]
                
                competicoes = [P_Competicao.objects.create(**data) for data in competicoes_data]
                self.stdout.write(self.style.SUCCESS(f'{len(competicoes)} Competições created'))
                
                # Inserir Jogador
                ## Situação: Ativo / Aleijado / Expulso / Sem Clube / Reformado
                ## As chaves estrangeiras que não tiver, coloca-se None
                ## Altura em cm, Valor de Mercado em milhões
                jogadores_data = [
                    {
                        'nome': "Viktor Gyökeres",
                        'idade': 26,
                        'imagem': "Thttps://i.guim.co.uk/img/media/949db9aed8c784769dd16baf88ba4a6e16da2e4d/233_511_3026_1815/master/3026.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=83d72cdfe662a162e809d77ca049ff6f" ,
                        'altura': 189,
                        'peso': 90.0,
                        'nacionalidade': "Suécia",
                        'num_camisola': 9, 
                        'valor_de_mercado': 77.0,
                        'situacao': "Ativo",
                        'clube': clubes[3], # Clube Sporting
                        'posicao': posicoes[7], # Posição Avançado (Ponta de Lança)
                        'equipa': equipas[2], # Equipa Principal Sporting
                    },
                    {
                        'nome': "Ángel Di María",
                        'idade': 36,
                        'imagem': "https://www.thesun.co.uk/wp-content/uploads/2023/06/crop-22767070.jpg?w=620" ,
                        'altura': 180,
                        'peso': 66.0,
                        'nacionalidade': "Argentina",
                        'num_camisola': 11, 
                        'valor_de_mercado': 3.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[6], # Posição Avançado (Extrema Direita)
                        'equipa': equipas[0], # Equipa Principal Sporting
                    },
                    {
                        'nome': "Nuno Félix",
                        'idade': 20,
                        'imagem': "https://www.zerozero.pt/img/planteis/new/77/10/8697710_nuno_felix_20240517091326.jpg" ,
                        'altura': 182,
                        'peso': 69.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 60, 
                        'valor_de_mercado': 1.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[3], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[0], # Equipa Principal Sporting
                    },
                ]
                
                jogadores = [P_Jogador.objects.create(**data) for data in jogadores_data]
                self.stdout.write(self.style.SUCCESS(f'{len(jogadores)} Jogadores created'))
                
                # Inserir Jogo
                ## Estado: Em Breve / A Decorrer / Terminado / Cancelado
                ## O Vencedor, se não houver, coloca-se None
                jogos_data = [
                    {
                        'dia': datetime(2025, 1, 30).date(),
                        'hora': "14:00",
                        'estado': "Terminado" ,
                        'duracao': 90,
                        'prolongamento': True,
                        'penaltis': True,
                        'competicao': competicoes[0], # Competição Liga Portuguesa
                        'estadio': estadios[1], # Estádio do Sport Lisboa e Benfica
                        'clube_casa': clubes[4], # Clube Benfica
                        'clube_fora': clubes[3], # Clube Sporting
                        'equipa_casa': equipas[0], # Equipa Principal Benfica
                        'equipa_fora': equipas[2], # Equipa Principal Sporting
                        'vencedor': clubes[2], # Benfica
                    },
                ]
                
                jogos = [P_Jogo.objects.create(**data) for data in jogos_data]
                self.stdout.write(self.style.SUCCESS(f'{len(jogos)} Jogos created'))
                
                # Inserir Golo
                golos_data = [
                    {
                        'minuto': 36,
                        'compensacao': 0,
                        'penalti': False,
                        'jogo': jogos[0], # Jogo Benfica - Sporting
                        'jogador': jogadores[1], # Jogador Ángel Di María
                        'clube': clubes[4], # Clube Benfica
                    },
                    {
                        'minuto': 90,
                        'compensacao': 3,
                        'penalti': False,
                        'jogo': jogos[0], # Jogo Benfica - Sporting
                        'jogador': jogadores[0], # Jogador Viktor Gyökeres
                        'clube': clubes[3], # Clube Sporting
                    },
                ]
                
                golos = [P_Golo.objects.create(**data) for data in golos_data]
                self.stdout.write(self.style.SUCCESS(f'{len(golos)} Golos created'))
            
                # Inserir Penálti
                penaltis_data = [
                    {
                        'numero': 1,
                        'golo': True,
                        'jogo': jogos[0], # Jogo Benfica - Sporting
                        'jogador': jogadores[1], # Jogador Ángel Di María
                        'clube': clubes[4], # Clube Benfica
                    },
                    {
                        'numero': 2,
                        'golo': True,
                        'jogo': jogos[0], # Jogo Benfica - Sporting
                        'jogador': jogadores[0], # Jogador Viktor Gyökeres
                        'clube': clubes[3], # Clube Sporting
                    },
                    {
                        'numero': 3,
                        'golo': True,
                        'jogo': jogos[0], # Jogo Benfica - Sporting
                        'jogador': jogadores[2], # Jogador Nuno Félix
                        'clube': clubes[4], # Clube Benfica
                    },
                ]
                    
                penaltis = [P_Penalti.objects.create(**data) for data in penaltis_data]
                self.stdout.write(self.style.SUCCESS(f'{len(penaltis)} Penaltis created'))
                
                # Inserir Falta
                ## Cartão Cor: Amarelo / Vermelho / ""
                faltas_data = [
                    {
                        'minuto': 56,
                        'compensacao': 0,
                        'cartao': True,
                        'cartao_cor': "",
                        'jogo': jogos[0], # Jogo Benfica - Sporting
                        'jogador': jogadores[1], # Jogador Ángel Di María
                        'clube': clubes[4], # Clube Benfica
                    },
                ]
                    
                faltas = [P_Falta.objects.create(**data) for data in faltas_data]
                self.stdout.write(self.style.SUCCESS(f'{len(faltas)} Faltas created'))
                
                # Inserir Substituição
                substituicoes_data = [
                    {
                        'minuto': 88,
                        'compensacao': 0,
                        'jogo': jogos[0], # Jogo Benfica - Sporting
                        'jogador_sai': jogadores[1], # Jogador Ángel Di María
                        'jogador_entra': jogadores[2], # Jogador Nuno Félix
                        'clube': clubes[4], # Clube Benfica
                    },
                ]
                    
                substituicoes = [P_Substituicao.objects.create(**data) for data in substituicoes_data]
                self.stdout.write(self.style.SUCCESS(f'{len(substituicoes)} Substituições created'))
                
                # Inserir Utilizadores
                ## Cuidado para não inserir o mesmo email
                utilizadores_data = [
                    {
                        'nome': "Miguel Silva",
                        'email': "miguel@email.com",
                        'palavra_passe': "123",
                        'is_active': True,
                        'is_staff': True,
                        'is_superuser': True 
                    },
                    {
                        'nome': "Francisca Palma",
                        'email': "kika@email.com",
                        'palavra_passe': "123",
                        'is_active': True,
                        'is_staff': False,
                        'is_superuser': False
                    },
                    {
                        'nome': "Marco Vicente",
                        'email': "vicente@email.com",
                        'palavra_passe': "123",
                        'is_active': True,
                        'is_staff': True,
                        'is_superuser': True
                    },
                ]
                
                # Criar Utilizadores utilizando o manager para a criptografia (hashing) da palavra-passe
                utilizadores = []
                for data in utilizadores_data:
                    palavra_passe = data.pop('palavra_passe')  # Remove password from data dict
                    utilizador = Utilizador.objects.create_user(
                        email=data.pop('email'),
                        nome=data.pop('nome'),
                        palavra_passe=palavra_passe,
                        **data
                    )
                    utilizadores.append(utilizador)
                
                self.stdout.write(self.style.SUCCESS(f'{len(utilizadores)} Utilizadores created'))
                
                # Inserir Clube Favorito
                clubesFav_data = [
                    {
                        'utilizador_id': utilizadores[1], # Utilizador Francisca
                        'clube': clubes[3], # Clube Sporting
                    },
                ]
                    
                clubesFav = [P_ClubeFavorito.objects.create(**data) for data in clubesFav_data]
                self.stdout.write(self.style.SUCCESS(f'{len(clubesFav)} Clubes Favoritos created'))
            
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error inserting data: {e}'))
            import traceback
            traceback.print_exc()