# -*- coding: cp1252 -*-
from Tkinter import *
class sistema:
	def __init__(self,master):
		self.frame=Frame(master)
		self.frame.pack()
		self.menu=Menu(master)
		self.menu_cadastro=Menu(self.menu)
		self.menu_cadastro.add_command(label="Buscar formularios")
		self.menu_cadastro.add_command(label="Buscar perguntas")
		self.menu_cadastro.add_command(label="Buscar opcões")
		self.menu.add_cascade(label="Buscas",menu=self.menu_cadastro)
		self.menu_cadastro1=Menu(self.menu)
		self.menu_cadastro1.add_command(label="Buscar formularios")
		self.menu_cadastro1.add_command(label="Buscar perguntas")
		self.menu_cadastro1.add_command(label="Buscar opcões")
		self.menu.add_cascade(label="Buscas",menu=self.menu_cadastro1)
		master.config(menu=self.menu)

root=Tk()
root.geometry("600x400")	#tamanho inicial da janela
root.maxsize(780,560)		 #tamanho maximo da janela
root.title("Buscar tabelas")	#nome da janela
a1=sistema(root)
print dir(a1)
a1.frame.mainloop()


