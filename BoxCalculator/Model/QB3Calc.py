from Model import SpeakerParametersCorrector
from Model import VentCalculator
from datetime import datetime


class QB3Calc:

    def __init__(self, speaker_configuration, display):

        self.__speaker_configuration = speaker_configuration

        self.__display = display

    def __check_speaker_params(self):

        if self.__speaker_configuration.cascade == True:
            self.__display.println(
                "ERROR: QB3 cannot be calculated for cascade filter configuration!")
            raise ValueError('Aborting calculation bad input data!')
        if self.__speaker_configuration.numer_of_sepakers != 1:
            if self.__speaker_configuration.rc_1 != self.__speaker_configuration.rc_2:
                self.__display.println(
                    "ERROR: QB3 cannot be calculated when rc_1 != rc_2!")
                raise ValueError('Aborting calculation bad input data!')

    def qb3(self, qts):

        if qts <= 0.20:
            return (1.9, 7.8)
        elif qts <= 0.21:
            return (1.8, 7.0)
        elif qts <= 0.22:
            return (1.8, 6.2)
        elif qts <= 0.23:
            return (1.7, 5.6)
        elif qts <= 0.24:
            return (1.6, 5.1)
        elif qts <= 0.25:
            return (1.6, 4.6)
        elif qts <= 0.26:
            return (1.5, 4.2)
        elif qts <= 0.27:
            return (1.5, 3.8)
        elif qts <= 0.28:
            return (1.4, 3.4)
        elif qts <= 0.29:
            return (1.4, 3.1)
        elif qts <= 0.30:
            return (1.3, 2.8)
        elif qts <= 0.31:
            return (1.3, 2.6)
        elif qts <= 0.32:
            return (1.2, 2.5)
        elif qts <= 0.33:
            return (1.2, 2.2)
        elif qts <= 0.34:
            return (1.2, 2.0)
        elif qts <= 0.35:
            return (1.4, 1.8)
        elif qts <= 0.36:
            return (1.4, 1.6)
        elif qts <= 0.37:
            return (1.4, 1.6)
        elif qts <= 0.38:
            return (1.4, 1.4)
        elif qts <= 0.39:
            return (1.0, 1.2)
        elif qts <= 0.40:
            return (1.0, 1.1)
        elif qts <= 0.41:
            return (1.0, 1.0)
        else:
            self.__display.print(
                "ERROR: QtsC value is out of QBS requrements, (over 0.41), QtsC: ")
            self.__display.println(str(qts))
            raise ValueError('Aborting calculation bad input data!')

    def calculate(self):

        self.__display.println(
            "***********************************************************")
        self.__display.println(datetime.now())
        self.__display.println("Calulate the QB3 box for the parameters:")

        if self.__check_speaker_params() == False:
            return

        speakers_param_corrector = SpeakerParametersCorrector.SpeakerParametersCorrector(
            self.__speaker_configuration, self.__display)

        qb3_tuple = self.qb3(speakers_param_corrector.qts_1_c)

        h, alfa = qb3_tuple
        fb = self.__speaker_configuration.fs * h
        vb = (self.__speaker_configuration.vas / alfa) * \
            self.__speaker_configuration.numer_of_sepakers

        self.__display.println(
            "-----------------------------------------------------------")
        self.__display.print("Calculated loudspeaker net Vb[L]: ")
        self.__display.println(str(vb))
        self.__display.print("Calculated loudspeaker Fb[Hz]: ")
        self.__display.println(str(fb))
        self.__display.println(
            "-----------------------------------------------------------")

        vent_calculator = VentCalculator.VentCalculator(
            self.__speaker_configuration, self.__display)
        vent_calculator.claclulate(vb, fb)
