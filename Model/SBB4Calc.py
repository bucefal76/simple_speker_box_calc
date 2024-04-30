from Model import SpeakerParametersCorrector
from Model import VentCalculator
from datetime import datetime


class SBB4Calc:

    def __init__(self, speaker_configuration, display):

        self.__speaker_configuration = speaker_configuration

        self.__display = display

        self.__Rc2C = self.__speaker_configuration.rc_2

    def sbb4(self, qts):

        if qts <= 0.2:
            return (1, 5.9)
        elif qts <= 0.21:
            return (1, 5.3)
        elif qts <= 0.22:
            return (1, 4.8)
        elif qts <= 0.23:
            return (1, 4.3)
        elif qts <= 0.24:
            return (1, 4)
        elif qts <= 0.25:
            return (1, 3.7)
        elif qts <= 0.26:
            return (1, 3.4)
        elif qts <= 0.27:
            return (1, 3.2)
        elif qts <= 0.28:
            return (1, 2.9)
        elif qts <= 0.29:
            return (1, 2.7)
        elif qts <= 0.30:
            return (1, 2.5)
        elif qts <= 0.31:
            return (1, 2.4)
        elif qts <= 0.32:
            return (1, 2.2)
        elif qts <= 0.33:
            return (1, 2.1)
        elif qts <= 0.34:
            return (1, 2.0)
        elif qts <= 0.35:
            return (1, 1.8)
        elif qts <= 0.36:
            return (1, 1.7)
        elif qts <= 0.37:
            return (1, 1.6)
        elif qts <= 0.38:
            return (1, 1.5)
        elif qts <= 0.39:
            return (1, 1.5)
        elif qts <= 0.40:
            return (1, 1.4)
        elif qts <= 0.41:
            return (1, 1.3)
        elif qts <= 0.42:
            return (1, 1.3)
        elif qts <= 0.43:
            return (1, 1.2)
        elif qts <= 0.44:
            return (1, 1.1)
        elif qts <= 0.45:
            return (1, 1.1)
        elif qts <= 0.46:
            return (1, 1.0)
        elif qts <= 0.47:
            return (1, 1.0)
        elif qts <= 0.48:
            return (1, 0.9)
        elif qts <= 0.49:
            return (1, 0.9)
        elif qts <= 0.50:
            return (1, 0.9)
        elif qts <= 0.51:
            return (1, 0.8)
        elif qts <= 0.52:
            return (1, 0.8)
        elif qts <= 0.53:
            return (1, 0.8)
        elif qts <= 0.54:
            return (1, 0.7)
        elif qts <= 0.55:
            return (1, 0.7)
        elif qts <= 0.56:
            return (1, 0.7)
        elif qts <= 0.57:
            return (1, 0.6)
        elif qts <= 0.58:
            return (1, 0.6)
        elif qts <= 0.58:
            return (1, 0.6)
        elif qts <= 0.59:
            return (1, 0.6)
        elif qts <= 0.60:
            return (1, 0.6)
        else:
            self.__display.print(
                "ERROR: QtsC value is out of SBB4 requirements, (over 0.60), QtsC: ")
            self.__display.println(str(qts))
            raise ValueError('Aborting calculation bad input data!')

    def calculate(self):

        self.__display.println(
            "***********************************************************")
        self.__display.println(datetime.now())
        self.__display.println("Calulate the SBB4 box for the parameters:")

        speakers_param_corrector = SpeakerParametersCorrector.SpeakerParametersCorrector(
            self.__speaker_configuration, self.__display)

        sbb4_1_tuple = self.sbb4(speakers_param_corrector.qts_1_c)
        h_1, alfa_1 = sbb4_1_tuple
        fb_1 = self.__speaker_configuration.fs * h_1
        vb_1 = self.__speaker_configuration.vas / alfa_1

        self.__display.print("Calculated speaker 1 Vb1[L]: ")
        self.__display.println(str(vb_1))
        self.__display.print("Calculated speaker 1 Fb1[Hz]: ")
        self.__display.println(str(fb_1))

        vb_2 = 0

        if self.__speaker_configuration.numer_of_sepakers > 1:

            sbb4_2_tuple = self.sbb4(speakers_param_corrector.qts_2_c)

            h_2, alfa_2 = sbb4_2_tuple
            fb_2 = self.__speaker_configuration.fs * h_2
            vb_2 = self.__speaker_configuration.vas / alfa_2

            self.__display.print("Calculated speaker 2 Vb2[L]: ")
            self.__display.println(str(vb_2))
            self.__display.print("Calculated speaker 2 Fb2[Hz]: ")
            self.__display.println(str(fb_2))

        vb = vb_1 + vb_2

        self.__display.println(
            "-----------------------------------------------------------")
        self.__display.print("Calculated loudspeaker net Vb[L]: ")
        self.__display.println(str(vb))
        self.__display.print("Calculated loudspeaker Fb[Hz]: ")
        self.__display.println(str(fb_1))
        self.__display.println(
            "-----------------------------------------------------------")

        vent_calculator = VentCalculator.VentCalculator(
            self.__speaker_configuration, self.__display)
        vent_calculator.claclulate(vb, fb_1)
