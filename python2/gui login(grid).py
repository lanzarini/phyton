# -*- coding: utf-8 -*-
from Tkinter import *

class login:
	def __init__(self,x):

		


		#Labels
		x.title("Realizar login")
		Label(x,text="Nome de usuario").grid(row=2,column=1,pady=5)
		Label(x,text="Senha do usuario").grid(row=3,column=1,pady=5)
		Label(x,text="Acesso ao sistema").grid(row=1,column=1,columnspan=2,pady=10)
		self.status=Label(x,text="Status...")
		self.status.grid(row=4,column=1,columnspan=2)
		
		#Entradas
		self.nome_usuario=Entry(x,width=10)
		self.nome_usuario.focus_force()
		self.nome_usuario.grid(row=2,column=2)
		self.senha_usuario=Entry(x,width=10,show='*',fg='darkgray')
		self.senha_usuario.grid(row=3,column=2)
		
		#Botões
		self.entrar=Button(x,width=7,text='Entrar',command=self.validacao)
		self.entrar.grid(row=5,column=1,columnspan=1)
		self.sair=Button(x,width=7,text='Sair',command=x.destroy)
		self.sair.grid(row=5,column=2,columnspan=1)
		#self.entrar.bind("<Return>",self.keypress02)
		#self.entrar.bind("<Any-Button>",self.button02)
		self.entrar.bind("<FocusIn>",self.fin01)
		self.entrar.bind("<FocusOut>",self.fout01)
		self.sair.bind("<FocusIn>",self.fin02)
		self.sair.bind("<FocusOut>",self.fout02)

		#self.entrar['relief']=RIDGE

	def fin01(self,event): self.entrar['relief']=RIDGE
	def fout01(self,event): self.entrar['relief']=RAISED
	def fin02(self,event): self.sair['relief']=RIDGE
	def fout02(self,event): self.sair['relief']=RAISED
	def validacao(self):
		if self.nome_usuario.get()=='icaro' and self.senha_usuario.get()=='123':
			self.status['text']="Acesso Aprovado"
		else:
			self.status['text']="Acesso Negado"
root=Tk()
login(root)
#root.geometry("600x400")
root.mainloop()