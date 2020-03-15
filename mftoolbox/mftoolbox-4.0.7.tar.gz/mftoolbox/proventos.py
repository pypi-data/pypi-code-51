class proventos:

    #
    # Define a classe Proventos
    # Autor: Celso Oliveira (c.oliveira@live.com)
    # Controle de versão:
    #
    #   1.0, 16/Ago/18, criação.
    #
    # Documentação de apoio:
    #
    #   http://catalogo.governoeletronico.gov.br/arquivos/Documentos/WS_SGS_BCB.pdf - descrição do uso do Webservice
    #   http://python-zeep.readthedocs.io/en/master/ - zeep, biblioteca para trabalhar com webservices
    #   http://blog.tiagocrizanto.com/configuracoes-do-webservice-do-banco-central-cotacoes-diversas/

    def __init__(self, arg_idioma, arg_cd_acao, arg_data, arg_valor, arg_tipo, arg_referencia):
        self.idioma = arg_idioma
        self.cd_acao = arg_cd_acao
        self.arg_data = arg_data
        self.arg_valor = arg_valor
        self.arg_tipo = arg_tipo
        self.tipo = self.arg_tipo.upper()
        self.referencia = arg_referencia
        self.data = datetime.datetime(int(self.arg_data[6:]),int(self.arg_data[3:5]),int(self.arg_data[:2]))
        self.ano = self.data.year
        self.mes = self.data.month
        self.dia = self.data.day
        if self.idioma == "ENG": self.valor=float(self.arg_valor)
        elif self.idioma == "PTB": self.valor=float(self.arg_valor.replace('.','').replace(',','.'))
        #Normalizando o tipo de dividendo
        #tipos existentes nas bases da Fundamentus:
        #"JUROS"
        #"JRS CAP PROPRIO"
        #"JRS CAP PRÓPRIO"
        #"DIVIDENDO"
        #"REST CAP DIN"
        #"JUROS MENSAL"
        #"RESTITUIÃ§Ã£O DE CAPITAL"
        #"DIVIDENDO MENSAL"
        #Fundamentus não apresenta dados de bonificações
        if self.tipo[:1] == "J": self.tipo_normalizado = "JCP"
        if self.tipo[:1] == "D": self.tipo_normalizado = "DIV"
        if self.tipo[:1] == "R": self.tipo_normalizado = "RST"
