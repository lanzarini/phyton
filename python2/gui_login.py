# -*- coding: utf-8 -*-
from Tkinter import *
#tkSimpleDialog.Dialog
import tkSimpleDialog
class login(tkSimpleDialog.Dialog):
	def __init__(self,x):
		#frames

		self.frame2=Frame(x,pady=0,padx=20,bg='green')
		self.frame2.pack(fill=X,expand=1)
		self.frame4=Frame(self.frame2,pady=10,padx=20,bg='red')
		self.frame4.pack(side=BOTTOM)
		self.frame3=Frame(self.frame2,bg='yellow',relief=SUNKEN,pady=10,padx=20)
		self.frame3.pack(side=BOTTOM)
		self.frame23=Frame(self.frame2,pady=10,padx=20,bg='pink')
		self.frame23.pack(side=BOTTOM)
		self.frame21=Frame(self.frame23,bg='blue',pady=10,padx=20)
		self.frame21.pack(side=LEFT)
		self.frame22=Frame(self.frame23,bg='darkgray',pady=10,padx=20)
		self.frame22.pack(side=RIGHT)		


		#Labels
		x.title("Realizar login")
		Label(self.frame21,text="Nome de usuario:").pack(side=TOP)#grid(row=2,column=1,pady=5)
		Label(self.frame21,text="Senha do usuario:").pack(side=TOP)#grid(row=3,column=1,pady=5)
		Label(self.frame2,text="Acesso ao sistema").pack(side=TOP,fill=X)#grid(row=1,column=1,columnspan=2,pady=10)
		self.status=Label(self.frame4,text="Status...",bg="red")
		self.status.pack()
		#self.status.grid(row=4,column=1,columnspan=2)
		
		#Entradas
		self.nome_usuario=Entry(self.frame22,width=20,justify=CENTER)
		self.nome_usuario.focus_force()
		self.nome_usuario.pack(side=TOP)#grid(row=2,column=2)
		self.senha_usuario=Entry(self.frame22,width=20,show='*',fg='darkgray',justify=CENTER)
		self.senha_usuario.pack(side=TOP)#grid(row=3,column=2)
		
		#Botões
		self.entrar=Button(self.frame3,width=7,text='Entrar',command=self.validacao)
		self.entrar.pack(side=LEFT)#grid(row=5,column=1,columnspan=1)
		self.sair=Button(self.frame3,width=7,text='Sair',command=x.destroy)
		self.sair.pack(side=LEFT)#grid(row=5,column=2,columnspan=1)
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
			self.nome_usuario.delete(0,END)
			self.nome_usuario.insert(0,'icaro')
			#self.nome_usuario.insert(self.nome_usuario.icursor(2),'icaro')			
			self.senha_usuario.delete(0,END)
			self.status['text']="Acesso Negado"

root=Tk()
login(root)
root.geometry("400x200")
root.mainloop()