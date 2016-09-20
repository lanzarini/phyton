from Tkinter import *
def callback(*args):
    print (frame.winfo_reqwidth(),master.winfo_screenheight())
master = Tk()
#master.state('zoomed')
#master.geometry("%dx%d" % (master.winfo_screenwidth(),master.winfo_screenheight() ))
MODES = [
        ("Monochrome", "1"),
        ("Grayscale", "L"),
        ("True color", "RGB"),
        ("Color separation", "CMYK"),
    ]
master.config(pady=10,padx=10)
v = StringVar()
v.set("L") # initialize
v.trace("w", callback)

for text, mode in MODES:
    b = Radiobutton(master, text=text,
                        variable=v, value=mode)
    b.pack(anchor=W)


vi = IntVar()
frame2=LabelFrame(master,text="pai",padx=10,pady=10)
frame2.pack(fill=X)
frame=LabelFrame(frame2,text="Especime",padx=10,pady=10)
frame.pack(fill=X)
#if frame.winfo_req

xls=Radiobutton(frame, text="Oneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
 variable=vi, value=1,indicatoron=0).pack(fill=BOTH,side=LEFT,expand=1)
#print ("asd=", xls.winfo_reqwidth())

xx=Radiobutton(frame, text="""Twoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo00000000000000000000000o""", 
    wraplength=(master.winfo_screenwidth()-200),variable=vi, value=2,indicatoron=0).pack(fill=BOTH,side=LEFT,expand=1)
#print ("asd=", xx.winfo_reqwidth())
slaves=frame.slaves()
print slaves

print (frame.cget("width"))
print (frame.cget("height"))
print (master.winfo_width(), master.winfo_height())
mainloop()

