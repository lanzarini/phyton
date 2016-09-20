# -*- coding: cp1252 -*-
"""módulo com acessos ao postgre"""
import psycopg2

def Acesso(sql):
    """
    Acessa o bd a partir de uma sql recebida e retorna o resultado
    """
    con = psycopg2.connect(host='localhost', database='tcc',user='postgres', password='123')
    cur = con.cursor()
    con.set_client_encoding('LATIN9')
    cur.execute(sql)
    recset = cur.fetchall()
    con.close()
    return recset
def BuscaPerguntas(argumento):
    """Função para retornar as perguntas contidas em um formulario passado como argumento"""
    sql="""select A.pergunta,A.topico,A.ID_Perg,B.ordem,A.subtopico from 
            Tab_Perguntas as A   
            LEFT JOIN Tab_Perg_Form as B
                  on A.ID_Perg = B.CodPergunta
                  where B.CodFormulario='%s'"""%argumento
    result=Acesso(sql)
    return (result)

def BuscaOpcoes(argumento):
    """Função para retornar o ID das opções de resposta referentes a pergunta passada como argumento"""
        #con = psycopg2.connect(host='localhost', database='tcc',user='postgres', password='123')
        #cur = con.cursor()
        #con.set_client_encoding('LATIN9')
        #sql="select ID_Resp from Tab_Respostas where CodPergunta=(select ID_Perg from Tab_Perguntas where Pergunta ='%s')" %argumento
        #cur.execute(sql)
        #recset = cur.fetchall()
        #con.close()
        #return recset
    sql="""select Resposta,Tipo from Tab_Respostas where CodPergunta=
(select ID_Perg from Tab_Perguntas where Pergunta ='%s')""" %argumento
    result=Acesso(sql)      
    return (result)

def RetornaTodosNomes(argumento):
    """
    Função que busca os dados de uma resposta a partir do seu ID
    """
    sql="select ID_Resp,Resposta from Tab_Respostas where CodPergunta='%s'" %argumento
    result=Acesso(sql)
    return (result)

def RetornaTodos():
    """
    Função que busca os dados de uma resposta a partir do seu ID
    """
    sql="select * from Tab_Perg_Form"
    result=Acesso(sql)
    print (result)
    return result
