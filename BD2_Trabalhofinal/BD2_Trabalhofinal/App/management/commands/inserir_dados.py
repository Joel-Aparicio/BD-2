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
                associacoes_data = [
                    {
                        'nome': "Associação de Futebol de Viseu",
                        'url': "https://afviseu.fpf.pt/",
                        'pais': "Portugal",
                        'imagem': "https://www.zerozero.pt/img/logos/associacoes/17_af_viseu_imgbank.png"
                    },
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
                    }
                ]

                
                associacoes = [P_Associacao.objects.create(**data) for data in associacoes_data]
                self.stdout.write(self.style.SUCCESS(f'{len(associacoes)} Associações created'))

                # Inserir Estádios
                ## Estados: Ativo / Em Obras / Demolido
                estadios_data = [
                    {
                        'nome': "Estádio das Antas",
                        'imagem': "https://img.iol.pt/image/id/56db8e790cf25dc1853beb23/",
                        'pais': "Portugal",
                        'cidade': "Porto",
                        'inauguracao': 1924,
                        'estado': 'Demolido',
                        'lotacao': 75000
                    },
                    {
                        'nome': "Estádio da Luz",
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
                        'nome': "Estádio Algarve",
                        'imagem': "https://www.zerozero.pt/img/estadios/048/1155048_ori_estadio_do_algarve.jpg",
                        'pais': "Portugal",
                        'cidade': "Algarve",
                        'inauguracao': 2003,
                        'estado': 'Ativo',
                        'lotacao': 30305
                    },
                    {
                        'nome': "Estádio do Dragão",
                        'imagem': "https://files.app.fcporto.pt/sources/5c90c108c4b3b1J17qAEFdZDq1XiD.jpg",
                        'pais': "Portugal",
                        'cidade': "Porto",
                        'inauguracao': 2003,
                        'estado': 'Ativo',
                        'lotacao': 50033
                    },
                    {
                        "nome": "Estádio Municipal de Braga",
                        "imagem": "https://scbraga.pt/wp-content/uploads/2019/07/est%C3%A1diooo.jpg",
                        "pais": "Portugal",
                        "cidade": "Braga",
                        "inauguracao": 2003,
                        "estado": "Ativo",
                        "lotacao": 30286
                    },
                    {
                        "nome": "Estádio de Sáo Miguel",
                        "imagem": "https://thumbs.web.sapo.io/?W=800&H=0&delay_optim=1&epic=NzVlF4WOSDr6hpXe3Y+yz6YMVAdPveGm4sNW9+y5/7H/LeZgM6bQrC9pDHWqH12v44Oxk6HMa+a4e+2VaiEONPeKdAWdYQNCd6O1TlLVFgAihP4=",
                        "pais": "Portugal",
                        "cidade": "Ponta Delgada",
                        "inauguracao": 1976,
                        "estado": "Ativo",
                        "lotacao": 12500
                    },
                      {
                        "nome": "Estádio Municipal de Rio Maior",
                        "imagem": "https://desmor.pt/image.php?image=estadio-municipal-de-rio-maior-rio-maior-football-stadium--31440206.jpg",
                        "pais": "Portugal",
                        "cidade": "Rio Maior",
                        "inauguracao": 2003,
                        "estado": "Ativo",
                        "lotacao": 6925
                    },
                    {
                        "nome": "Estádio D. Afonso Henriques",
                        "imagem": "https://vitoriasc.pt/wp-content/uploads/2022/01/Esta%CC%81dio-D.-Afonso-Henriques.jpg",
                        "pais": "Portugal",
                        "cidade": "Guimarães",
                        "inauguracao": 1965,
                        "estado": "Ativo",
                        "lotacao": 30000
                    },
                    {
                        "nome": "Estádio António Coimbra da Mota",
                        "imagem": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/31/0b/e2/estadio-antonio-coimbra.jpg?w=1200&h=-1&s=1",
                        "pais": "Portugal",
                        "cidade": "Estoril",
                        "inauguracao": 1939,
                        "estado": "Ativo",
                        "lotacao": 8000
                    },
                    {
                        "nome": "Estádio Municipal de Famalicão",
                        "imagem": "https://www.noticiasdefamalicao.pt/wp-content/uploads/2023/06/Estadio-MUnicipal-_-campo-de-treinos.jpg",
                        "pais": "Portugal",
                        "cidade": "Vila Nova de Famalicão",
                        "inauguracao": 1952,
                        "estado": "Ativo",
                        "lotacao": 5186
                    },
                    {
                        "nome": "Estádio do Rio Ave FC",
                        "imagem": "https://cdn-images.rtp.pt/icm/noticias/images/76/76d8f3a64323a773de803f21c58da2e7?w=860&q=90&rect=195,0,810,444",
                        "pais": "Portugal",
                        "cidade": "Vila do Conde",
                        "inauguracao": 1984,
                        "estado": "Ativo",
                        "lotacao": 5300
                    },
                    {
                        "nome": "Estádio Comendador Joaquim de Almeida Freitas",
                        "imagem": "https://www.zerozero.pt/img/estadios/826/1130826_ori_estadio_comendador_joaquim_de_almeida_freitas.jpg",
                        "pais": "Portugal",
                        "cidade": "Moreira de Cónegos - Guimarães",
                        "inauguracao":2002,
                        "estado": "Ativo",
                        "lotacao": 6150
                    },
                    {
                        "nome": "Estádio Cidade de Barcelos",
                        "imagem": "https://www.zerozero.pt/img/estadios/627/1018627_ori_estadio_cidade_de_barcelos.jpg",
                        "pais": "Portugal",
                        "cidade": "Barcelos",
                        "inauguracao":2004,
                        "estado": "Ativo",
                        "lotacao": 12046
                    },
                    {
                        "nome": "Estádio Municipal de Arouca",
                        "imagem": "https://www.zerozero.pt/img/estadios/762/857762_ori_estadio_municipal_de_arouca.jpg",
                        "pais": "Portugal",
                        "cidade": "Arouca",
                        "inauguracao":2006,
                        "estado": "Ativo",
                        "lotacao": 5600
                    },
                    {
                        "nome": "Estádio da Madeira",
                        "imagem": "https://www.zerozero.pt/img/estadios/265/1223265_ori_estadio_da_madeira.jpg",
                        "pais": "Portugal",
                        "cidade": "Funchal",
                        "inauguracao":1998,
                        "estado": "Ativo",
                        "lotacao": 5200
                    },
                    {
                        "nome": "Estádio do Clube Desportivo das Aves",
                        "imagem": "https://www.zerozero.pt/img/estadios/921/573921_ori_estadio_do_clube_desportivo_das_aves.jpg",
                        "pais": "Portugal",
                        "cidade": "Vila das Aves",
                        "inauguracao":1981,
                        "estado": "Ativo",
                        "lotacao": 6230
                    },
                    {
                        "nome": "Estádio José Gomes",
                        "imagem": "https://www.zerozero.pt/img/estadios/607/687607_ori_estadio_jose_gomes.jpg",
                        "pais": "Portugal",
                        "cidade": "Amadora",
                        "inauguracao":157,
                        "estado": "Ativo",
                        "lotacao": 9288
                    },
                    {
                        "nome": "Estádio de São Luís",
                        "imagem": "https://www.zerozero.pt/img/estadios/393/735393_ori__20201223182044_estadio_de_sao_luis.jpg",
                        "pais": "Portugal",
                        "cidade": "Faro",
                        "inauguracao":1922,
                        "estado": "Ativo",
                        "lotacao": 7000
                    },
                    {
                        "nome": "Estádio do Bessa Séc. XXI",
                        "imagem": "https://www.zerozero.pt/img/estadios/388/690388_ori_estadio_do_bessa_sec_xxi.jpg",
                        "pais": "Portugal",
                        "cidade": "Faro",
                        "inauguracao":1922,
                        "estado": "Ativo",
                        "lotacao": 7000
                    },
                    {
                        "nome": "Estádio Municipal de Aveiro",
                        "imagem": "https://www.zerozero.pt/wimg/p807242g/-.jpg",
                        "pais": "Portugal",
                        "cidade": "Aveiro",
                        "inauguracao":2003,
                        "estado": "Ativo",
                        "lotacao": 30127
                    },
                    {
                        "nome": "Estádio Nacional do Jamor",
                        "imagem": "https://jamor.ipdj.pt/cacheimage/dXBsb2FkL2ltZ19nYWxlcmlhLzEtZXN0YWRpb2hvbnJhL2VzdGFkaW9ob25yYV81NC5qcGdfNjIwXzM1MF8wXzBfMzc0ODg1.jpg",
                        "pais": "Portugal",
                        "cidade": "Oeiras",
                        "inauguracao":1944,
                        "estado": "Ativo",
                        "lotacao": 37593
                    },       
                    {
                        "nome": "Estádio Municipal de Leiria",
                        "imagem": "https://www.regiaodeleiria.pt/wp-content/uploads/2021/07/uniao_leiria_futebol_estadio_Fotos-Joaquim-DamasoDSCF7833_.jpg",
                        "pais": "Portugal",
                        "cidade": "Leiria",
                        "inauguracao": 1985,
                        "estado": "Ativo",
                        "lotacao": 27200
                    },
                    {
                        "nome": "Campo de jogos Almeida Sobrinho",
                        "imagem": "https://www.zerozero.pt/img/estadios/602/660602_ori__20200308174404_campo_almeida_sobrinho.jpg",
                        "pais": "Portugal",
                        "cidade": "S. Cruz da Trapa",
                        "estado": "Em Obras",
                        "lotacao": 600
                    },
                   
                    {
                        "nome": "Estádio Municipal da Pedreira",
                        "imagem": "https://www.zerozero.pt/img/estadios/155/182155_ori_municipal_da_pedreira.jpg",
                        "pais": "Portugal",
                        "cidade": "São Pedro do Sul",
                        "estado": "Ativo",
                        "lotacao": 2000
                    },                   
                ]
                
                estadios = [P_Estadio.objects.create(**data) for data in estadios_data]
                self.stdout.write(self.style.SUCCESS(f'{len(estadios)} Estádios created'))

                # Inserir Posições
                posicoes_data = [
                    # Guarda-Redes
                    {'nome': 'Guarda-Redes', 'descricao': 'Guarda-Redes', 'desig': 'GR'},
                    {'nome': 'Guarda-Redes', 'descricao': 'Guarda-Redes Líbero', 'desig': 'GRL'},
                    
                    # Defesa
                    {'nome': 'Defesa', 'descricao': 'Defesa Central', 'desig': 'DC'},
                    {'nome': 'Defesa', 'descricao': 'Defesa Com Bola', 'desig': 'DCP'},
                    {'nome': 'Defesa', 'descricao': 'Defesa Central Eficiente', 'desig': 'DCE'},
                    {'nome': 'Defesa', 'descricao': 'Central Descaído', 'desig': 'DCL'},
                    {'nome': 'Defesa', 'descricao': 'Líbero Avançado', 'desig': 'L'},
                    {'nome': 'Defesa', 'descricao': 'Defesa Lateral', 'desig': 'DL'},
                    {'nome': 'Defesa', 'descricao': 'Ala', 'desig': 'AL'},
                    {'nome': 'Defesa', 'descricao': 'Defesa Lateral Descomplicado', 'desig': 'DLD'},
                    {'nome': 'Defesa', 'descricao': 'Ala Completo', 'desig': 'DLA'},
                    {'nome': 'Defesa', 'descricao': 'Defesa Ala Invertido', 'desig': 'DLI'},
                    
                    # Médio
                    {'nome': 'Médio', 'descricao': 'Médio Defensivo', 'desig': 'MD'},
                    {'nome': 'Médio', 'descricao': 'Construtor de Jogo Recuado', 'desig': 'MDR'},
                    {'nome': 'Médio', 'descricao': 'Médio Recuperador de Bolas', 'desig': 'MRB'},
                    {'nome': 'Médio', 'descricao': 'Trinco', 'desig': 'TR'},
                    {'nome': 'Médio', 'descricao': 'Pivô Defensivo', 'desig': 'PV'},
                    {'nome': 'Médio', 'descricao': 'Médio Criativo', 'desig': 'MC'},
                    {'nome': 'Médio', 'descricao': 'Organizador Móvel', 'desig': 'MCM'},
                    {'nome': 'Médio', 'descricao': 'Segundo Volante', 'desig': 'SV'},
                    {'nome': 'Médio', 'descricao': 'Médio Centro', 'desig': 'MC'},
                    {'nome': 'Médio', 'descricao': 'Médio Área-a-Área', 'desig': 'AA'},
                    {'nome': 'Médio', 'descricao': 'Construtor de Jogo Avançado', 'desig': 'CJA'},
                    {'nome': 'Médio', 'descricao': 'Mezzala', 'desig': 'MS'},
                    {'nome': 'Médio', 'descricao': 'Carrilero', 'desig': 'CR'},
                    {'nome': 'Médio', 'descricao': 'Médio Ofensivo', 'desig': 'MO'},
                    {'nome': 'Médio', 'descricao': 'Número 10', 'desig': 'N10'},
                    {'nome': 'Médio', 'descricao': 'Pivô Ofensivo', 'desig': 'PO'},
                    {'nome': 'Médio', 'descricao': 'Avançado Sombra', 'desig': 'AVS'},
                    {'nome': 'Médio', 'descricao': 'Médio Ala', 'desig': 'MA'},
                    
                    # Avançado
                    {'nome': 'Avançado', 'descricao': 'Extremo Direito', 'desig': 'ED'},
                    {'nome': 'Avançado', 'descricao': 'Extremo Esquerdo', 'desig': 'EE'},
                    {'nome': 'Avançado', 'descricao': 'Organizador Aberto', 'desig': 'OA'},
                    {'nome': 'Avançado', 'descricao': 'Extremo Invertido', 'desig': 'EI'},
                    {'nome': 'Avançado', 'descricao': 'Avançado Interior', 'desig': 'AI'},
                    {'nome': 'Avançado', 'descricao': 'Avançado de Referência', 'desig': 'ALR'},
                    {'nome': 'Avançado', 'descricao': 'Ponta de Lança Aberto', 'desig': 'PLA'},
                    {'nome': 'Avançado', 'descricao': 'Avançado Recuado', 'desig': 'AR'},
                    {'nome': 'Avançado', 'descricao': 'Falso Nove', 'desig': 'FN'},
                    {'nome': 'Avançado', 'descricao': 'Ponta-de-Lança', 'desig': 'PL'},
                    {'nome': 'Avançado', 'descricao': 'Ponta-de-Lança Fixo', 'desig': 'PLF'},
                    {'nome': 'Avançado', 'descricao': 'Avançado Completo', 'desig': 'AF'}
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
                        'alcunhas': "Santa",
                        'pais': "Portugal",
                        'cidade': "Santa Cruz da Trapa - São Pedro do Sul",
                        'estado': "Ativo",
                        'associacao': associacoes[0],  # Associação de Futebol de Viseu
                        'estadio': estadios[25]
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
                        'associacao': associacoes[13],  # Associação de Futebol de Lisboa
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
                        'associacao': associacoes[13],  # Associação de Futebol de Lisboa
                        'estadio': estadios[1]  # Estádio do Sport Lisboa e Benfica
                    },
                    {
                        'nome': "Porto",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/9_imgbank_1728921003.png",
                        'ano_fundacao': 1893,
                        'ano_extinto': 0,
                        'alcunhas': "Dragões, Azuis e Brancos, Portistas",
                        'pais': "Portugal",
                        'cidade': "Porto",
                        'estado': "Ativo",
                        'associacao': associacoes[17],  
                        'estadio': estadios[6]  
                    },
                    {
                        'nome': "SC Braga",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/15_imgbank_1682583585.png",
                        'ano_fundacao': 1921,
                        'ano_extinto': 0,
                        'alcunhas': "Arsenalistas, Guerreiros do Minho",
                        'pais': "Portugal",
                        'cidade': "Braga",
                        'estado': "Ativo",
                        'associacao': associacoes[6],  
                        'estadio': estadios[7]  
                    },
                    {
                        'nome': "Santa Clara",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas_a_data/4199_logo__20240712101624.png",
                        'ano_fundacao': 1921,
                        'ano_extinto': 0,
                        'alcunhas': "Bravos Açorianos",
                        'pais': "Portugal",
                        'cidade': "Ponta Delgada",
                        'estado': "Ativo",
                        'associacao': associacoes[15],  
                        'estadio': estadios[8]  
                    },
                    {
                        'nome': "Casa Pia",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/2412_imgbank_1695724045.png",
                        'ano_fundacao': 1920,
                        'ano_extinto': 0,
                        'alcunhas': "Gansos , Casapianos",
                        'pais': "Portugal",
                        'cidade': "Lisboa",
                        'estado': "Ativo",
                        'associacao': associacoes[13],  
                        'estadio': estadios[9]  
                    },
                    {
                        'nome': "Estoril Praia",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/1734_imgbank_1682584220.png",
                        'ano_fundacao': 1939,
                        'ano_extinto': 0,
                        'alcunhas': "Mágico, Estorilistas, Canarinhos, Equipa da Linha ",
                        'pais': "Portugal",
                        'cidade': "Estoril",
                        'estado': "Ativo",
                        'associacao': associacoes[13],  
                        'estadio': estadios[11]  
                    },
                    {
                        'nome': "Vitoria SC",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/18_imgbank_1691672368.png",
                        'ano_fundacao': 1922,
                        'ano_extinto': 0,
                        'alcunhas': "Vitorianos, Os Conquistadores",
                        'pais': "Portugal",
                        'cidade': "Guimarães",
                        'estado': "Ativo",
                        'associacao': associacoes[6],  
                        'estadio': estadios[10]  
                    },
                    {
                        'nome': "Famalicão",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/2175_imgbank_1682583693.png",
                        'ano_fundacao': 1931,
                        'ano_extinto': 0,
                        'alcunhas': "Famalicenses",
                        'pais': "Portugal",
                        'cidade': "Vila Nova de Famalicão",
                        'estado': "Ativo",
                        'associacao': associacoes[6],  
                        'estadio': estadios[12]  
                    },
                    {
                        'nome': "Rio Ave",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/31_imgbank_1682584600.png",
                        'ano_fundacao': 1939,
                        'ano_extinto': 0,
                        'alcunhas': "Vilacondenses; Rioavistas",
                        'pais': "Portugal",
                        'cidade': "Vila do Conde",
                        'estado': "Ativo",
                        'associacao': associacoes[17],  
                        'estadio': estadios[13]  
                    },
                     {
                        'nome': "Moreirense",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/6_imgbank_1682585615.png",
                        'ano_fundacao': 1938,
                        'ano_extinto': 0,
                        'alcunhas': "Cónegos, Moreira",
                        'pais': "Portugal",
                        'cidade': "Guimarães",
                        'estado': "Ativo",
                        'associacao': associacoes[6],  
                        'estadio': estadios[14]  
                    },
                    {
                        'nome': "Gil Vicente",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/11_imgbank_1682582593.png",
                        'ano_fundacao': 1924,
                        'ano_extinto': 0,
                        'alcunhas': "Gilistas, Galos de Barcelos",
                        'pais': "Portugal",
                        'cidade': "Barcelos",
                        'estado': "Ativo",
                        'associacao': associacoes[6],  
                        'estadio': estadios[15]  
                    },
                    {
                        'nome': "Arouca",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/3555_imgbank_1682582864.png",
                        'ano_fundacao': 1952,
                        'ano_extinto': 0,
                        'alcunhas': "Lobos de Arouca, Arouquenses",
                        'pais': "Portugal",
                        'cidade': "Arouca",
                        'estado': "Ativo",
                        'associacao': associacoes[1],  
                        'estadio': estadios[16]  
                    },
                    {
                        'nome': "Nacional",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/27_imgbank_1682588574.png",
                        'ano_fundacao': 1910,
                        'ano_extinto': 0,
                        'alcunhas': "Alvinegros, Insulares",
                        'pais': "Portugal",
                        'cidade': "Funchal ",
                        'estado': "Ativo",
                        'associacao': associacoes[14],  
                        'estadio': estadios[17]  
                    },
                    {
                        'nome': "AFS",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/296012_imgbank_1730118268.png",
                        'ano_fundacao': 2023,
                        'ano_extinto': 0,
                        'alcunhas': "Aves",
                        'pais': "Portugal",
                        'cidade': "Vila das Aves ",
                        'estado': "Ativo",
                        'associacao': associacoes[17],  
                        'estadio': estadios[18]  
                    },
                    {
                        'nome': "Est. Amadora",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/253884_imgbank_1691766850.png",
                        'ano_fundacao': 1932,
                        'ano_extinto': 0,
                        'alcunhas': "Tricolores, Estrelistas",
                        'pais': "Portugal",
                        'cidade': "Amadora",
                        'estado': "Ativo",
                        'associacao': associacoes[13],  
                        'estadio': estadios[19]  
                    },
                    {
                        'nome': "Farense",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/10_imgbank_1682585361.png",
                        'ano_fundacao': 1910,
                        'ano_extinto': 0,
                        'alcunhas': "Leões de Faro",
                        'pais': "Portugal",
                        'cidade': "Faro",
                        'estado': "Ativo",
                        'associacao': associacoes[3],  
                        'estadio': estadios[20]  
                    },
                    {
                        'nome': "Boavista",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/5_imgbank_1683106885.png",
                        'ano_fundacao': 1903,
                        'ano_extinto': 0,
                        'alcunhas': "Axadrezados, Panteras Negras",
                        'pais': "Portugal",
                        'cidade': "Porto",
                        'estado': "Ativo",
                        'associacao': associacoes[17],  
                        'estadio': estadios[21]  
                    },
                    
                    {
                        'nome': "CDDrizes",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/68/15068_logo_drizes.gif",
                        'ano_fundacao': 1962,
                        'ano_extinto': 2015,
                        'pais': "Portugal",
                        'cidade': "Sao Pedro do Sul",
                        'estado': "Extinto",
                        'associacao': associacoes[0],  
                        'estadio': estadios[26]  
                    },
                    
                    {
                        'nome': "UD Sampedrense",
                        'imagem': "https://www.zerozero.pt/img/logos/equipas/6700_imgbank_1709044943.png",
                        'ano_fundacao': 1946,
                        'ano_extinto': 0,
                        'pais': "Portugal",
                        'cidade': "Sao Pedro do Sul",
                        'estado': "Ativo",
                        'associacao': associacoes[0],  
                        'estadio': estadios[26]  
                    },
                ]
                
                clubes = [P_Clube.objects.create(**data) for data in clubes_data]
                self.stdout.write(self.style.SUCCESS(f'{len(clubes)} Clubes created'))
                

                # Inserir Equipas
                equipas_data = [
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[0],  # CD Santacruzense
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Extinto",
                        'clube': clubes[1],  # Naval
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[2],  # Naval 1893
                    },
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
                        'clube': clubes[3],  # Sporting
                    },
                    {
                        'nome': "Jun.A S19",
                        'estado': "Ativo",
                        'clube': clubes[3],  
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[5],  # Porto
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[6],  # SC Braga
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[7],  # Santa Clara
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[8],  # Casa Pia
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[9],  # Estoril Praia
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[10], # Vitória SC
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[11], # Famalicão
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[12], # Rio Ave
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[13], # Moreirense
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[14], # Gil Vicente
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[15], # Arouca
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[16], # Nacional
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[17], # AFS
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[18], # Est. Amadora
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[19], # Farense
                    },
                    {
                        'nome': "Equipa Principal",
                        'estado': "Ativo",
                        'clube': clubes[20], # Boavista
                    },
                ]

                equipas = [P_Equipa.objects.create(**data) for data in equipas_data]
                self.stdout.write(self.style.SUCCESS(f'{len(equipas)} Equipas created'))

                
                # Inserir Formato Competição
                ## Valor de Mercado: se não houver, metes zero (para garantir que não dá erro) e é em milhões
                formatosComp_data = [
                    {
                        'nome': "Liga ",
                        'descricao': "Liga Portuguesa",
                        'valor_de_mercado': 1980,
                    },
                    {
                        'nome': "Taça",
                        'descricao': "Taça de Portugual",
                        'valor_de_mercado': 1980,
                    },
                    {
                        'nome': "Taça da Liga",
                        'descricao': "Taça da Liga",
                        'valor_de_mercado': 1980,
                    },
                ]
                
                formatosComp = [P_FormatoCompeticao.objects.create(**data) for data in formatosComp_data]
                self.stdout.write(self.style.SUCCESS(f'{len(formatosComp)} Formatos Competição created'))
                
                # Inserir Competição
                ## Vencedor: coloca-se None se não houver
                competicoes_data = [
                    {
                        'nome': "Liga Portuguesa 2024-2025",
                        'imagem': "https://upload.wikimedia.org/wikipedia/commons/5/5a/S%C3%ADmbolo_da_Liga_Portuguesa_de_Futebol_Profissional.png",
                        'data_inicio': datetime(2024, 8, 17).date(),
                        'data_fim': datetime(2025, 6, 29).date(),
                        'finalizado': False,
                        'formato': formatosComp[0],  # Formato Liga Portuguesa
                    },
                    {
                        'nome': "Taça da Liga 2024",
                        'data_inicio': datetime(2024, 8, 17).date(),
                         'imagem': "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/S%C3%ADmbolo_da_Allianz_Cup.png/800px-S%C3%ADmbolo_da_Allianz_Cup.png",                      
                        'data_fim': datetime(2024, 12, 29).date(),
                        'finalizado': True,
                        'formato': formatosComp[2],  # Formato Liga Portuguesa
                        'vencedor': clubes[4],  # Clube Naval 1893
                    },
                ]

                # Criar as competições
                competicoes = [P_Competicao.objects.create(**data) for data in competicoes_data]
                self.stdout.write(self.style.SUCCESS(f'{len(competicoes)} Competições criadas'))
                                
                
                # Inserir Jogador
                ## Situação: Ativo / Lesionado / Expulso / Sem Clube / Retirado /Falecido
                ## As chaves estrangeiras que não tiver, coloca-se None
                ## Altura em cm, Valor de Mercado em milhões
                jogadores_data = [
                    {
                        'nome': "Marco Vicente Rodrigues",
                        'idade': 20,
                        'imagem': "https://lh3.googleusercontent.com/pw/AP1GczOhRWLfVhuSlZeqBsd7Y0CYoJV7ub68l8zg4EOAmRL1NiY_b-tkSw4Cszs5W2NdZ-6nBwXZvHCC0NKysMewwj2LRSYudkvakCCo5yoeGwYJZC-viSeGK8TRI-55sq7ffk81uKj7ha-z0ZKl8JMQNAQKCg=w604-h841-s-no?authuser=0" ,
                        'altura': 177,
                        'peso': 70.5,
                        'nacionalidade': "Portugal",
                        'num_camisola': 10, 
                        'valor_de_mercado': 99999.0,
                        'situacao': "Ativo",
                        'clube': clubes[0], 
                        'posicao': posicoes[26], 
                        'equipa': equipas[0], 
                    },
                    {
                        'nome': "Gigi Donnarumma",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/07/22/450722_gigi_donnarumma_20241012233112.png" ,
                        'altura': 196,
                        'peso': 92.5,
                        'nacionalidade': "Italia",
                        'num_camisola': 1, 
                        'valor_de_mercado': 36.0,
                        'situacao': "Ativo",
                        'clube': clubes[0], 
                        'posicao': posicoes[0], 
                        'equipa': equipas[0], 
                    },
                    {
                        'nome': "João Ricardo",
                        'idade': 17,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png" ,
                        'altura': 191,
                        'peso': 88.3,
                        'nacionalidade': "Portugal",
                        'num_camisola': 99, 
                        'situacao': "Ativo",
                        'clube': clubes[0], 
                        'posicao': posicoes[0], 
                        'equipa': equipas[0], 
                    },
                    {
                        'nome': "Ruben Dias",
                        'idade': 27,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/52/70/155270_ruben_dias_20240816210746.png" ,
                        'altura': 187,
                        'peso': 82.5,
                        'nacionalidade': "Portugal",
                        'num_camisola': 6, 
                        'valor_de_mercado': 72.0,
                        'situacao': "Ativo",
                        'clube': clubes[0], 
                        'posicao': posicoes[2], 
                        'equipa': equipas[0], 
                    },
                    {
                        'nome': "Luís Covelo",
                        'idade': 17,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png" ,
                        'altura': 181,
                        'peso': 79.3,
                        'nacionalidade': "Portugal",
                        'num_camisola': 3, 
                        'situacao': "Ativo",
                        'clube': clubes[0], 
                        'posicao': posicoes[2], 
                        'equipa': equipas[0], 
                    },
                    {
                        'nome': "Antonio Silva",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/04/96/490496_antonio_silva_20241012232544.jpg" ,
                        'altura': 187,
                        'peso': 81.3,
                        'nacionalidade': "Portugal",
                        'num_camisola': 4, 
                        'valor_de_mercado': 37.0,
                        'situacao': "Ativo",
                        'clube': clubes[0], 
                        'posicao': posicoes[2], 
                        'equipa': equipas[0], 
                    },
                    {
                        'nome': "Guilherme Lopes",
                        'idade': 26,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 18, 
                        'situacao': "Ativo",
                        'clube': clubes[0], 
                        'posicao': posicoes[8], 
                        'equipa': equipas[0], 
                    },
                    {
                        'nome': "Joel Duarte",
                        'idade': 14,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 18, 
                        'situacao': "Ativo",
                        'clube': clubes[0], 
                        'posicao': posicoes[8], 
                        'equipa': equipas[0], 
                    },
                      # Defesas Centrais (2)
                    {
                        'nome': "Rafael Costa",
                        'idade': 26,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 188,
                        'peso': 84.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 3,
                        'valor_de_mercado': 18.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[2],  # Defesa Central (DC)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Tiago Mendes",
                        'idade': 24,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 190,
                        'peso': 82.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 4,
                        'valor_de_mercado': 20.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[2],  # Defesa Central (DC)
                        'equipa': equipas[0],
                    },

                    # Defesas Laterais (4: 2 esquerdos e 2 direitos)
                    {
                        'nome': "Miguel Tavares",
                        'idade': 22,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 178,
                        'peso': 75.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 5,
                        'valor_de_mercado': 12.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[7],  # Defesa Lateral (DL)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "André Gomes",
                        'idade': 23,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 180,
                        'peso': 77.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 6,
                        'valor_de_mercado': 14.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[7],  # Defesa Lateral (DL)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Bruno Fernandes",
                        'idade': 25,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 176,
                        'peso': 74.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 2,
                        'valor_de_mercado': 15.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[7],  # Defesa Lateral (DL)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Carlos Rocha",
                        'idade': 27,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 179,
                        'peso': 76.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 22,
                        'valor_de_mercado': 16.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[7],  # Defesa Lateral (DL)
                        'equipa': equipas[0],
                    },

                    # Médios (6)
                    {
                        'nome': "Diogo Silva",
                        'idade': 24,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 182,
                        'peso': 78.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 8,
                        'valor_de_mercado': 20.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[12],  # Médio Defensivo (MD)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Eduardo Castro",
                        'idade': 26,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 180,
                        'peso': 77.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 10,
                        'valor_de_mercado': 22.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[17],  # Organizador Móvel (MCM)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Filipe Oliveira",
                        'idade': 23,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 178,
                        'peso': 75.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 14,
                        'valor_de_mercado': 18.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[14],  # Médio Recuperador de Bolas (MRB)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Gonçalo Martins",
                        'idade': 25,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 181,
                        'peso': 79.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 16,
                        'valor_de_mercado': 24.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[21],  # Médio Área-a-Área (AA)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Hugo Almeida",
                        'idade': 22,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 183,
                        'peso': 80.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 18,
                        'valor_de_mercado': 19.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[23],  # Mezzala (MS)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Ivo Costa",
                        'idade': 27,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 185,
                        'peso': 82.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 20,
                        'valor_de_mercado': 21.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[25],  # Médio Ofensivo (MO)
                        'equipa': equipas[0],
                    },

                    # Avançados (6: 1 ponta-de-lança, 4 extremos, 1 avançado completo)
                    {
                        'nome': "João Silva",
                        'idade': 28,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 187,
                        'peso': 83.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 9,
                        'valor_de_mercado': 25.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[39],  # Ponta-de-Lança (PL)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Luís Fernandes",
                        'idade': 24,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 179,
                        'peso': 76.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 7,
                        'valor_de_mercado': 18.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[30],  # Extremo Direito (ED)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Miguel Santos",
                        'idade': 23,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 178,
                        'peso': 75.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 11,
                        'valor_de_mercado': 17.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[30],  # Extremo Direito (ED)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Nuno Costa",
                        'idade': 25,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 180,
                        'peso': 77.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 17,
                        'valor_de_mercado': 19.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[31],  # Extremo Esquerdo (EE)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Pedro Alves",
                        'idade': 22,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 181,
                        'peso': 78.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 19,
                        'valor_de_mercado': 20.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[31],  # Extremo Esquerdo (EE)
                        'equipa': equipas[0],
                    },
                    {
                        'nome': "Ricardo Pereira",
                        'idade': 26,
                        'imagem': "https://cdn-icons-png.flaticon.com/512/46/46637.png",
                        'altura': 184,
                        'peso': 80.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 21,
                        'valor_de_mercado': 22.0,
                        'situacao': "Ativo",
                        'clube': clubes[0],
                        'posicao': posicoes[41],  # Avançado Completo (AF)
                        'equipa': equipas[0],
                    },
                    
                    
                    
                    
                    {
                        'nome': "Viktor Gyökeres",
                        'idade': 26,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/39/56/473956_viktor_gyokeres_20250118232350.png" ,
                        'altura': 189,
                        'peso': 90.0,
                        'nacionalidade': "Suécia",
                        'num_camisola': 9, 
                        'valor_de_mercado': 77.0,
                        'situacao': "Ativo",
                        'clube': clubes[3], # Clube Sporting
                        'posicao': posicoes[39], # Posição Avançado (Ponta de Lança)
                        'equipa': equipas[5], # Equipa Principal Sporting
                    },
                    
                    {

                        'nome': "António Adán",
                        'idade': 36,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/83/33/38333_antonio_adan_20241029170259.jpg",
                        'altura': 188,
                        'peso': 85.0,
                        'nacionalidade': "Espanha",
                        'num_camisola': 1,
                        'valor_de_mercado': 2.5,
                        'situacao': "Ativo",
                        'clube': clubes[3],  # Sporting
                        'posicao': posicoes[0],  # Guarda-Redes (GR)
                        'equipa': equipas[5],  # Equipa 5

                    },

                    {

                        'nome': "Gonçalo Inácio",
                        'idade': 22,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/41/59/384159_goncalo_inacio_20241027010748.png",
                        'altura': 185,
                        'peso': 78.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 15,
                        'valor_de_mercado': 20.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[2],  # Defesa Central (DC)
                        'equipa': equipas[5],

                    },

                    {
                        'nome': "Matheus Reis",
                        'idade': 28,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/57/02/395702_matheus_reis_20240812161006.jpg",
                        'altura': 180,
                        'peso': 75.0,
                        'nacionalidade': "Brasil",
                        'num_camisola': 3,
                        'valor_de_mercado': 10.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[7],  # Defesa Lateral (DL)
                        'equipa': equipas[5],

                    },

                    {

                        'nome': "Pedro Gonçalves",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/83/88/338388_pedro_goncalves_20240812160800.jpg",
                        'altura': 180,
                        'peso': 77.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 28,
                        'valor_de_mercado': 30.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[17],  # Médio Criativo (MC)
                        'equipa': equipas[5],

                    },

                    {

                        'nome': "João Palhinha",
                        'idade': 28,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/11/16/211116_joao_palhinha_20241031110257.png",
                        'altura': 185,
                        'peso': 80.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 6,
                        'valor_de_mercado': 25.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[12],  # Médio Defensivo (MD)
                        'equipa': equipas[5],

                    },

                    {

                        'nome': "Nuno Santos",
                        'idade': 27,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/08/73/160873_nuno_santos_20240729155308.jpg",
                        'altura': 178,
                        'peso': 74.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 19,
                        'valor_de_mercado': 18.0,
                        'situacao': "Lesionado",
                        'clube': clubes[3],
                        'posicao': posicoes[30],  # Extremo Direito (ED)
                        'equipa': equipas[5],

                    },

                    {

                        'nome': "Paulinho",
                        'idade': 29,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/90/04/189004_paulinho_20241024123451.png",
                        'altura': 182,
                        'peso': 85.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 21,
                        'valor_de_mercado': 20.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[39],  # Ponta-de-Lança (PL)
                        'equipa': equipas[5],

                    },

                    {
                        'nome': "Tiago Tomás",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/81/416481_20230929134124_tiago_tomas.png",
                        'altura': 180,
                        'peso': 72.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 17,
                        'valor_de_mercado': 15.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[28],  # Avançado Sombra (AVS)
                        'equipa': equipas[5],

                    },

                    {

                        'nome': "Matheus Nunes",
                        'idade': 24,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/41/99/564199_matheus_nunes_20240816210213.png",
                        'altura': 182,
                        'peso': 80.0,
                        'nacionalidade': "Brasil",
                        'num_camisola': 8,
                        'valor_de_mercado': 30.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[20],  # Médio Centro (MC)
                        'equipa': equipas[5],

                    },

                    {

                        'nome': "Daniel Bragança",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/48/50/84850_daniel_braganca_20240812161107.jpg",
                        'altura': 180,
                        'peso': 75.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 10,
                        'valor_de_mercado': 12.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[18],  # Organizador Móvel (MCM)
                        'equipa': equipas[5],

                    },

                    {
                        'nome': "Jovane Cabral",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/13/96/461396_jovane_cabral_20250120231132.png",
                        'altura': 175,
                        'peso': 70.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 77,
                        'valor_de_mercado': 15.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[31],  # Extremo Esquerdo (EE)
                        'equipa': equipas[5],

                    },

                    {
                        'nome': "Nuno Mendes",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/41/64/384164_nuno_mendes_20241012232838.png",
                        'altura': 178,
                        'peso': 70.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 29,
                        'valor_de_mercado': 25.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[9],  # Defesa Lateral Descomplicado (DLD)
                        'equipa': equipas[5],

                    },

                    {
                        'nome': "Eduardo Quaresma",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/05/17/160517_eduardo_quaresma_20240812161817.jpg",
                        'altura': 185,
                        'peso': 80.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 4,
                        'valor_de_mercado': 18.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[2],  # Defesa Central (DC)
                        'equipa': equipas[5],

                    },


                    {

                        'nome': "Francisco Trincão",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/02/56/500256_francisco_trincao_20240812160208.jpg",
                        'altura': 180,
                        'peso': 72.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 7,
                        'valor_de_mercado': 20.0,
                        'situacao': "Ativo",
                        'clube': clubes[3],
                        'posicao': posicoes[30],  # Extremo Direito (ED)
                        'equipa': equipas[5],

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
                        'posicao': posicoes[30], # Posição Avançado (Extrema Direita)
                        'equipa': equipas[3], # Equipa Principal Sporting
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
                        'posicao': posicoes[12], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    {
                        'nome': "Anatoliy Trubin",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/40/58/594058_anatoliy_trubin_20250103092031.png" ,
                        'altura': 199,
                        'peso': 86.0,
                        'nacionalidade': "Ucrânia",
                        'num_camisola': 1, 
                        'valor_de_mercado': 24.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[0], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    
                    {
                        'nome': "Alexander Bah",
                        'idade': 27,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/30/06/523006_alexander_bah_20240807131232.jpg" ,
                        'altura': 183,
                        'peso': 77.0,
                        'nacionalidade': "Dinamarca",
                        'num_camisola': 6, 
                        'valor_de_mercado': 14.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[7], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    
                    {
                        'nome': "Nicolás Otamendi",
                        'idade': 36,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/75/88/67588_nicolas_otamendi_20250103092114.png" ,
                        'altura': 183,
                        'peso': 80.0,
                        'nacionalidade': "Argentina",
                        'num_camisola':30, 
                        'valor_de_mercado': 1.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[2], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    
                    {
                        'nome': "Tomás Araújo",
                        'idade': 22,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/03/53/520353_tomas_araujo_20240807131554.jpg" ,
                        'altura': 187,
                        'peso': 81.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':44, 
                        'valor_de_mercado': 29.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[2], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    
                    {
                        'nome': "Álvaro Carreras",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/53/05/825305_alvaro_carreras_20240807130155.jpg" ,
                        'altura': 186,
                        'peso': 78.0,
                        'nacionalidade': "Espanha",
                        'num_camisola':3, 
                        'valor_de_mercado': 19.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[7], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    
                    {
                        'nome': "Florentino Luís",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/62/29/166229_florentino_luis_20240807130919.jpg" ,
                        'altura': 184,
                        'peso': 76.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':61, 
                        'valor_de_mercado': 19.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[12], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    
                    {
                        'nome': "Andreas Schjelderup",
                        'idade': 20,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/18/85/741885_andreas_schjelderup_20250111235523.png" ,
                        'altura': 176,
                        'peso': 69.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':21, 
                        'valor_de_mercado': 10.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[30], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    
                    {
                        'nome': "Zeki Amdouni",
                        'idade': 24,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/46/54/724654_zeki_amdouni__20240930104822.jpg" ,
                        'altura': 186,
                        'peso': 79.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':7, 
                        'valor_de_mercado': 16.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[37], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    
                                        
                    {
                        'nome': "Renato Sanches",
                        'idade': 27,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/52/84/155284_renato_sanches_20240813093549.jpg" ,
                        'altura': 176,
                        'peso': 73.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':85, 
                        'valor_de_mercado': 5.0,
                        'situacao': "Lesionado",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[20], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    
                    {
                        'nome': "Leandro Barreiro",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/12/76/591276_leandro_barreiro_20240807130229.jpg" ,
                        'altura': 174,
                        'peso': 67.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':18, 
                        'valor_de_mercado': 14.0,
                        'situacao': "Ativo",
                        'clube': clubes[4], # Clube Benfica
                        'posicao': posicoes[20], # Posição Médio (Médio Defensivo)
                        'equipa': equipas[3], # Equipa Principal Sporting
                    },
                    
                    
                                        
                    {
                        'nome': "Diogo Costa",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/44/06/284406_diogo_costa_20240731174246.png" ,
                        'altura': 186,
                        'peso': 82.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':99, 
                        'valor_de_mercado': 41.0,
                        'situacao': "Ativo",
                        'clube': clubes[5], 
                        'posicao': posicoes[0],
                        'equipa': equipas[7],
                    },
                    
                    
                    {
                        'nome': "João Mário",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/12/83/421283_joao_mario_20240731174919.png" ,
                        'altura': 178,
                        'peso': 66.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':23, 
                        'valor_de_mercado': 14.0,
                        'situacao': "Ativo",
                        'clube': clubes[5], 
                        'posicao': posicoes[7],
                        'equipa': equipas[7],
                    },
                    
                    
                    {
                        'nome': "Iván Marcano",
                        'idade': 37,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/67/73/36773_ivan_marcano_20240731175356.png" ,
                        'altura': 189,
                        'peso': 92.0,
                        'nacionalidade': "Espanha",
                        'num_camisola':5, 
                        'valor_de_mercado': 1.0,
                        'situacao': "Lesionado",
                        'clube': clubes[5], 
                        'posicao': posicoes[2],
                        'equipa': equipas[7],
                    },
                    
                    
                    {
                        'nome': "Zé Pedro",
                        'idade': 27,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/68/87/226887_ze_pedro_20240731175509.png" ,
                        'altura': 187,
                        'peso': 84.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':97, 
                        'valor_de_mercado': 3.0,
                        'situacao': "Ativo",
                        'clube': clubes[5], 
                        'posicao': posicoes[2],
                        'equipa': equipas[7],
                    },
                    
                    

                    
                    
                    {
                        'nome': "Vasco Sousa",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/94/45/529445_vasco_sousa_20240731175251.png" ,
                        'altura': 169,
                        'peso': 64.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':15, 
                        'valor_de_mercado': 5.0,
                        'situacao': "Ativo",
                        'clube': clubes[5], 
                        'posicao': posicoes[20],
                        'equipa': equipas[7],
                    },
             
             
                                 
                    {
                        'nome': "Gonçalo Borges",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/83/78/428378_goncalo_borges_20240731174604.png" ,
                        'altura': 184,
                        'peso': 69.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':70, 
                        'valor_de_mercado': 4.0,
                        'situacao': "Ativo",
                        'clube': clubes[5], 
                        'posicao': posicoes[30],
                        'equipa': equipas[7],
                    },
                    
                    {
                        'nome': "Samu Aghehowa",
                        'idade': 20,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/22/94/1182294_samu_omorodion_20240828172835.png" ,
                        'altura': 193,
                        'peso': 90.0,
                        'nacionalidade': "Espanha",
                        'num_camisola':14, 
                        'valor_de_mercado': 50.0,
                        'situacao': "Ativo",
                        'clube': clubes[5], 
                        'posicao': posicoes[39],
                        'equipa': equipas[7],
                    },
                    
                    
                    {
                        'nome': "Matheus Magalhães",
                        'idade': 32,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/70/75/147075_matheus_magalhaes_20240816114204.png" ,
                        'altura': 190,
                        'peso': 86.0,
                        'nacionalidade': "Brasil",
                        'num_camisola': 1, 
                        'valor_de_mercado': 5.0,
                        'situacao': "Ativo",
                        'clube': clubes[6], 
                        'posicao': posicoes[0],
                        'equipa': equipas[8],
                    },
                    
                    {
                        'nome': "João Moutinho",
                        'idade': 38,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/76/08/7608_joao_moutinho_20241019235352.png" ,
                        'altura': 170,
                        'peso': 63.0,
                        'nacionalidade': "Portugal",
                        'num_camisola': 8, 
                        'valor_de_mercado': 0.6,
                        'situacao': "Ativo",
                        'clube': clubes[6], 
                        'posicao': posicoes[20],
                        'equipa': equipas[8],
                    },
                    
                    
                    {
                        'nome': "Ricardo Horta",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/49/52/74952_ricardo_horta_20240722153939.jpg" ,
                        'altura': 173,
                        'peso': 58.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':21, 
                        'valor_de_mercado': 12.6,
                        'situacao': "Ativo",
                        'clube': clubes[6], 
                        'posicao': posicoes[30],
                        'equipa': equipas[8],
                    },
                    
                    
                    {
                        'nome': "Bruma",
                        'idade': 30,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/43/12/74312_bruma_20240722153821.jpg" ,
                        'altura': 173,
                        'peso': 58.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':7, 
                        'valor_de_mercado': 10.6,
                        'situacao': "Ativo",
                        'clube': clubes[6], 
                        'posicao': posicoes[31],
                        'equipa': equipas[8],
                    },
                    
                    
                    
                    {
                        'nome': "Gabriel Batista",
                        'idade': 26,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/48/34/484834_gabriel_batista_20241218203725.png" ,
                        'altura': 190,
                        'peso': 83.0,
                        'nacionalidade': "Brasil",
                        'num_camisola':1, 
                        'valor_de_mercado': 1.6,
                        'situacao': "Ativo",
                        'clube': clubes[7], 
                        'posicao': posicoes[0],
                        'equipa': equipas[9],
                    },
                    
                    
                    {
                        'nome': "Luís Rocha",
                        'idade': 38,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/82/21/78221_luis_rocha_20241218205138.png" ,
                        'altura': 186,
                        'peso': 83.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':13, 
                        'situacao': "Ativo",
                        'clube': clubes[7], 
                        'posicao': posicoes[0],
                        'equipa': equipas[9],
                    },
                    
                    
                    {
                        'nome': "Luís Rocha",
                        'idade': 38,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/82/21/78221_luis_rocha_20241218205138.png" ,
                        'altura': 186,
                        'peso': 83.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':13, 
                        'situacao': "Ativo",
                        'clube': clubes[7], 
                        'posicao': posicoes[2],
                        'equipa': equipas[9],
                    },
                    
                    
                    
                    
                    {
                        'nome': "João Costa",
                        'idade': 24,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/26/21/592621_joao_costa_20241218204707.png" ,
                        'altura': 185,
                        'peso': 80.0,
                        'nacionalidade': "Portugal",
                        'num_camisola':17, 
                        'situacao': "Ativo",
                        'clube': clubes[7], 
                        'posicao': posicoes[39],
                        'equipa': equipas[9],
                    },
                    
                    
                    
                    {
                        'nome': "Vital Maia",
                        'idade': 17,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/78/68/1157868_vital_maia_20240813104653.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':7, 
                        'situacao': "Ativo",
                        'clube': clubes[7], 
                        'posicao': posicoes[31],
                        'equipa': equipas[9],
                    },
                    
                    
                    {
                        'nome': "Daniel Azevedo",
                        'idade': 26,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/48/80/164880_daniel_azevedo_20250120160505.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':22, 
                        'situacao': "Ativo",
                        'clube': clubes[8], 
                        'posicao': posicoes[0],
                        'equipa': equipas[10],
                    },
                    
                    
                    
                    
                    {
                        'nome': "José Fonte",
                        'idade': 41,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/55/37/15537_jose_fonte_20250120160723.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':6, 
                        'situacao': "Ativo",
                        'clube': clubes[8], 
                        'posicao': posicoes[2],
                        'equipa': equipas[10],
                    },
                    
                    
                    
                    {
                        'nome': "Nuno Moreira",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/48/49/84849_nuno_moreira_20250120161259.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':7, 
                        'situacao': "Ativo",
                        'clube': clubes[8], 
                        'posicao': posicoes[31],
                        'equipa': equipas[10],
                    },
                    
                    
                    
                    {
                        'nome': "Cassiano",
                        'idade': 35,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/49/74/144974_cassiano_20250120161408.png" ,
                        'nacionalidade': "Brasil",
                        'num_camisola':90, 
                        'situacao': "Ativo",
                        'clube': clubes[8], 
                        'posicao': posicoes[39],
                        'equipa': equipas[10],
                    },
                    
                    
                    
                    {
                        'nome': "João Oliveira",
                        'idade': 22,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/73/35/507335_joao_oliveira_20240813092726.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':47, 
                        'situacao': "Ativo",
                        'clube': clubes[10], 
                        'posicao': posicoes[0],
                        'equipa': equipas[12],
                    },
                    
                    
                    
                    {
                        'nome': "Miguel Maga",
                        'idade': 22,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/09/14/530914_miguel_maga_20240813092924.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':2, 
                        'situacao': "Ativo",
                        'clube': clubes[10], 
                        'posicao': posicoes[7],
                        'equipa': equipas[12],
                    },
                    
                    
                    {
                        'nome': "Rodrigo Silva",
                        'idade': 17,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/71/65/897165_rodrigo_silva_20250130234322.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':5, 
                        'situacao': "Ativo",
                        'clube': clubes[10], 
                        'posicao': posicoes[7],
                        'equipa': equipas[12],
                    },
                    
                    
                    
                    {
                        'nome': "Diogo Sousa",
                        'idade': 19,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/84/78/648478_diogo_sousa_20240904151251.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':92, 
                        'situacao': "Ativo",
                        'clube': clubes[10], 
                        'posicao': posicoes[14],
                        'equipa': equipas[12],
                    },
                    
                    
                    {
                        'nome': "Nuno Santos",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/52/67/375267_nuno_santos_20250118231834.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':77, 
                        'situacao': "Ativo",
                        'clube': clubes[10], 
                        'posicao': posicoes[25],
                        'equipa': equipas[12],
                    },
                    
                                        
                    {
                        'nome': "Jota silva",
                        'idade': 25,
                        'imagem': "https://livesport-ott-images.ssl.cdn.cra.cz/r900xfq60/2873a11d-c429-44de-a9d3-2a3e7a417eb6.jpeg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':77, 
                        'situacao': "Ativo",
                        'clube': clubes[10], 
                        'posicao': posicoes[39],
                        'equipa': equipas[12],
                    },
                    
                    
                    
                    {
                        'nome': "Diogo Dias",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/80/56/718056_diogo_dias_20240807145211.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':77, 
                        'situacao': "Ativo",
                        'clube': clubes[9], 
                        'posicao': posicoes[0],
                        'equipa': equipas[11],
                    },
                    
                    
                    {
                        'nome': "António Vital",
                        'idade': 18,
                        'imagem': "https://www.zerozero.pt/img/jogadores/85/879785_antonio_vital_1676859726.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':6, 
                        'situacao': "Ativo",
                        'clube': clubes[9], 
                        'posicao': posicoes[2],
                        'equipa': equipas[11],
                    },
                    
                    
                    {
                        'nome': "Pedro Álvaro",
                        'idade': 24,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/24/35/372435_pedro_alvaro_20240807150016.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':23, 
                        'situacao': "Ativo",
                        'clube': clubes[9], 
                        'posicao': posicoes[2],
                        'equipa': equipas[11],
                    },
                    
                    
                    {
                        'nome': "Pedro Amaral",
                        'idade': 27,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/52/69/155269_pedro_amaral_20240807150254.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':24, 
                        'situacao': "Ativo",
                        'clube': clubes[9], 
                        'posicao': posicoes[10],
                        'equipa': equipas[11],
                    },
                    
                    
                    {
                        'nome': "Xeka",
                        'idade': 30,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/55/78/175578_xeka_20240828174030.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':88, 
                        'situacao': "Ativo",
                        'clube': clubes[9], 
                        'posicao': posicoes[10],
                        'equipa': equipas[11],
                    },
                    
                    
                   {
                        'nome': "Gabriel Tavares",
                        'idade': 19,
                        'imagem': "https://www.zerozero.pt/img/jogadores/32/731732_20230927213331_gabriel_tavares.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':13, 
                        'situacao': "Ativo",
                        'clube': clubes[9], 
                        'posicao': posicoes[30],
                        'equipa': equipas[11],
                    },
                    
                    
                    {
                        'nome': "André Lacximicant",
                        'idade': 19,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/05/69/290569_andre_lacximicant_20240807145811.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':19, 
                        'situacao': "Ativo",
                        'clube': clubes[9], 
                        'posicao': posicoes[41],
                        'equipa': equipas[11],
                    },
                    
                    
                    
                    {
                        'nome': "Ivan Zlobin",
                        'idade': 27,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/68/11/376811_ivan_zlobin_20250201005601.png" ,
                        'nacionalidade': "Russia",
                        'num_camisola':1, 
                        'situacao': "Ativo",
                        'clube': clubes[11], 
                        'posicao': posicoes[0],
                        'equipa': equipas[13],
                    },
                    
                    
                    
                    
                    
                    
                   {
                        'nome': "Hugo Cunha",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/63/45/426345_hugo_cunha_20250201005526.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':90, 
                        'situacao': "Ativo",
                        'clube': clubes[11], 
                        'posicao': posicoes[0],
                        'equipa': equipas[13],
                    },
                    
                    
                    {
                        'nome': "José Müller",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/76/31/587631_jose_muller_20240923163731.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':62, 
                        'situacao': "Ativo",
                        'clube': clubes[11], 
                        'posicao': posicoes[2],
                        'equipa': equipas[13],
                    },
                    
                    
                    
                    {
                        'nome': "Rodrigo Pinheiro",
                        'idade': 22,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/94/40/529440_rodrigo_pinheiro_20250201003947.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':17, 
                        'situacao': "Ativo",
                        'clube': clubes[11], 
                        'posicao': posicoes[8],
                        'equipa': equipas[13],
                    },
                    
                    
                    
                    {
                        'nome': "Samuel Lobato",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/61/71/386171_samuel_lobato_20250201005115.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':88, 
                        'situacao': "Ativo",
                        'clube': clubes[11], 
                        'posicao': posicoes[25],
                        'equipa': equipas[13],
                    },
                    
                    
                    
                    {
                        'nome': "Gil Dias",
                        'idade': 28,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/82/21/368221_gil_dias_20250201005751.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':23, 
                        'situacao': "Ativo",
                        'clube': clubes[11], 
                        'posicao': posicoes[30],
                        'equipa': equipas[13],
                    },
                    
                    
                    
                    {
                        'nome': "Sorriso",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/11/47/691147_sorriso_20250201004527.png" ,
                        'nacionalidade': "Brasileiro",
                        'num_camisola':7, 
                        'situacao': "Ativo",
                        'clube': clubes[11], 
                        'posicao': posicoes[31],
                        'equipa': equipas[13],
                    },
                    
                    
                    
                    {
                        'nome': "Matheus Teixeira",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/72/94/547294_matheus_teixeira_20250120175024.png" ,
                        'nacionalidade': "Brasil",
                        'num_camisola':1, 
                        'situacao': "Ativo",
                        'clube': clubes[12], 
                        'posicao': posicoes[0],
                        'equipa': equipas[14],
                    },
                    
                    
                    
                    
                    {
                        'nome': "João Tomé",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/45/63/304563_joao_tome_20240809155344.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':20, 
                        'situacao': "Ativo",
                        'clube': clubes[12], 
                        'posicao': posicoes[7],
                        'equipa': equipas[14],
                    },
                    
                    
                                        
                    {
                        'nome': "João Novais",
                        'idade': 31,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/13/73/161373_joao_novais_20240809154454.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':6, 
                        'situacao': "Ativo",
                        'clube': clubes[12], 
                        'posicao': posicoes[27],
                        'equipa': equipas[14],
                    },
                    
                    
                    
                    {
                        'nome': "João Graça",
                        'idade': 29,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/08/69/160869_joao_graca_20240809155410.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':21, 
                        'situacao': "Ativo",
                        'clube': clubes[12], 
                        'posicao': posicoes[21],
                        'equipa': equipas[14],
                    },
                    
                    {
                        'nome': "Kiko Bondoso",
                        'idade': 29,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/00/64/370064_kiko_bondoso_20240809155325.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':19, 
                        'situacao': "Ativo",
                        'clube': clubes[12], 
                        'posicao': posicoes[31],
                        'equipa': equipas[14],
                    },
                    
                    
                    
                    {
                        'nome': "Mika",
                        'idade': 33,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/53/55/85355_mika_20240812152400.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':16, 
                        'situacao': "Ativo",
                        'clube': clubes[13], 
                        'posicao': posicoes[0],
                        'equipa': equipas[15],
                    },
                    
                    
                                       
                    {
                        'nome': "Dinis Pinto",
                        'idade': 24,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/26/16/532616_dinis_pinto_20240812152120.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':76, 
                        'situacao': "Ativo",
                        'clube': clubes[13], 
                        'posicao': posicoes[7],
                        'equipa': equipas[15],
                    },
                    
                    
                    
                    {
                        'nome': "Rúben Ismael",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/47/06/524706_ruben_ismael_20240812151940.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola':6, 
                        'situacao': "Ativo",
                        'clube': clubes[13], 
                        'posicao': posicoes[12],
                        'equipa': equipas[15],
                    },
                    
                    
                    
                    {
                        'nome': "Pedro Santos",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/76/38/587638_pedro_santos_20240812152447.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 21, 
                        'situacao': "Ativo",
                        'clube': clubes[13], 
                        'posicao': posicoes[30],
                        'equipa': equipas[15],
                    },
                    
                   

                    {
                        'nome': "Brian Araújo",
                        'idade': 24,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/44/46/474446_brian_araujo_20250120093725.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 99, 
                        'situacao': "Ativo",
                        'clube': clubes[14], 
                        'posicao': posicoes[0],
                        'equipa': equipas[16],
                    },
                    
                    
                    {
                        'nome': "Zé Carlos",
                        'idade': 26,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/18/01/221801_ze_carlos_20250120093826.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 2, 
                        'situacao': "Ativo",
                        'clube': clubes[14], 
                        'posicao': posicoes[7],
                        'equipa': equipas[16],
                    },
                    
                    {
                        'nome': "Gui Beleza",
                        'idade': 18,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/58/93/515893_gui_beleza_20250120094431.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 16, 
                        'situacao': "Ativo",
                        'clube': clubes[14], 
                        'posicao': posicoes[12],
                        'equipa': equipas[16],
                    },
                    
                    
                   {
                        'nome': "João Pinto",
                        'idade': 22,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/82/05/528205_joao_pinto_20250120094852.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 13, 
                        'situacao': "Ativo",
                        'clube': clubes[14], 
                        'posicao': posicoes[41],
                        'equipa': equipas[16],
                    },
                    
                    
                    
                    {
                        'nome': "João Valido",
                        'idade': 24,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/01/71/520171_joao_valido_20240807144211.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 1, 
                        'situacao': "Ativo",
                        'clube': clubes[15], 
                        'posicao': posicoes[1],
                        'equipa': equipas[17],
                    },
                    
                    
                    {
                        'nome': "Tiago Esgaio",
                        'idade': 29,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/21/97/282197_tiago_esgaio_20250118231600.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 1, 
                        'situacao': "Ativo",
                        'clube': clubes[15], 
                        'posicao': posicoes[7],
                        'equipa': equipas[17],
                    },
                    
                    
                    {
                        'nome': "Pedro Santos",
                        'idade': 24,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/59/09/545909_pedro_santos_20240807144800.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 89, 
                        'situacao': "Ativo",
                        'clube': clubes[15], 
                        'posicao': posicoes[28],
                        'equipa': equipas[17],
                    },
                    
                    
                    {
                        'nome': "Henrique Araújo",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/80/31/238031_henrique_araujo_20250201205757.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 39, 
                        'situacao': "Ativo",
                        'clube': clubes[15], 
                        'posicao': posicoes[39],
                        'equipa': equipas[17],
                    },
                    
                    
                    {
                        'nome': "Rui Encarnação",
                        'idade': 26,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/19/92/471992_rui_encarnacao_20250120092416.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 1, 
                        'situacao': "Ativo",
                        'clube': clubes[16], 
                        'posicao': posicoes[0],
                        'equipa': equipas[18],
                    },
                    
                    
                    {
                        'nome': "João Aurélio",
                        'idade': 36,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/55/60/5560_joao_aurelio_20250120092642.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 2, 
                        'situacao': "Ativo",
                        'clube': clubes[16], 
                        'posicao': posicoes[7],
                        'equipa': equipas[18],
                    },
                    
                    
                    {
                        'nome': "Jota Garcês",
                        'idade': 31,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/08/66/170866_jota_garces_20250120093142.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 31, 
                        'situacao': "Ativo",
                        'clube': clubes[16], 
                        'posicao': posicoes[20],
                        'equipa': equipas[18],
                    },
                    
                                        
                    {
                        'nome': "Rúben Macedo",
                        'idade': 28,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/08/99/160899_ruben_macedo_20250120093403.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 31, 
                        'situacao': "Ativo",
                        'clube': clubes[16], 
                        'posicao': posicoes[30],
                        'equipa': equipas[18],
                    },
                    
                    
                    {
                        'nome': "Guillermo Ochoa",
                        'idade': 39,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/69/11/26911_guillermo_ochoa_20250120000501.png" ,
                        'nacionalidade': "México",
                        'num_camisola': 1, 
                        'situacao': "Ativo",
                        'clube': clubes[17], 
                        'posicao': posicoes[0],
                        'equipa': equipas[19],
                    },
                    
                    
                    {
                        'nome': "Rafael Rodrigues",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/03/52/520352_rafael_rodrigues_20250120095441.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 3, 
                        'situacao': "Ativo",
                        'clube': clubes[17], 
                        'posicao': posicoes[7],
                        'equipa': equipas[19],
                    },


                    {
                        'nome': "Gustavo Mendonça",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/58/97/385897_gustavo_mendonca_20250120095915.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 23, 
                        'situacao': "Ativo",
                        'clube': clubes[17], 
                        'posicao': posicoes[15],
                        'equipa': equipas[19],
                    },
                    
                    {
                        'nome': "Rodrigo Ribeiro",
                        'idade': 19,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/46/09/664609_rodrigo_ribeiro_20250120000331.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 20, 
                        'situacao': "Ativo",
                        'clube': clubes[17], 
                        'posicao': posicoes[39],
                        'equipa': equipas[19],
                    },
                    
                    
                    
                    {
                        'nome': "Francisco Meixedo",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/57/40/505740_francisco_meixedo_20250120225953.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 1, 
                        'situacao': "Ativo",
                        'clube': clubes[18], 
                        'posicao': posicoes[0],
                        'equipa': equipas[20],
                    },
                    
                    
                    {
                        'nome': "Fábio Ronaldo",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/26/60/512660_fabio_ronaldo_20240809155531.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 7, 
                        'situacao': "Ativo",
                        'clube': clubes[18], 
                        'posicao': posicoes[7],
                        'equipa': equipas[20],
                    },
                    
                    
                    {
                        'nome': "Ferro",
                        'idade': 27,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/43/68/214368_ferro_20250120230056.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 4, 
                        'situacao': "Ativo",
                        'clube': clubes[18], 
                        'posicao': posicoes[2],
                        'equipa': equipas[20],
                    },
                    
                    {
                        'nome': "Diogo Travassos",
                        'idade': 20,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/23/51/182351_diogo_travassos_20250120230043.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 2, 
                        'situacao': "Ativo",
                        'clube': clubes[18], 
                        'posicao': posicoes[7],
                        'equipa': equipas[20],
                    },
                    
                    
                    {
                        'nome': "Rúben Lima",
                        'idade': 35,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/27/66/52766_ruben_lima_20250120230401.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 28, 
                        'situacao': "Ativo",
                        'clube': clubes[18], 
                        'posicao': posicoes[7],
                        'equipa': equipas[20],
                    },
                   
                   
                    {
                        'nome': "Paulo Moreira",
                        'idade': 35,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/12/94/421294_paulo_moreira_20250120230824.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 19, 
                        'situacao': "Ativo",
                        'clube': clubes[18], 
                        'posicao': posicoes[21],
                        'equipa': equipas[20],
                    },
                    
                    
                    {
                        'nome': "Kikas",
                        'idade': 26,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/59/55/385955_kikas_20250120231156.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 98, 
                        'situacao': "Ativo",
                        'clube': clubes[18], 
                        'posicao': posicoes[39],
                        'equipa': equipas[20],
                    },
                    
                    
                    {
                        'nome': "Ricado Velho",
                        'idade': 26,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/74/13/227413_ricardo_velho_20240729164546.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 33, 
                        'situacao': "Ativo",
                        'clube': clubes[19], 
                        'posicao': posicoes[0],
                        'equipa': equipas[21],
                    },
                    
                    {
                        'nome': "Artur Jorge",
                        'idade': 30,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/70/99/167099_artur_jorge_20240729165916.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 4, 
                        'situacao': "Ativo",
                        'clube': clubes[19], 
                        'posicao': posicoes[2],
                        'equipa': equipas[21],
                    },
                    
                    
                    {
                        'nome': "Zé Carlos",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/01/74/450174_ze_carlos_20250202231222.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 8, 
                        'situacao': "Ativo",
                        'clube': clubes[19], 
                        'posicao': posicoes[20],
                        'equipa': equipas[21],
                    },
                    
                    
                    {
                        'nome': "André Seruca",
                        'idade': 24,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/04/28/160428_andre_seruca_20240729165253.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 50, 
                        'situacao': "Ativo",
                        'clube': clubes[19], 
                        'posicao': posicoes[23],
                        'equipa': equipas[21],
                    },
                    
                    
                    
                    {
                        'nome': "Miguel Menino",
                        'idade': 22,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/52/36/155236_miguel_menino_20241221195917.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 93, 
                        'situacao': "Ativo",
                        'clube': clubes[19], 
                        'posicao': posicoes[24],
                        'equipa': equipas[21],
                    },
                    
                    
                    
                    
                    {
                        'nome': "Tiago Madeira",
                        'idade': 23,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/34/48/553448_tiago_madeira_20240729170140.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 20, 
                        'situacao': "Ativo",
                        'clube': clubes[19], 
                        'posicao': posicoes[37],
                        'equipa': equipas[21],
                    },
                    
                    
                   {
                        'nome': "Tomané",
                        'idade': 32,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/30/37/133037_tomane_20240729165759.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 9, 
                        'situacao': "Ativo",
                        'clube': clubes[19], 
                        'posicao': posicoes[39],
                        'equipa': equipas[21],
                    },
                    
                    {
                        'nome': "Tomané",
                        'idade': 32,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/30/37/133037_tomane_20240729165759.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 9, 
                        'situacao': "Ativo",
                        'clube': clubes[19], 
                        'posicao': posicoes[39],
                        'equipa': equipas[21],
                    },
                    
                    {
                        'nome': "Tomé Sousa",
                        'idade': 18,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/65/25/746525_tome_sousa_20250120143532.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 76, 
                        'situacao': "Ativo",
                        'clube': clubes[20], 
                        'posicao': posicoes[0],
                        'equipa': equipas[22],
                    },
                    
                    
                    {
                        'nome': "Augusto Dabó",
                        'idade': 20,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/09/15/870915_augusto_dabo_20250120143721.png" ,
                        'nacionalidade': "Guiné-Bissau",
                        'num_camisola': 25, 
                        'situacao': "Ativo",
                        'clube': clubes[20], 
                        'posicao': posicoes[7],
                        'equipa': equipas[22],
                    },
                    
                    
                    {
                        'nome': "Gonçalo Almeida",
                        'idade': 21,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/33/31/693331_goncalo_almeida_20250120143816.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 35, 
                        'situacao': "Ativo",
                        'clube': clubes[20], 
                        'posicao': posicoes[7],
                        'equipa': equipas[22],
                    },
                    
                    
                    
                    {
                        'nome': "Tomás Silva",
                        'idade': 18,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/94/04/669404_tomas_silva_20250120143900.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 75, 
                        'situacao': "Ativo",
                        'clube': clubes[20], 
                        'posicao': posicoes[7],
                        'equipa': equipas[22],
                    },
                    
                    {
                        'nome': "Leonardo Ferreira",
                        'idade': 17,
                        'imagem': "https://www.zerozero.pt/jogador/leonardo-ferreira/877441" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 85, 
                        'situacao': "Ativo",
                        'clube': clubes[20], 
                        'posicao': posicoes[2],
                        'equipa': equipas[22],
                    },
                    
                    
                    {
                        'nome': "Miguel Reisinho",
                        'idade': 25,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/58/00/415800_miguel_reisinho_20250120144052.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 10, 
                        'situacao': "Ativo",
                        'clube': clubes[20], 
                        'posicao': posicoes[26],
                        'equipa': equipas[22],
                    },
                    
                    
                    {
                        'nome': "Manuel Namora",
                        'idade': 26,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/72/68/417268_manuel_namora_20250120144326.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 17, 
                        'situacao': "Ativo",
                        'clube': clubes[20], 
                        'posicao': posicoes[39],
                        'equipa': equipas[22],
                    },
                    
                    {
                        'nome': "Tiago Machado",
                        'idade': 20,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/84/78/468478_tiago_machado_20250120144837.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 26, 
                        'situacao': "Ativo",
                        'clube': clubes[20], 
                        'posicao': posicoes[39],
                        'equipa': equipas[22],
                    },
                    
                    {
                        'nome': "João Barros",
                        'idade': 19,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/78/11/877811_joao_barros_20250120144948.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 71, 
                        'situacao': "Ativo",
                        'clube': clubes[20], 
                        'posicao': posicoes[31],
                        'equipa': equipas[22],
                    },
                    
                    {
                        'nome': "Salvador Agra",
                        'idade': 33,
                        'imagem': "https://www.zerozero.pt/img/jogadores/new/38/40/123840_salvador_agra_20250120144314.png" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 7, 
                        'situacao': "Ativo",
                        'clube': clubes[20], 
                        'posicao': posicoes[30],
                        'equipa': equipas[22],
                    },
                    
                    
                    
                    
                    {
                        'nome': "Miguel DaSilba",
                        'idade': 20,
                        'imagem': "https://scontent.fopo4-2.fna.fbcdn.net/v/t39.30808-6/344746020_1637346010072123_4867410465697714811_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=a5f93a&_nc_ohc=DVsrwPhk258Q7kNvgH3o7Bg&_nc_oc=Adihf5FAwrkOPul27fiIIZ5sWl9QgqpaOhxTXkRHLpkMm6aDOU_hsZFgwH4esDOPLHC2kYAqUqUjwAwca2WuLhGI&_nc_zt=23&_nc_ht=scontent.fopo4-2.fna&_nc_gid=AcL1MlkOSsXsoLQ1CezQnDJ&oh=00_AYBTtVNGx6hIiHfSX0UwGS0Z43p6p4_sZMXhN85KWURkMg&oe=67A55A14" ,
                        'altura': 169,
                        'peso': 64.5,
                        'nacionalidade': "Portugal",
                        'num_camisola': 88, 
                        'valor_de_mercado': 99.0,
                        'situacao': "Ativo",
                        'clube': clubes[2], 
                        'posicao': posicoes[28], 
                        'equipa': equipas[2], 
                    },
                    {
                        'nome': "Roberto Macedo",
                        'imagem': "https://www.zerozero.pt/img/jogadores/27/1048227_roberto_macedo.jpg" ,
                        'nacionalidade': "Portugal",
                        'num_camisola': 15, 
                        'situacao': "Falecido",
                        'clube': clubes[22], 
                        'posicao': posicoes[12], 
                    },

                    
                    
                ]
                
                jogadores = [P_Jogador.objects.create(**data) for data in jogadores_data]
                self.stdout.write(self.style.SUCCESS(f'{len(jogadores)} Jogadores created'))
                
                # Inserir Jogo
                ## Estado: Em Breve / A Decorrer / Terminado / Cancelado
                ## O Vencedor, se não houver, coloca-se None
                jogos_data = [
                    {
                        'dia': datetime(2024, 8, 29).date(),
                        'hora': "14:00",
                        'estado': "Terminado" ,
                        'duracao': 90,
                        'prolongamento': True,
                        'penaltis': True,
                        'competicao': competicoes[1], # Competição Liga Portuguesa
                        'estadio': estadios[24], # Estádio  leiria
                        'clube_casa': clubes[4], # Clube Benfica
                        'clube_fora': clubes[3], # Clube Sporting
                        'equipa_casa': equipas[3], # Equipa Principal Benfica
                        'equipa_fora': equipas[5], # Equipa Principal Sporting
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
                        'password': "123",
                        'is_active': True,
                        'is_staff': True,
                        'is_superuser': True 
                    },
                    {
                        'nome': "Francisca Palma",
                        'email': "kika@email.com",
                        'password': "123",
                        'is_active': True,
                        'is_staff': False,
                        'is_superuser': False
                    },
                    {
                        'nome': "Marco Vicente",
                        'email': "vicente@email.com",
                        'password': "123",
                        'is_active': True,
                        'is_staff': True,
                        'is_superuser': True
                    },
                ]
                
                # Criar Utilizadores utilizando o manager para a criptografia (hashing) da palavra-passe
                utilizadores = []
                for data in utilizadores_data:
                    password = data.pop('password')  # Remove password from data dict
                    utilizador = Utilizador.objects.create_user(
                        email=data.pop('email'),
                        nome=data.pop('nome'),
                        palavra_passe=password,
                        **data
                    )
                    utilizadores.append(utilizador)
                
                self.stdout.write(self.style.SUCCESS(f'{len(utilizadores)} Utilizadores created'))
                
                # Inserir Clube Favorito
                clubesFav_data = [
                    {
                        'utilizador_id': utilizadores[1].utilizador_id, # Utilizador Francisca
                        'clube': clubes[3], # Clube Sporting
                        'clube': clubes[0],
                    },
                ]
                    
                clubesFav = [P_ClubeFavorito.objects.create(**data) for data in clubesFav_data]
                self.stdout.write(self.style.SUCCESS(f'{len(clubesFav)} Clubes Favoritos created'))
            
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error inserting data: {e}'))
            import traceback
            traceback.print_exc()
            
     
     
     
     
     
     
