# -*- coding: cp1252 -*-
class Pergunta:
    "classe que aloca as perguntas"
    __nome= None
    __topico= None
    __subtopico= None
    def __init__(self,nome,topico,subtopico='éó'):
        self.__nome=nome
        self.__topico=topico
        self.__subtopico=subtopico
        print "criando nova instância"
    def busca_respostas(self):
        from controle import BuscaOpcoes
        IDs=BuscaOpcoes(self.__nome)
        print IDs
        self.opcoes=[Resposta(j[0],j[1])for j in IDs]
    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        self.__nome=nome
    def get_topico(self):
        return self.__topico
    def set_topico(self,topico):
        self.__topico=topico
    def get_subtopico(self):
        return self.__subtopico
    def set_subtopico(self,subtopico):
        self.__subtopico=subtopico
    def __call__(self,x):
        print self.__nome
    def __str__(self):
        return 'Instancia de %s' %self.__class__
    nome=property(get_nome,set_nome)
    subtopico=property(get_subtopico,set_subtopico)
    topico=property(get_topico,set_topico)
class Resposta:
    "Classe que aloca todas respostas das perguntas"
    __tipo=None
    __nome=None
    def __init__(self,nome,tipo):
        self.__tipo__=tipo
        self.__nome__=nome
        print "criando nova instância"
    def get_nome(self):
        return self.__nome__
    def get_tipo(self):
        return self.__tipo__
    def set_nome(self,nome):
        self.__nome__=nome
    def set_tipo(self,tipo):
        self.__tipo__=tipo
    def __str__(self):
        return 'Instancia de %s' %self.__class__
    def __call__(self,x):
        print self.__nome__
class Usuario:
    "Classe que aloca os dados dos usuarios"
    __nome=None

    def __init__(self,nome):
        self.__nome__=nome
        print "criando nova instancia"
    def get_nome(self):
        return self.__nome__
    def set_nome(self,nome):
        self.__nome__=nome
    def __str__(self):
        return "Instancia de %s" %self.__class__
    def __call__(self,x):
        print self.__nome__
class Formulario:
    "Classe que aloca os dados dos formularios"
    __nome=None

    def __init__(self,nome):
        self.__nome__=nome
        print "criando nova instancia"
    def get_nome(self):
        return self.__nome__
    def set_nome(self,nome):
        self.__nome__=nome
    def __str__(self):
        return "Instancia de %s" %self.__class__
    def __call__(self,x):
        print self.__nome__

