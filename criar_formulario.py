# -*- coding: utf-8 -*-

from tkinter import *
from classes import Formulario
class ScrolledWindow(Frame):


    def __init__(self, parent, *args, **kwargs):

        self.parent = parent

        # creating a scrollbars
        self.xscrlbr = Scrollbar(self.parent, orient = 'horizontal')
        self.xscrlbr.pack(side=BOTTOM,fill=X)                              
        self.yscrlbr = Scrollbar(self.parent)
        self.yscrlbr.pack(side=RIGHT,fill=Y)             			       
        # creating a canvas
        self.canv = Canvas(self.parent)
        self.canv.config(relief = 'flat',width = 0,heigh =0, bd = 0, bg='pink')
        # placing a canvas into frame
        self.canv.pack(side=TOP,expand=0)								
        # accociating scrollbar comands to canvas scroling
        self.xscrlbr.config(command = self.canv.xview)
        self.yscrlbr.config(command = self.canv.yview)

        # creating a frame to inserto to canvas
        self.scrollwindow = Frame(self.parent,pady=0,padx=50,bg='blue')

        self.canv.create_window(0,0, window = self.scrollwindow, anchor = 'nw')
        #self.canv.create_window(0,0, window = self.scrollwindow, anchor = 'nw')
        self.canv.config(xscrollcommand = self.xscrlbr.set, yscrollcommand = self.yscrlbr.set)
        self.yscrlbr.lift(self.scrollwindow)        
        self.xscrlbr.lift(self.scrollwindow)
        self.scrollwindow.bind('<Configure>', self._configure_window)  
        self.canv.bind('<Enter>', self._bound_to_mousewheel)
        self.canv.bind('<Leave>', self._unbound_to_mousewheel)
        self.scrollwindow.bind('<Enter>', self._bound_to_mousewheel)
        self.scrollwindow.bind('<Leave>', self._unbound_to_mousewheel)
        
        return

    def aumentar_frame(self,x):
        frame=Frame(self.scrollwindow,pady=10,padx=208,bg='cyan')
        frame.pack(fill=BOTH,expand=1)
        label=Label(frame,text=x.get_nome())
        label.pack()
        en=Entry(frame,width=20,justify=CENTER)
        en.focus_force()
        en.pack()
        bt1=Button(frame,width=7,text="exportar",command=lambda: self.exportar(x,en,label))
        bt1.pack()
        bt2=Button(frame,width=7,text="importar",command=self.sair)
        bt2.pack()
        self.parent.geometry("800x600" )#%(self.canv.winfo_width(),self.canv.winfo_width()) )

    def sair(self):
        self.parent.destroy()

    def exportar(self,x,en,l):
        print ('aqui '+x.get_nome())
        x.set_nome(en.get())
        print ('ali '+x.get_nome())
        #l.config(text=x.get_nome())

    def _bound_to_mousewheel(self, event):
        self.canv.bind_all("<MouseWheel>", self._on_mousewheel)   

    def _unbound_to_mousewheel(self, event):
        self.canv.unbind_all("<MouseWheel>") 

    def _on_mousewheel(self, event):
        self.canv.yview_scroll(-1*(1 if event.delta>0 else -1), "units")  

    def _configure_window(self, event):
        # update the scrollbars to match the size of the inner frame
         size = (self.scrollwindow.winfo_reqwidth(), self.scrollwindow.winfo_reqheight())
         self.canv.config(scrollregion='0 0 %s %s' % size)
         if self.scrollwindow.winfo_reqwidth() != self.canv.winfo_width():
             # update the canvas's width to fit the inner frame
             self.canv.config(width = self.scrollwindow.winfo_reqwidth())
             #self.scrollwindow.config(width = self.canv.winfo_reqwidth())
         if self.scrollwindow.winfo_reqheight() != self.canv.winfo_height():
             # update the canvas's width to fit the inner frame
             #self.scrollwindow.config(width = self.canv.winfo_reqheight())
             self.canv.config(height = self.scrollwindow.winfo_reqheight())
        #self.canvas.configure(scrollregion=self.canvas.bbox("all"))

root=Tk()
pg=ScrolledWindow(root)
#root.geometry("800x600")
#print (pg.bt1['text'])

# fram1=Frame(pg.scrollwindow,pady=50,padx=109,bg='red')
# fram1.pack(fill=BOTH,expand=1)
# bt1=Button(fram1,width=7,text="exportar")
# bt1.pack()
# bt2=Button(fram1,width=7,text="exportar")
# bt2.pack()
red=Formulario("Esd",3)
red.busca_perguntas()
for l in red.perguntas:
    pg.aumentar_frame(l)
#print (red.get_nome())
# fram2=Frame(pg.scrollwindow,pady=10,padx=208,bg='yellow')
# fram2.pack(fill=BOTH,expand=1)
# bt3=Button(fram2,width=7,text="exportar")
# bt3.pack()
# bt4=Button(fram2,width=7,text="exportar")
# bt4.pack()

root.mainloop()
#print ("deu certo "+red.get_nome())