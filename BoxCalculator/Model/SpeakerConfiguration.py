class SpeakerConfiguration:

    def __init__(self):
        self.__qts = 0.35
        self.__qes = 0.42
        self.__qms = 1.90
        self.__fs = 37
        self.__re = 6.20
        self.__le = 0.28
        self.__vas = 28
        self.__number_of_spekers = 1
        self.__rc_1 = 0.25
        self.__rc_2 = 0.47
        self.__filters_in_cascasde = 0
        self.__vent_diameter = 5
        self.__number_of_vents = 1
        self.__x_max = 0.6
        self.__sd = 133

    @property
    def qts(self):
        return self.__qts

    @qts.setter
    def qts(self, val):
        self.__qts = val

    @property
    def qes(self):
        return self.__qes

    @qes.setter
    def qes(self, val):
        self.__qes = val

    @property
    def qms(self):
        return self.__qms

    @qms.setter
    def qms(self, val):
        self.__qms = val

    @property
    def fs(self):
        return self.__fs

    @fs.setter
    def fs(self, val):
        self.__fs = val

    @property
    def Re(self):
        return self.__re

    @Re.setter
    def Re(self, val):
        self.__re = val

    @property
    def vas(self):
        return self.__vas

    @vas.setter
    def vas(self, val):
        self.__vas = val

    @property
    def numer_of_sepakers(self):
        return self.__number_of_spekers

    @numer_of_sepakers.setter
    def numer_of_sepakers(self, val):
        self.__number_of_spekers = val

    @property
    def rc_1(self):
        return self.__rc_1

    @rc_1.setter
    def rc_1(self, val):
        self.__rc_1 = val

    @property
    def rc_2(self):
        return self.__rc_2

    @rc_2.setter
    def rc_2(self, val):
        self.__rc_2 = val

    @property
    def cascade(self):
        return self.__filters_in_cascasde

    @cascade.setter
    def cascade(self, val):
        self.__filters_in_cascasde = val

    @property
    def vent_diameter(self):
        return self.__vent_diameter

    @vent_diameter.setter
    def vent_diameter(self, val):
        self.__vent_diameter = val

    @property
    def x_max(self):
        return self.__x_max

    @x_max.setter
    def x_max(self, val):
        self.__x_max = val

    @property
    def sd(self):
        return self.__sd

    @sd.setter
    def sd(self, val):
        self.__sd = val

    @property
    def number_of_vents(self):
        return self.__number_of_vents

    @number_of_vents.setter
    def number_of_vents(self, val):
        self.__number_of_vents = val
