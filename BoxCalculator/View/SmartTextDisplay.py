'''
Created on 10 sty 2019

@author: Tomasz Jakobiec
'''

from tkinter import *

class SmartTextDisplay(Text):
    
    def __init__(self,master=None, cnf={}, **kw):
        Text.__init__(self, master, cnf={}, **kw)
        
    def print(self, string):
        self.insert(END, string)
        
    def println(self, string):
        self.insert(END, string)
        self.insert(END, "\n")

