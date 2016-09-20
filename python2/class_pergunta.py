# -*- coding: cp1252 -*-
class Pergunta:
    "classe que aloca as perguntas"
    __nome__= None
    __topico__= None
    __subtopico__= None

    def __init__(self,nome,topico,subtopico=None):
        self.__nome__=nome
        self.__topico__=topico
        self.__subtopico__=subtopico
        print "criando nova instância"
    def get_nome(self):
        return self.__nome__
    def set_nome(self,nome):
        self.__nome__=nome
    def get_topico(self):
        return self.__topico__
    def set_topico(self,topico):
        self.__topico__=topico
    def get_subtopico(self):
        return self.__subtopico__
    def set_subtopico(self,subtopico):
        self.__subtopico__=subtopico
    def __call__(self,x):
        print self.__nome__
    def __str__(self):
        return 'Instancia da classe %s' %self.__class__

class Resposta:
    "Classe que aloca todas respostas das perguntas"
    __tipo__=None
    __nome__=None

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
        return 'Instancia da classe %s' %self.__class__
    def __call__(self,x):
        print self.__nome__
