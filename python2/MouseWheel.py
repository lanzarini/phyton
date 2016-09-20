import Tkinter as tk
import ttk

import platform

class ScrollingArea(object):
    OS = platform.system()
    
    def __init__(self, root, factor = 2):
        
        self.activeArea = None
        
        if type(factor) == int:
            self.factor = factor
        else:
            raise Exception("Factor must be an integer.")

        if self.OS == "Linux" :
            root.bind_all('<4>', self.onMouseWheel,  add='+')
            root.bind_all('<5>', self.onMouseWheel,  add='+')
        else:
            # Windows and MacOS
            root.bind_all("<MouseWheel>", self.onMouseWheel,  add='+')

    def onMouseWheel(self,event):
        if self.activeArea:
            self.activeArea.onMouseWheel(event)

    def mouseWheel_bind(self, widget):
        self.activeArea = widget

    def mouseWheel_unbind(self):
        self.activeArea = None

    def build_function_onMouseWheel(self, widget, orient, factor = 1):
        view_command = getattr(widget, orient+'view')
        
        if self.OS == 'Linux':
            def onMouseWheel(event):
                if event.num == 4:
                    view_command("scroll",(-1)*factor,"units" )
                elif event.num == 5:
                    view_command("scroll",factor,"units" ) 
                
        elif self.OS == 'Windows':
            def onMouseWheel(event):        
                view_command("scroll",(-1)*int((event.delta/120)*factor),"units" ) 
        
        elif self.OS == 'Darwin':
            def onMouseWheel(event):        
                view_command("scroll",event.delta,"units" )             
        
        return onMouseWheel
        

    def add_scrolling(self, scrollingArea, xscrollbar=None, yscrollbar=None):
        # if xscrollbar:
        #     scrollingArea.configure(xscrollcommand=xscrollbar.set)
        #     xscrollbar['command']=scrollingArea.yview

        # if yscrollbar:
        #     scrollingArea.configure(yscrollcommand=yscrollbar.set)
        #     yscrollbar['command']=scrollingArea.xview
        
        scrollingArea.bind('<Enter>',lambda event: self.mouseWheel_bind(scrollingArea))
        scrollingArea.bind('<Leave>', lambda event: self.mouseWheel_unbind())

        if xscrollbar and not hasattr(xscrollbar, 'onMouseWheel'):
            xscrollbar.onMouseWheel = self.build_function_onMouseWheel(scrollingArea,'x', self.factor)

        if yscrollbar and not hasattr(yscrollbar, 'onMouseWheel'):
            yscrollbar.onMouseWheel = self.build_function_onMouseWheel(scrollingArea,'y', self.factor)

        main_scrollbar = yscrollbar or xscrollbar
        
        if main_scrollbar:
            scrollingArea.onMouseWheel = main_scrollbar.onMouseWheel

        for scrollbar in (xscrollbar, yscrollbar):
            if scrollbar:
                scrollbar.bind('<Enter>', lambda event, scrollbar=scrollbar: self.mouseWheel_bind(scrollbar) )
                scrollbar.bind('<Leave>', lambda event: self.mouseWheel_unbind())
