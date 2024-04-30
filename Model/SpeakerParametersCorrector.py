class SpeakerParametersCorrector:

    def __init__(self, speaker_configuration, display):

        self.__speaker_configuration = speaker_configuration
        self.__display = display

        self.__qts_1_c = 0
        self.__qts_2_c = 0

        self.__calculate()

    def __check_speaker_params(self):

        if self.__speaker_configuration.Re == 0:
            self.__display.print("ERROR: Re value is 0!")
            return False
        if self.__speaker_configuration.Re < 0:
            self.__display.print("ERROR: Re value is < 0!")
            return False

        return True

    def __calculate(self):

        self.__display.print("Speaker count: ")
        self.__display.println(
            str(self.__speaker_configuration.numer_of_sepakers))
        self.__display.print("Speaker qts: ")
        self.__display.println(str(self.__speaker_configuration.qts))
        self.__display.print("Speaker qes: ")
        self.__display.println(str(self.__speaker_configuration.qes))
        self.__display.print("Speaker qms: ")
        self.__display.println(str(self.__speaker_configuration.qms))
        self.__display.print("Speaker fs[Hz]: ")
        self.__display.println(str(self.__speaker_configuration.fs))
        self.__display.print("Speaker vas[L]: ")
        self.__display.println(str(self.__speaker_configuration.vas))
        self.__display.print("Speaker Re[Ohm]: ")
        self.__display.println(str(self.__speaker_configuration.Re))

        if self.__speaker_configuration.cascade == 1:
            self.__display.println("INFO: Cascade filtering is selected!")

        if self.__check_speaker_params() == False:
            raise ValueError('Aborting calculation bad input data!')

        self.__display.print(
            "Aditional filter inductor coil for first speaker rc_1[Ohm]: ")
        self.__display.println(str(self.__speaker_configuration.rc_1))

        if self.__speaker_configuration.numer_of_sepakers > 1:
            self.__display.print(
                "Aditional filter inductor coil for second speaker rc_2[Ohm]: ")
            self.__display.println(str(self.__speaker_configuration.rc_2))
            if self.__speaker_configuration.cascade == 1:
                self.__display.print(
                    "Second speaker is connected over cascade filter, so Rc2C(corrected)[Ohm]: ")
                self.__display.println(
                    str(self.__speaker_configuration.rc_1 + self.__speaker_configuration.rc_2))

        self.__display.print("Speaker 1 QesC(qes corrected by rc_1): ")
        Qes1C = self.__speaker_configuration.qes * \
            ((self.__speaker_configuration.rc_1 +
              self.__speaker_configuration.Re) / self.__speaker_configuration.Re)
        self.__display.println(str(Qes1C))

        self.__display.print("Speaker 1 QtsC(Qtc corrected by rc_1): ")
        self.__qts_1_c = (Qes1C * self.__speaker_configuration.qms) / \
            (Qes1C + self.__speaker_configuration.qms)
        self.__display.println(str(self.__qts_1_c))

        if self.__speaker_configuration.numer_of_sepakers > 1:
            if self.__speaker_configuration.cascade == 0:
                self.__display.print("Speaker 2 QesC(qes corrected by rc_2): ")
                Qes2C = self.__speaker_configuration.qes * \
                    ((self.__speaker_configuration.rc_2 +
                      self.__speaker_configuration.Re) / self.__speaker_configuration.Re)
                self.__display.println(str(Qes2C))

                self.__display.print("Speaker 2 QtsC(Qtc corrected by rc_2): ")
                self.__qts_2_c = (Qes2C * self.__speaker_configuration.qms) / \
                    (Qes2C + self.__speaker_configuration.qms)
                self.__display.println(str(self.__qts_2_c))
            else:
                self.__display.print(
                    "Speaker 2 QesC(qes corrected by rc_1+rc_2): ")
                Qes2C = self.__speaker_configuration.qes * \
                    ((self.__speaker_configuration.rc_1 + self.__speaker_configuration.rc_2 +
                      self.__speaker_configuration.Re) / self.__speaker_configuration.Re)
                self.__display.println(str(Qes2C))

                self.__display.print(
                    "Speaker 2 QtsC(Qtc corrected by rc_1+rc_2): ")
                self.__qts_2_c = (Qes2C * self.__speaker_configuration.qms) / \
                    (Qes2C + self.__speaker_configuration.qms)
                self.__display.println(str(self.__qts_2_c))

    @property
    def qts_1_c(self):
        return self.__qts_1_c

    @property
    def qts_2_c(self):
        return self.__qts_2_c
