# -*- coding: cp1252 -*-
from Tkinter import *
from controle import *
from multlist import  MultiListbox
master = Tk()

frame=Frame(master,pady=10,padx=20,bg='blue')
frame.pack(side=TOP,fill=BOTH,expand=1)
framebot=Frame(master,pady=10,padx=20,bg='purple')
framebot.pack(side=BOTTOM,fill=BOTH,expand=0)

frame1=Frame(frame,pady=10,padx=20,bg='green')
frame1.pack(side=LEFT,fill=BOTH,expand=1)
frame2=Frame(frame,pady=10,padx=20,bg='red')
frame2.pack(side=RIGHT,fill=BOTH,expand=1)

frameb=Frame(frame1,pady=10,padx=20,bg='yellow')
frameb.pack(side=TOP,fill=X,expand=0)
frameb2=Frame(frame2,pady=10,padx=20,bg='yellow')
frameb2.pack(side=TOP,fill=X,expand=0)

#lab=Label(framebot,text='aqs', borderwidth=1, relief=FLAT,justify=LEFT,anchor=W)
#lab.pack(fill=X)

v = StringVar()
Label(framebot, textvariable=v,borderwidth=1, relief=FLAT,justify=LEFT,anchor=W).pack(fill=X)

v.set("New Text!")


# scrollbar1Y = Scrollbar(frame1, orient=VERTICAL,takefocus=1)
# scrollbar2Y = Scrollbar(frame2, orient=VERTICAL)
# scrollbar1X = Scrollbar(frame1, orient=HORIZONTAL)
# scrollbar2X = Scrollbar(frame2, orient=HORIZONTAL)

#listbox3 = Listbox(frame1,selectmode=EXTENDED,exportselection=0,yscrollcommand=scrollbar1Y.set,xscrollcommand=scrollbar1X.set,relief=SUNKEN)
#listbox = Listbox(frame1,selectmode=EXTENDED,exportselection=0,yscrollcommand=scrollbar1Y.set,xscrollcommand=scrollbar1X.set,relief=FLAT)
#listbox2 = Listbox(frame2,selectmode=EXTENDED,exportselection=0,yscrollcommand=scrollbar2Y.set,xscrollcommand=scrollbar2X.set,relief=SUNKEN)

#scrollbar1X.config(command=listbox.xview)
#scrollbar1X.pack(side=BOTTOM, fill=X)
#scrollbar2X.config(command=listbox.xview)
#scrollbar2X.pack(side=BOTTOM, fill=X)

#listbox.pack(side=LEFT,fill=BOTH,expand=1)
#listbox2.pack(side=LEFT,fill=BOTH,expand=1)

#scrollbar1Y.config(command=listbox.yview)
#scrollbar1Y.pack(side=LEFT, fill=Y)

#scrollbar2Y.config(command=listbox2.yview)
#scrollbar2Y.pack(side=LEFT, fill=Y)






# listbox.insert(END, "a list entry")
# items=RetornaTodosNomes()
# print items
# #for item in ["one", "two", "three", "four"]:
# #    listbox.insert(END, item)
# for a in range(0,10):
# 	for valor in items:
# 		listbox.insert(END, valor[0])
# #items = map(int, listbox.curselection())


def export():

	for item in mlb.curselection():
		mlb2.insert(END, mlb.get(item))
		#lab['text']="%s" %mlb.get(mlb.curselection())[1]
		
		mlb.selection_clear(item)
		#print mlb.get(mlb.curselection())
		#listbox.activate(item)
		#listbox.itemconfig(item,bg='red')
		#listbox.selection_clear(item)
		#listbox2.insert(END,listbox.get(item))
		#listbox2.insert(END,listbox.get(ACTIVE))
def analisar():
	#result=RetornaTodosNomes(mlb.get(mlb.curselection()))
	if mlb.curselection():
		v.set('%s \n%s' %(mlb.get(mlb.curselection())[0],mlb.get(mlb.curselection())[1]))


def retornar():
	for item in listbox.curselection():
		if listbox.itemcget(item,'bg')=='red':
			listbox.itemconfig(item,bg='SystemButtonFace')
			listbox2.itemconfig

def delete():
	print listbox2.see(2)#delete(0)

bt1=Button(frameb,width=7,text="exportar",command=export)
bt1.pack(side=LEFT,expand=1)
bt2=Button(frameb,width=7,text="analisar",command=analisar)
bt2.pack(side=LEFT,expand=1)
bt3=Button(frameb,width=7,text="exportar",command=export)
bt3.pack(side=LEFT,expand=1)

bt4=Button(frameb2,width=7,text="exportar",command=export)
bt4.pack(side=LEFT,expand=1)
bt5=Button(frameb2,width=7,text="exportar",command=export)
bt5.pack(side=LEFT,expand=1)
bt6=Button(frameb2,width=7,text="exportar",command=export)
bt6.pack(side=LEFT,expand=1)





item=RetornaTodos()
mlb = MultiListbox(frame1, ((u'Numero', 10), (u'joão peidão', 50)))
mlb2 = MultiListbox(frame2, ((u'Numero', 10), (u'Pergunta', 50)))
for io in range(0,2): #apenas para inserir o drobro
	for i in range(0,len(item)):
		mlb.insert(END, (item[i][0],item[i][1]))
		mlb2.insert(END, (item[i][0],item[i][1]))
mlb.pack(side=LEFT,fill=BOTH,expand=1)
mlb2.pack(side=RIGHT,fill=BOTH,expand=1)

#print mlb.curselection()

#ScrollingArea(mlb).add_scrolling(mlb, xscrollbar=xScrollbar, yscrollbar=yScrollbar)
#listbox2.insert(END, "a list entry2")
mainloop()