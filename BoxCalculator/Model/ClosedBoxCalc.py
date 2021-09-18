from datetime import datetime
import math


class ClosedBoxCalc:

    def __init__(self, speaker_configuration, display):

        self.__speaker_configuration = speaker_configuration

        self.__display = display

    def ClosedBox(self, qtc):

        self.__display.println(
            "-----------------------------------------------------------")
        self.__display.print("Calculate closed box volume for Qtc: ")
        self.__display.println(str(qtc))

        alfa = ((qtc / self.__speaker_configuration.qts)**2) - 1
        vb = self.__speaker_configuration.vas / alfa

        vb = vb * self.__speaker_configuration.numer_of_sepakers

        self.__display.print("Box net volume [L]: ")
        self.__display.println(str(vb))

        fc = self.__speaker_configuration.fs * math.sqrt(alfa + 1)
        self.__display.print("Box and speaker Fc [Hz]: ")
        self.__display.println(str(fc))

        # f3 = { { (1/Qtc2 -2) + [(1/Qtc2 -2)2 + 4]1/2 } /2 }1/2 * fc
        # https://audiojudgement.com/sealed-enclosure-closed-box/

        c1 = (1 / qtc**2) - 2
        c2 = math.sqrt((((1 / qtc**2) - 2)**2) + 4)
        f3 = math.sqrt((c1 + c2) / 2) * fc

        self.__display.print("Box and speaker F3 [Hz]: ")
        self.__display.println(str(f3))

    def calculate(self):

        self.__display.println(
            "***********************************************************")
        self.__display.println(datetime.now())
        self.__display.println(
            "Calulate the Closed Box volume (nett volume, no stuffing):")

        self.ClosedBox(0.5)
        self.ClosedBox(0.6)
        self.ClosedBox(0.707)
        self.ClosedBox(0.75)
        self.ClosedBox(0.8)
        self.ClosedBox(0.9)
        self.ClosedBox(1)
        self.ClosedBox(1.1)
        self.ClosedBox(1.2)

        self.__display.println(
            "-----------------------------------------------------------")

        ebp = self.__speaker_configuration.fs / self.__speaker_configuration.qes

        self.__display.print("INFO: EBP (efficiency bandwidth product):")
        self.__display.println(str(ebp))

        if ebp < 50:
            self.__display.println(
                "INFO: The EBP < 50, selected speaker is good to work in the closed box.")
        elif ebp < 100:
            self.__display.println(
                "INFO: The EBP < 100, selected speaker is good enough to work in the closed box.")
        else:
            self.__display.println(
                "INFO: The EBP > 100, selected speaker is not recommended to work in the closed box.")

        self.__display.println("INFO: Recommended Qtc values: 0.7 up to 0.9.")
        self.__display.println(
            "INFO: Put stuffing into the box, more stuffing is always better.")
        self.__display.println(
            "INFO: Consider box dimentions relation (w:d:h): 1:1.25:1.6, 1:1.45:2.1, 1:1.6:2.5")

        self.__display.println(
            "-----------------------------------------------------------")
