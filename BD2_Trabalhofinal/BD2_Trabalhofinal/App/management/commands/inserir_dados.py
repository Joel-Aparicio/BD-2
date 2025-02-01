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
                        "nome": "Estádio do Bessa Séc. XXI",
                        "imagem": "https://www.zerozero.pt/img/estadios/388/690388_ori_estadio_do_bessa_sec_xxi.jpg",
                        "pais": "Portugal",
                        "cidade": "Porto",
                        "inauguracao":1910,
                        "estado": "Ativo",
                        "lotacao": 28263
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
                        'estadio': estadios[24]
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