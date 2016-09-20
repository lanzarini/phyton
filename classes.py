# -*- coding: cp1252 -*-
class Pergunta:
    "classe que aloca as perguntas"
    __nome= None
    __topico= None
    __subtopico= None
    def __init__(self,nome,topico,Id=None,ordem=None,subtopico=None):
        self.__nome=nome
        self.__topico=topico
        self.__subtopico=subtopico
        self.__ID=Id
        self.__ordem=ordem
        print ("criando nova instância "+self.__nome)

    def busca_respostas(self):
        from controle import BuscaOpcoes
        IDs=BuscaOpcoes(self.__nome)
        print (IDs)
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

    def get_id(self):
        return self.__ID
    def set_id(self,id):
        self.__ID=id

    def get_ordem(self):
        return self.__ordem
    def set_ordem(self,ordem):
        self.__ordem=ordem

    def __call__(self,x):
        print (self.__nome)
    def __str__(self):
        return 'Instancia de %s' %self.__class__

class Resposta:
    "Classe que aloca todas respostas das perguntas"
    def __init__(self,nome,tipo):
        self.__tipo__=tipo
        self.__nome__=nome
        print ("criando nova instância")
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
        print (self.__nome__)
class Usuario:
    "Classe que aloca os dados dos usuarios"
    __nome=None

    def __init__(self,nome):
        self.__nome__=nome
        print ("criando nova instancia")
    def get_nome(self):
        return self.__nome__
    def set_nome(self,nome):
        self.__nome__=nome
    def __str__(self):
        return "Instancia de %s" %self.__class__
    def __call__(self,x):
        print (self.__nome__)

class Formulario:
    "Classe que aloca os dados dos formularios"

    def __init__(self,nome,Id=None):
        self.__nome=nome
        self.__id=Id
        print ("criando nova instancia")
    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        self.__nome=nome

    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id=id

    def __str__(self):
        return "Instancia de %s" %self.__class__
    def __call__(self,x):
        print (self.__nome__)   

    def busca_perguntas(self):
        from controle import BuscaPerguntas
        IDs=BuscaPerguntas(self.__id)
        print (IDs)
        #for j in IDs:
         #   pass
            #if j[4] is not None :
            #print (j)
            #else:
             #   print (j[0]) 
        self.perguntas=[Pergunta(j[0],j[1],j[2],j[3],j[4]) for j in IDs]
        for l in self.perguntas:
            l.busca_respostas()

