from Tkinter import *
class ScrolledWindow(Frame):
    """
    1. Master widget gets scrollbars and a canvas. Scrollbars are connected 
    to canvas scrollregion.

    2. self.scrollwindow is created and inserted into canvas

    Usage Guideline:
    Assign any widgets as children of <ScrolledWindow instance>.scrollwindow
    to get them inserted into canvas

    __init__(self, parent, canv_w = 400, canv_h = 400, *args, **kwargs)
    docstring:
    Parent = master of scrolled window
    canv_w - width of canvas
    canv_h - height of canvas

    """


    def __init__(self, parent,canv_w = 0, canv_h = 0, *args, **kwargs):
        """Parent = master of scrolled window
        canv_w - width of canvas
        canv_h - height of canvas

       """
        #super().__init__(parent, *args, **kwargs)

        self.parent = parent

        # creating a scrollbars
        self.xscrlbr = Scrollbar(self.parent, orient = 'horizontal')
        self.xscrlbr.pack(side=BOTTOM,fill=X)                        #grid(column = 0, row = 1, sticky = 'ew', columnspan = 2)         
        self.yscrlbr = Scrollbar(self.parent)
        self.yscrlbr.pack(side=RIGHT,fill=Y)             			 #grid(column = 1, row = 0, sticky = 'ns')         
        # creating a canvas
        self.canv = Canvas(self.parent)
        self.canv.config(relief = 'flat',
                         width = canv_w,
                         heigh = canv_h, bd = 0, bg='pink')
        # placing a canvas into frame
        self.canv.pack(side=TOP,expand=0)								#grid(column = 0, row = 0, sticky = 'nsew')
        # accociating scrollbar comands to canvas scroling
        self.xscrlbr.config(command = self.canv.xview)
        self.yscrlbr.config(command = self.canv.yview)

        # creating a frame to inserto to canvas
        self.scrollwindow = Frame(self.parent,pady=0,padx=10,bg='blue')

        #self.scrollwindow.pack(fill=BOTH,expand=1)
        
        fram1=Frame(self.scrollwindow,pady=1000,padx=409,bg='red')
        fram1.pack(fill=BOTH,expand=1)
        bt1=Button(fram1,width=7,text="exportar")
        bt1.pack()
        bt2=Button(fram1,width=7,text="exportar")
        bt2.pack()

        fram2=Frame(self.scrollwindow,pady=10,padx=208,bg='yellow')
        fram2.pack(fill=BOTH,expand=1)
        bt3=Button(fram2,width=7,text="exportar")
        bt3.pack()
        bt4=Button(fram2,width=7,text="exportar")
        bt4.pack()

        self.canv.create_window(0,0, window = self.scrollwindow, anchor = 'nw')
        self.canv.create_window(0,0, window = self.scrollwindow, anchor = 'nw')
        self.canv.config(xscrollcommand = self.xscrlbr.set,
                         yscrollcommand = self.yscrlbr.set)

        self.yscrlbr.lift(self.scrollwindow)        
        self.xscrlbr.lift(self.scrollwindow)
        self.scrollwindow.bind('<Configure>', self._configure_window)  
        self.scrollwindow.bind('<Enter>', self._bound_to_mousewheel)
        self.scrollwindow.bind('<Leave>', self._unbound_to_mousewheel)

        return

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
ScrolledWindow(root)
root.geometry("800x600")
root.mainloop()
