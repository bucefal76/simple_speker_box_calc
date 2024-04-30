from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from Model import SpeakerConfiguration
from PIL import ImageTk, Image
#from test.test_decimal import file

import pickle


class SpeakerWindow(Toplevel):

    def __init__(self, master, speaker_configuration):
        super(SpeakerWindow, self).__init__(master)
        
        self.__filetypes = (
            ('Speaker description file', '*.bcs'),
        )

        self.__msg_box_result = False

        self.__check_btn_var = IntVar()

        self.title("Speaker parameters")
        self.geometry("")        
        
        self.resizable(False, False)
        self.create_widgets()

        self.__speaker_configuration = speaker_configuration

        self.update_widgets(self.__speaker_configuration)
        self.grab_set()  # I'm modal window now

        pass
    
    def GetSpeakerConfiguration(self):
        return self.__speaker_configuration

    def create_widgets(self):
                
        self.__image_single_driver = ImageTk.PhotoImage(Image.open("img_signle_driver.png"))
        self.__image_two_paralell_drivers = ImageTk.PhotoImage(Image.open("img_two_pararell_drivers.png"))
        self.__image_two_paralell_cascade_drivers  = ImageTk.PhotoImage(Image.open("img_two_pararell_cascade_drivers.png"))        

        self.__label_comment_param_name = Label(
            self, text="Parameter name")
        self.__label_comment_param_name.grid(row=1, column=0)
        
        self.__label_comment_value = Label(
            self, text="Value")
        self.__label_comment_value.grid(row=1, column=1)        

        self.__label_Qts = Label(self, text="qts:")
        self.__label_Qts.grid(row=2, column=0)

        self.__edit_Qts = Entry(self)
        self.__edit_Qts.grid(row=2, column=1)

        self.__label_Qes = Label(self, text="qes")
        self.__label_Qes.grid(row=3, column=0)

        self.__edit_Qes = Entry(self)
        self.__edit_Qes.grid(row=3, column=1)

        self.__label_Qms = Label(self, text="qms")
        self.__label_Qms.grid(row=4, column=0)

        self.__edit_Qms = Entry(self)
        self.__edit_Qms.grid(row=4, column=1)

        self.__label_Fs = Label(self, text="fs[Hz]")
        self.__label_Fs.grid(row=5, column=0)

        self.__edit_Fs = Entry(self)
        self.__edit_Fs.grid(row=5, column=1)

        self.__label_Re = Label(self, text="Re[Ohm]")
        self.__label_Re.grid(row=6, column=0)

        self.__edit_Re = Entry(self)
        self.__edit_Re.grid(row=6, column=1)

        self.__label_Vas = Label(self, text="vas[L]:")
        self.__label_Vas.grid(row=8, column=0)

        self.__edit_Vas = Entry(self)
        self.__edit_Vas.grid(row=8, column=1)

        self.__label_x_max = Label(self, text="Xmax [cm] (0-P):")
        self.__label_x_max.grid(row=10, column=0)
        self.__edit_x_max = Entry(self)
        self.__edit_x_max.grid(row=10, column=1)

        self.__label_sd = Label(self, text="Sd [cm2]:")
        self.__label_sd.grid(row=11, column=0)
        self.__edit_sd = Entry(self)
        self.__edit_sd.grid(row=11, column=1)

        self.__label_vent_diameter = Label(self, text="Vent diameter[cm]:")
        self.__label_vent_diameter.grid(row=12, column=0)
        self.__edit_vent_diameter = Entry(self)
        self.__edit_vent_diameter.grid(row=12, column=1)

        self.__label_vents_number = Label(self, text="Number of vents:")
        self.__label_vents_number.grid(row=13, column=0)
        self.__edit_vents_number = Entry(self)
        self.__edit_vents_number.grid(row=13, column=1)

        self.__label_no_of_speakers = Label(self, text="Speakers no.:")
        self.__label_no_of_speakers.grid(row=14, column=0)
        self.__no_of_speakers_list_box = Listbox(
            self, height=2, exportselection=0)
        self.__no_of_speakers_list_box.grid(row=14, column=1)
        self.__no_of_speakers_list_box.insert(0, "1")
        self.__no_of_speakers_list_box.insert(1, "2")
        self.__no_of_speakers_list_box.bind(
            '<<ListboxSelect>>', self.on_list_box_select)

        self.__label_Rc1 = Label(self, text="rc_1[Ohm]:")
        self.__label_Rc1.grid(row=15, column=0)

        self.__edit_Rc1 = Entry(self)
        self.__edit_Rc1.grid(row=15, column=1)

        self.__label_Rc2 = Label(self, text="rc_2[Ohm]:")
        self.__label_Rc2.grid(row=16, column=0)
        self.__label_Rc2.grid_remove()

        self.__edit_Rc2 = Entry(self)
        self.__edit_Rc2.grid(row=16, column=1)
        self.__edit_Rc2.grid_remove()

        self.__label_filters_in_cascade = Label(
            self, text="Note: If the filters are set in cascade for 2.5D, then rc_2 bis = rc_1 + rc_2")
        self.__label_filters_in_cascade.grid(row=17, column=1)

        self.__cascade_filters_check = Checkbutton(self, text="cascade filter",
                                                   command=self.on_check_btn,
                                                   variable=self.__check_btn_var,
                                                   onvalue=1, offvalue=0)
        self.__cascade_filters_check.grid(row=18, column=1)
                
        self.__image_panel = Label(self, image = self.__image_single_driver)
        self.__image_panel.grid(row=19, column=1)        

        self.__ok_button = Button(
            self, text="    Apply   ", command=self.on_OK)
        self.__ok_button.grid(row=20, column=3)
        
        self.__load_button = Button(
            self, text="    Load     ", command=self.on_Load)
        self.__load_button.grid(row=20, column=0)
        
        self.__save_button = Button(
            self, text="    Save     ", command=self.on_Save)
        self.__save_button.grid(row=20, column=1)
    
        self.__canvas_bottom = Label(self)
        self.__canvas_bottom.grid(row=21, column=1)
        self.__canvas_right = Label(self, text = "     ")
        self.__canvas_right.grid(row=21, column=4)
        

    def on_list_box_select(self, event):

        number_of_speakers = self.__no_of_speakers_list_box.curselection()

        if not number_of_speakers:
            return

        if number_of_speakers[0] == 1:
            self.__label_Rc2.grid()
            self.__edit_Rc2.grid()
            self.__speaker_configuration.numer_of_sepakers = 2
        else:
            self.__label_Rc2.grid_remove()
            self.__edit_Rc2.grid_remove()
            self.__speaker_configuration.numer_of_sepakers = 1
            self.__speaker_configuration.cascade = 0
            self.__cascade_filters_check.deselect()
            
        self.update_widgets(self.__speaker_configuration)

    def on_check_btn(self):
        self.__speaker_configuration.cascade = self.__check_btn_var.get()
        self.update_widgets(self.__speaker_configuration)

    def on_OK(self):
        self.update_data()
        if self.__msg_box_result == True:
            self.destroy()

    def on_Load(self): 
        file = filedialog.askopenfile(mode='rb',filetypes=self.__filetypes)
        if file is not None:            
            temp_speaker_configuration = pickle.load(file)
            self.update_widgets(temp_speaker_configuration)
        pass
    
    def on_Save(self):        
        self.update_data()        
        file = filedialog.asksaveasfile(mode='wb',filetypes=self.__filetypes, defaultextension=".bcs")
        if file is not None:
            pickle.dump(self.__speaker_configuration,file)
        pass

    def update_data(self):

        self.__msg_box_result = True

        try:
            self.__speaker_configuration.qts = float(self.__edit_Qts.get())
            self.__speaker_configuration.vas = float(self.__edit_Vas.get())
            self.__speaker_configuration.rc_1 = float(self.__edit_Rc1.get())
            self.__speaker_configuration.rc_2 = float(self.__edit_Rc2.get())
            self.__speaker_configuration.qes = float(self.__edit_Qes.get())
            self.__speaker_configuration.fs = float(self.__edit_Fs.get())
            self.__speaker_configuration.Re = float(self.__edit_Re.get())
            self.__speaker_configuration.qms = float(self.__edit_Qms.get())
            self.__speaker_configuration.x_max = float(self.__edit_x_max.get())
            self.__speaker_configuration.sd = float(self.__edit_sd.get())
            self.__speaker_configuration.vent_diameter = float(
                self.__edit_vent_diameter.get())
            self.__speaker_configuration.number_of_vents = float(
                self.__edit_vents_number.get())
        except ValueError:
            messagebox.showerror(
                title="BoxCalc", message="Bad value, not a float or int!")
            self.__msg_box_result = False

    def update_widgets(self, speakerConfiguration):
        self.__edit_Qts.delete(0, END)
        self.__edit_Qts.insert(0, str(speakerConfiguration.qts))
        
        self.__edit_Vas.delete(0, END)
        self.__edit_Vas.insert(0, str(speakerConfiguration.vas))
        
        self.__edit_Qes.delete(0, END)
        self.__edit_Qes.insert(0, str(speakerConfiguration.qes))
        
        self.__edit_Fs.delete(0, END)
        self.__edit_Fs.insert(0, str(speakerConfiguration.fs))
        
        self.__edit_Re.delete(0, END)
        self.__edit_Re.insert(0, str(speakerConfiguration.Re))
        
        self.__edit_Qms.delete(0, END)
        self.__edit_Qms.insert(0, str(speakerConfiguration.qms))
        
        self.__edit_x_max.delete(0, END)
        self.__edit_x_max.insert(0, str(speakerConfiguration.x_max))
        
        self.__edit_sd.delete(0, END)
        self.__edit_sd.insert(0, str(speakerConfiguration.sd))
        
        self.__edit_vent_diameter.delete(0, END)
        self.__edit_vent_diameter.insert(
            0, str(speakerConfiguration.vent_diameter))
        
        self.__edit_vents_number.delete(0, END)
        self.__edit_vents_number.insert(
            0, str(speakerConfiguration.number_of_vents))

        self.__no_of_speakers_list_box.selection_clear(0, END)
        
        if speakerConfiguration.numer_of_sepakers == 1:
            self.__no_of_speakers_list_box.select_set(0)
            self.__label_Rc2.grid_remove()
            self.__edit_Rc2.grid_remove()            
            self.__image_panel['image'] = self.__image_single_driver
        else:
            self.__no_of_speakers_list_box.select_set(1)
            self.__label_Rc2.grid()
            self.__edit_Rc2.grid()
            
            if speakerConfiguration.cascade == 0:
                self.__image_panel['image'] = self.__image_two_paralell_drivers
            else:
                self.__image_panel['image'] = self.__image_two_paralell_cascade_drivers            

        if speakerConfiguration.cascade == 0:
            self.__cascade_filters_check.deselect()
        else:
            self.__cascade_filters_check.select()

        self.__edit_Rc1.delete(0, END)
        self.__edit_Rc1.insert(0, str(speakerConfiguration.rc_1))
                
        self.__edit_Rc2.delete(0, END)
        self.__edit_Rc2.insert(0, str(speakerConfiguration.rc_2))
