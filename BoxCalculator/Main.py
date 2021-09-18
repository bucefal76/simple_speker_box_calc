'''
Created on 24 Aug 2021

@author: Tomasz Jakobiec
'''

from tkinter import *

from View import MainWindow

if __name__ == '__main__':

    print("Starting the BoxCalculator...")

    master = Tk()
    master.title("BoxCalc 0.02")
    master.geometry("800x600")
    master.resizable(False, False)

    main_window = MainWindow.MainWindow(master)
    master.mainloop()

    pass
