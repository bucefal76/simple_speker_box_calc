class VentCalculator:

    def __init__(self, speaker_configuration, display):

        self.__speaker_configuration = speaker_configuration

        self.__display = display

    def claclulate(self, v_box, f_box,):

        # Port Length
        # The port length required to tune a volume of air to a specific frequency can be calculated by using the following equation:
        #
        # Lv = (23562.5*Dv^2*Np/(Fb^2*Vb))-(k*Dv), where:
        #
        # Dv = port diameter (cm)
        # Fb = tuning frequency (Hz)
        # Vb = net volume (litres)
        # Lv = length of each port (cm)
        # Np = number of ports
        # k = end correction (normally 0.732)
        # The value for k, the end correction, can be fine-tuned by using the following values to derive the appropriate end correction figure for each end of the port, then adding them together
        # Both ends flanged: k = 0.425 + 0.425 = 0.850
        # One end flanged, one end free: k = 0.425 + 0.307 = 0.732
        # Both ends free: k = 0.307 + 0.307 = 0.614
        # Normally, k=0.732 is assumed.
        #
        # Source: http://www.troelsgravesen.dk/vent_tuning.htm

        self.__display.println("Circle shaped vent dimentions calculation.")
        self.__display.println("Vent one end flanged, one end free.")

        total_vent_diameter = self.__speaker_configuration.vent_diameter * \
            self.__speaker_configuration.number_of_vents

        self.__display.print(
            "Total vent diameter (considers all vents together) [cm]: ")
        self.__display.println(str(total_vent_diameter))

        lv = ((23562.5 * (total_vent_diameter ** 2) * self.__speaker_configuration.number_of_vents) /
              ((f_box**2) * v_box)) - (0.732 * total_vent_diameter)

        total_x_max = self.__speaker_configuration.x_max * \
            self.__speaker_configuration.numer_of_sepakers

        self.__display.print(
            "Total x max (considers all speakers together) [cm]: ")
        self.__display.println(str(total_x_max))

        # Convert SD to mm2 and multiply by number of speakers
        total_sd = (self.__speaker_configuration.sd / 10000) * \
            self.__speaker_configuration.numer_of_sepakers

        vd = (total_sd * total_x_max) / 1000

        total_minimum_vent_diamater = (100 * (20.3 * ((vd**2 / f_box)**0.25))) / \
            (self.__speaker_configuration.number_of_vents**0.5)

        self.__display.println(
            "-----------------------------------------------------------")
        self.__display.print("Vent length [cm]: ")
        self.__display.println(str(lv))
        self.__display.print("Vent minimum diameter [cm]: ")
        self.__display.println(str(total_minimum_vent_diamater))
        if (total_minimum_vent_diamater >= total_vent_diameter):
            self.__display.println(
                "ERROR: Total vent diameter is lesser than minimum vent diameter!")
        self.__display.println(
            "-----------------------------------------------------------")

        pass
