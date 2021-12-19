'''
Created on 25 Aug 2021

@author: Tomasz Jakobiec
@email: tjakobiec@gmail.com
'''

from tkinter import *
from View import SmartTextDisplay
from View import SpeakerWindow
from Model import SpeakerConfiguration
from Model import SBB4Calc
from Model import QB3Calc
from Model import ClosedBoxCalc


class MainWindow(Frame):

    def __init__(self, master):

        self.__speaker_configuration = SpeakerConfiguration.SpeakerConfiguration()

        super(MainWindow, self).__init__(master)

        self.bind("<Configure>", self.on_resize)

        self.pack()
        self.create_widgets()
        self.create_main_menu()

    def create_widgets(self):

        self.__scrollbar = Scrollbar(self)
        self.__scrollbar.pack(side=RIGHT, fill=Y)

        self.__text_display = SmartTextDisplay.SmartTextDisplay(self,
                                                                wrap=WORD,
                                                                yscrollcommand=self.__scrollbar.set)

        self.__text_display.pack(side=BOTTOM, fill=X)

        self.__scrollbar.config(command=self.__text_display.yview)

        # self.__text_display.println("-----------------------------------------------------------")
        self.__text_display.println(
            "This is a very basic loudspeakers box calculator.")
        self.__text_display.println(
            "It calculates box net volume for 1 or 2 speakers in bass reflex SBB4, QB3 and sealed boxes.")
        self.__text_display.println(
            "The 2 speakers configuration is: parallel with common cavity.")
        self.__text_display.println(
            "Filters configuration for the 2 speakers can be parallel or cascade.")
        self.__text_display.println(
            "Vented Box calculations takes under the consideration impact of the woofer filter Rs on the final Qts.")
        self.__text_display.println(
            "Calculations are based at document publish by Jaroslaw Sobolski under the link:")
        self.__text_display.println(
            "https://diyaudio.pl/articles/artyku-y/638981-obudowa-bass-reflex")
        self.__text_display.println(
            "And doument publish by Troels Gravesen, under the link:")
        self.__text_display.println(
            "http://www.troelsgravesen.dk/vent_tuning.htm")
        self.__text_display.println(
            "Progam code copyrights belongs to T.Jakobiec 2021")
        self.__text_display.println(
            "Free to use in profit and non profit purpose.")
        self.__text_display.println(
            "Author does not guarantee that calculation results are correct, use program at your own risk!")
        # self.__text_display.println("-----------------------------------------------------------")
        self.__text_display.println("")
        self.__text_display.println("Short instrukction manual:")
        self.__text_display.println(
            "1. Go to Program -> Speaker Parameters to set up speaker and filter configuration.")
        self.__text_display.println(
            "2. Go to Calculations -> SBB4, QB3 or Closed to calculate box volume and vent parameters.")
        self.__text_display.println("")

    def create_main_menu(self):

        self.__main_menu = Menu(self)

        self.__program_menu = Menu(self.__main_menu, tearoff=0)

        self.__program_menu.add_command(
            label="Sepaker parameters", command=self.on_display_speaker_parameters)
        self.__program_menu.add_separator()
        self.__program_menu.add_command(
            label="Exit", command=self.on_menu_exit)

        self.__main_menu.add_cascade(label="Program", menu=self.__program_menu)

        self.__calculations_menu = Menu(self.__main_menu,  tearoff=0)
        self.__calculations_menu.add_command(
            label="Vented box SBB4/BB4", command=self.on_vented_sbb4_calc)
        self.__calculations_menu.add_command(
            label="Vented box QB3", command=self.on_vented_qb3_calc)
        self.__calculations_menu.add_separator()
        self.__calculations_menu.add_command(
            label="Closed box", command=self.on_closed_box_calc)

        self.__main_menu.add_cascade(
            label="Calculations", menu=self.__calculations_menu)

        self.master.config(menu=self.__main_menu)

    def on_menu_exit(self):
        exit()

    def on_display_speaker_parameters(self):

        SpeakerWindow.SpeakerWindow(self, self.__speaker_configuration)

    def on_vented_sbb4_calc(self):

        self.__SBB4Calc = SBB4Calc.SBB4Calc(
            self.__speaker_configuration, self.__text_display)

        self.__SBB4Calc.calculate()

    def on_vented_qb3_calc(self):

        self.__QB3Calc = QB3Calc.QB3Calc(
            self.__speaker_configuration, self.__text_display)

        self.__QB3Calc.calculate()

    def on_closed_box_calc(self):

        self.__ClosedBoxCalc = ClosedBoxCalc.ClosedBoxCalc(
            self.__speaker_configuration, self.__text_display)

        self.__ClosedBoxCalc.calculate()

    def on_resize(self, event):

        self.__text_display["width"] = self.master.winfo_width()
        self.__text_display["height"] = self.master.winfo_height()
