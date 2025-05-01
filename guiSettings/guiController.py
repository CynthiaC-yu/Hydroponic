from tkinter import simpledialog, messagebox
from tktimepicker import AnalogPicker, AnalogThemes
import tkinter as tk
import serial
import serial.tools.list_ports


def gui_controller(tab2):
    """
    Function to create a GUI for controlling various systems in a hydroponic setup.
    """
    ports = serial.tools.list_ports.comports()
    portsList = []

    def hint():
        """
        Function to generate hint string for serial port selection.
        Returns:
        str: Serial result, which is the input value for com
        """
        result = ""
        for port, desc, hwid in sorted(ports):
            portsList.append(port)
            print("{}: {}".format(port, desc))
            result = result + "{}: {}".format(port, desc) + "\n"
        return result
    # Ask user to select a serial port
    com = simpledialog.askstring("Select Serial Port", hint() + "\n" +
                                  "Select the serial port for Arduino (e.g., /dev/tty.usbmodemXXXX): ")

    if com:
        messagebox.showinfo("Success", "Serial port is selected successfully")

    # Initialize serial connection with Arduino
    arduino = serial.Serial(com, 9600)  # Adjust the port and baud rate as needed

    # Labels and buttons for selecting controllers
    label = tk.Label(tab2, text='Select the controller you want to check: ', anchor=tk.NW)
    label.pack()

    # # button widget
    btn_lighting_system = tk.Button(tab2, text="Lighting System", command=lambda: create_controller_windows(tab2, "LightingSystem"))
    btn_lighting_system.pack()
    btn_nutrition_system = tk.Button(tab2, text="Nutrition System", command=lambda: create_controller_windows(tab2, "NutritionSystem"))
    btn_nutrition_system.pack()
    btn_temperature_system = tk.Button(tab2, text="Temperature System",  command=lambda: create_controller_windows(tab2, "TemperatureSystem"))
    btn_temperature_system.pack()
    btn_oxygen_system = tk.Button(tab2, text="Oxygen System", command=lambda: create_controller_windows(tab2, "OxygenSystem"))
    btn_oxygen_system.pack()
    btn_moisture_system = tk.Button(tab2, text="Moisture System", command=lambda: create_controller_windows(tab2, "MoistureSystem"))
    btn_moisture_system.pack()
    btn_ventilation_system = tk.Button(tab2, text="Ventilation System",  command=lambda: create_controller_windows(tab2, "VentilationSystem"))
    btn_ventilation_system.pack()

    def switch(is_on, btn, status):
        """
        Function to switch on/off a system and update its status.

        Args:
            is_on (str): Current status of the system.
            btn (tk.Button): Button widget representing the system.
            status (tk.Label): Label widget representing the status of the system.
        """
        # Determine is on or off
        if is_on == "On":
            btn.config(text="Off", fg="grey")
            status.config(text="Off", fg="grey")
            is_on = "Off"
            arduino.write(b'0')  # Send '0' to turn off the LED
        else:
            btn.config(text="On", fg="green")
            status.config(text="On", fg="green")
            is_on = "On"
            arduino.write(b'1')  # Send '1' to turn on the LED

    def create_controller_windows(window, controller):
        """
        Function to create a window for controlling a specific system.

        Args:
            window: Parent window where the controller window will be created.
            controller (str): Name of the system being controlled.
        """
        # create a pop up window
        controller_window = tk.Toplevel(window)
        controller_window.geometry("1000x500")
        controller_window.title(controller)
        controller_window.config(bg="light blue")

        # widgets of lighting system
        if controller == "LightingSystem":
            l_lighting_switch = tk.Label(controller_window, text="Switch")
            l_lighting_switch.config(font=("Courier", 14))
            l_lighting_switch.grid(row=0, column=0)

            l_lighting_auto = tk.Label(controller_window, text="Auto mode")
            l_lighting_auto.config(font=("Courier", 14))
            l_lighting_auto.grid(row=1, column=0)

            l_switch_status = tk.Label(controller_window, text="Off")
            l_switch_status.config(font=("Courier", 14))
            l_switch_status.grid(row=0, column=2)

            l_auto_status = tk.Label(controller_window, text="Off")
            l_auto_status.config(font=("Courier", 14))
            l_auto_status.grid(row=1, column=2)

            btn_lighting_switch = tk.Button(controller_window, text="Off", bd=0,
                                            command=lambda: switch(btn_lighting_switch.cget('text'),
                                                                   btn_lighting_switch, l_switch_status))
            btn_lighting_switch.config(fg="grey")
            btn_lighting_switch.grid(row=0, column=1)

            btn_lighting_auto = tk.Button(controller_window, text="Off", bd=0,
                                          command=lambda: switch(btn_lighting_auto.cget('text'), btn_lighting_auto,
                                                                 l_auto_status))
            btn_lighting_auto.config(fg="grey")
            btn_lighting_auto.grid(row=1, column=1)

            l_auto_mode = tk.Label(controller_window, text="Auto Mode")
            l_auto_mode.config(font=("Courier", 20), fg="Pink")
            l_auto_mode.grid(row=2, column=1)

            l_lighting_start = tk.Label(controller_window, text="Start Time")
            l_lighting_start.config(font=("Courier", 14))
            l_lighting_start.grid(row=3, column=0)

            l_lighting_end = tk.Label(controller_window, text="End Time")
            l_lighting_end.config(font=("Courier", 14))
            l_lighting_end.grid(row=4, column=0)

            time_picker_lighting_start = AnalogPicker(controller_window)
            time_picker_lighting_start.grid(row=3, column=1)
            theme = AnalogThemes(time_picker_lighting_start)
            theme.setDracula()

            time_picker_lighting_end = AnalogPicker(controller_window)
            time_picker_lighting_end.grid(row=4, column=1)
            theme = AnalogThemes(time_picker_lighting_end)
            theme.setDracula()

        # widgets of nutrition system
        if controller == "NutritionSystem":
            l_nutrition_switch = tk.Label(controller_window, text="Switch")
            l_nutrition_switch.config(font=("Courier", 14))
            l_nutrition_switch.grid(row=0, column=0)

            l_nutrition_auto = tk.Label(controller_window, text="Auto mode")
            l_nutrition_auto.config(font=("Courier", 14))
            l_nutrition_auto.grid(row=1, column=0)

            l_switch_status = tk.Label(controller_window, text="Off")
            l_switch_status.config(font=("Courier", 14))
            l_switch_status.grid(row=0, column=2)

            l_auto_status = tk.Label(controller_window, text="Off")
            l_auto_status.config(font=("Courier", 14))
            l_auto_status.grid(row=1, column=2)

            btn_nutrition_switch = tk.Button(controller_window, text="Off", bd=0,
                                             command=lambda: switch(btn_nutrition_switch.cget('text'),
                                                                    btn_nutrition_switch,
                                                                    l_switch_status))
            btn_nutrition_switch.config(fg="grey")
            btn_nutrition_switch.grid(row=0, column=1)

            btn_nutrition_auto = tk.Button(controller_window, text="Off", bd=0,
                                           command=lambda: switch(btn_nutrition_auto.cget('text'), btn_nutrition_auto,
                                                                  l_auto_status))
            btn_nutrition_auto.config(fg="grey")
            btn_nutrition_auto.grid(row=1, column=1)

            l_auto_mode = tk.Label(controller_window, text="Auto Mode")
            l_auto_mode.config(font=("Courier", 20), fg="Pink")
            l_auto_mode.grid(row=2, column=1)

            btn_select = tk.Button(controller_window, text="Select", bd=0)
            btn_select.config(fg="black")
            btn_select.grid(row=3, column=3)

            def get_spinner_value(spinner1, spinner2):
                print(spinner1.get())
                print(spinner2.get())
                l_condition_sentence.config(
                    text="If the nutrition concentration is lower than " + str(spinner1.get()) + " ppm\n"
                         + "add " + str(spinner2.get()) + " ml nutrition solution.")

            btn_select.bind("<Button-1>",
                            lambda event: get_spinner_value(spin_nutrition_condition, spin_nutrition_solution))

            l_spin_nutrition_condition = tk.Label(controller_window, text="Choose nutrition concentration: ")
            l_spin_nutrition_condition.config(font=("Courier", 14))
            l_spin_nutrition_condition.grid(row=4, column=0)
            l_spin_nutrition_solution = tk.Label(controller_window, text="Choose quantity of nutrition solution: ")
            l_spin_nutrition_solution.config(font=("Courier", 14))
            l_spin_nutrition_solution.grid(row=5, column=0)

            spin_nutrition_condition = tk.Spinbox(controller_window, from_=0, to=10)
            spin_nutrition_condition.grid(row=4, column=1)
            spin_nutrition_solution = tk.Spinbox(controller_window, from_=0, to=10)
            spin_nutrition_solution.grid(row=5, column=1)

            l_condition_sentence = tk.Label(controller_window)
            l_condition_sentence.config(text="If the nutrition concentration is lower than " + "0" + " ppm\n"
                                             + "add " + "0" + " ml nutrition solution.")
            l_condition_sentence.grid(row=3, column=1)

        # widgets of temperature system
        if controller == "TemperatureSystem":
            l_heater_switch = tk.Label(controller_window, text="Heater Switch")
            l_heater_switch.config(font=("Courier", 14))
            l_heater_switch.grid(row=0, column=0)

            l_cooler_switch = tk.Label(controller_window, text="Cooler Switch")
            l_cooler_switch.config(font=("Courier", 14))
            l_cooler_switch.grid(row=1, column=0)

            l_temperature_auto = tk.Label(controller_window, text="Auto mode")
            l_temperature_auto.config(font=("Courier", 14))
            l_temperature_auto.grid(row=2, column=0)

            l_switch_heater_status = tk.Label(controller_window, text="Off")
            l_switch_heater_status.config(font=("Courier", 14))
            l_switch_heater_status.grid(row=0, column=2)

            l_switch_cooler_status = tk.Label(controller_window, text="Off")
            l_switch_cooler_status.config(font=("Courier", 14))
            l_switch_cooler_status.grid(row=1, column=2)

            btn_heater_switch = tk.Button(controller_window, text="Off", bd=0,
                                          command=lambda: switch(btn_heater_switch.cget('text'), btn_heater_switch,
                                                                 l_switch_heater_status))
            btn_heater_switch.config(fg="grey")
            btn_heater_switch.grid(row=0, column=1)

            btn_cooler_switch = tk.Button(controller_window, text="Off", bd=0,
                                          command=lambda: switch(btn_cooler_switch.cget('text'), btn_cooler_switch,
                                                                 l_switch_cooler_status))
            btn_cooler_switch.config(fg="grey")
            btn_cooler_switch.grid(row=1, column=1)

            btn_temperature_auto = tk.Button(controller_window, text="Off", bd=0,
                                             command=lambda: switch(btn_temperature_auto.cget('text'),
                                                                    btn_temperature_auto,
                                                                    l_auto_status))
            btn_temperature_auto.config(fg="grey")
            btn_temperature_auto.grid(row=2, column=1)

            l_auto_status = tk.Label(controller_window, text="Off")
            l_auto_status.config(font=("Courier", 14))
            l_auto_status.grid(row=2, column=2)

            l_auto_mode = tk.Label(controller_window, text="Auto Mode")
            l_auto_mode.config(font=("Courier", 20), fg="Pink")
            l_auto_mode.grid(row=3, column=1)

            btn_select = tk.Button(controller_window, text="Select", bd=0)
            btn_select.config(fg="black")
            btn_select.grid(row=4, column=3)

            def get_spinner_value(spinner1, spinner2):
                print(spinner1.get())
                print(spinner2.get())
                l_condition_sentence.config(
                    text="if the room temperature is lower than " + str(
                        spinner1.get()) + " Celsius Degrees then turn on the heater;\n"
                         + "if the room temperature is higher than " + str(
                        spinner2.get()) + " Celsius Degrees then turn on the cooler.")

            btn_select.bind("<Button-1>", lambda event: get_spinner_value(spin_temp_low, spin_temp_high))

            l_spin_temp_low = tk.Label(controller_window, text="Choose lower temperature boundary: ")
            l_spin_temp_low.config(font=("Courier", 14))
            l_spin_temp_low.grid(row=5, column=0)
            l_spin_temp_high = tk.Label(controller_window, text="Choose higher temperature boundary: ")
            l_spin_temp_high.config(font=("Courier", 14))
            l_spin_temp_high.grid(row=6, column=0)

            spin_temp_low = tk.Spinbox(controller_window, from_=0, to=10)
            spin_temp_low.grid(row=5, column=1)
            spin_temp_high = tk.Spinbox(controller_window, from_=0, to=10)
            spin_temp_high.grid(row=6, column=1)

            l_condition_sentence = tk.Label(controller_window)
            l_condition_sentence.config(
                text="if the room temperature is lower than " + "0" + " Celsius Degrees then turn on the heater;\n"
                     + "if the room temperature is higher than " + "0" + " Celsius Degrees then turn on the cooler.")
            l_condition_sentence.grid(row=4, column=1)

        # widgets of oxygen system
        if controller == "OxygenSystem":
            l_oxygen_switch = tk.Label(controller_window, text="Switch")
            l_oxygen_switch.config(font=("Courier", 14))
            l_oxygen_switch.grid(row=0, column=0)

            l_oxygen_auto = tk.Label(controller_window, text="Auto mode")
            l_oxygen_auto.config(font=("Courier", 14))
            l_oxygen_auto.grid(row=1, column=0)

            l_switch_status = tk.Label(controller_window, text="Off")
            l_switch_status.config(font=("Courier", 14))
            l_switch_status.grid(row=0, column=2)

            l_auto_status = tk.Label(controller_window, text="Off")
            l_auto_status.config(font=("Courier", 14))
            l_auto_status.grid(row=1, column=2)

            btn_oxygen_switch = tk.Button(controller_window, text="Off", bd=0,
                                          command=lambda: switch(btn_oxygen_switch.cget('text'),
                                                                 btn_oxygen_switch,
                                                                 l_switch_status))
            btn_oxygen_switch.config(fg="grey")
            btn_oxygen_switch.grid(row=0, column=1)

            btn_oxygen_auto = tk.Button(controller_window, text="Off", bd=0,
                                        command=lambda: switch(btn_oxygen_auto.cget('text'), btn_oxygen_auto,
                                                               l_auto_status))
            btn_oxygen_auto.config(fg="grey")
            btn_oxygen_auto.grid(row=1, column=1)

            l_auto_mode = tk.Label(controller_window, text="Auto Mode")
            l_auto_mode.config(font=("Courier", 20), fg="Pink")
            l_auto_mode.grid(row=2, column=1)

            btn_select = tk.Button(controller_window, text="Select", bd=0)
            btn_select.config(fg="black")
            btn_select.grid(row=3, column=3)

            def get_spinner_value(spinner1):
                print(spinner1.get())
                l_condition_sentence.config(
                    text="if the Oxygen level is lower than " + str(spinner1.get()) + " DO turn oxygen pump on.\n")

            btn_select.bind("<Button-1>", lambda event: get_spinner_value(spin_oxygen))

            l_spin_oxygen = tk.Label(controller_window, text="Choose oxygen concentration limit: ")
            l_spin_oxygen.config(font=("Courier", 14))
            l_spin_oxygen.grid(row=4, column=0)

            spin_oxygen = tk.Spinbox(controller_window, from_=0, to=10)
            spin_oxygen.grid(row=4, column=1)

            l_condition_sentence = tk.Label(controller_window)
            l_condition_sentence.config(
                text="if the Oxygen level is lower than " + "0" + " DO turn oxygen pump on.\n")
            l_condition_sentence.grid(row=3, column=1)

        # widgets of moisture system
        if controller == "MoistureSystem":
            l_humidifier_switch = tk.Label(controller_window, text="Humidifier Switch")
            l_humidifier_switch.config(font=("Courier", 14))
            l_humidifier_switch.grid(row=0, column=0)

            l_fans_switch = tk.Label(controller_window, text="Fans Switch")
            l_fans_switch.config(font=("Courier", 14))
            l_fans_switch.grid(row=1, column=0)

            l_moisture_auto = tk.Label(controller_window, text="Auto mode")
            l_moisture_auto.config(font=("Courier", 14))
            l_moisture_auto.grid(row=2, column=0)

            l_switch_humidifier_status = tk.Label(controller_window, text="Off")
            l_switch_humidifier_status.config(font=("Courier", 14))
            l_switch_humidifier_status.grid(row=0, column=2)

            l_switch_fans_status = tk.Label(controller_window, text="Off")
            l_switch_fans_status.config(font=("Courier", 14))
            l_switch_fans_status.grid(row=1, column=2)

            btn_humidifier_switch = tk.Button(controller_window, text="Off", bd=0,
                                              command=lambda: switch(btn_humidifier_switch.cget('text'),
                                                                     btn_humidifier_switch,
                                                                     l_switch_humidifier_status))
            btn_humidifier_switch.config(fg="grey")
            btn_humidifier_switch.grid(row=0, column=1)

            btn_fans_switch = tk.Button(controller_window, text="Off", bd=0,
                                        command=lambda: switch(btn_fans_switch.cget('text'), btn_fans_switch,
                                                               l_switch_fans_status))
            btn_fans_switch.config(fg="grey")
            btn_fans_switch.grid(row=1, column=1)

            btn_humidifier_auto = tk.Button(controller_window, text="Off", bd=0,
                                            command=lambda: switch(btn_humidifier_auto.cget('text'),
                                                                   btn_humidifier_auto,
                                                                   l_auto_status))
            btn_humidifier_auto.config(fg="grey")
            btn_humidifier_auto.grid(row=2, column=1)

            l_auto_status = tk.Label(controller_window, text="Off")
            l_auto_status.config(font=("Courier", 14))
            l_auto_status.grid(row=2, column=2)

            l_auto_mode = tk.Label(controller_window, text="Auto Mode")
            l_auto_mode.config(font=("Courier", 20), fg="Pink")
            l_auto_mode.grid(row=3, column=1)

            btn_select = tk.Button(controller_window, text="Select", bd=0)
            btn_select.config(fg="black")
            btn_select.grid(row=4, column=3)

            def get_spinner_value(spinner1, spinner2):
                print(spinner1.get())
                print(spinner2.get())
                l_condition_sentence.config(
                    text="If the room moisture is lower than " + str(
                        spinner1.get()) + " % then turn on the humidifier;;\n"
                         + "if the moisture is higher than " + str(
                        spinner2.get()) + " % then turn on the fans to high speed.")

            btn_select.bind("<Button-1>", lambda event: get_spinner_value(l_spin_mois_low, l_spin_mois_high))

            l_spin_mois_low = tk.Label(controller_window, text="Choose lower moisture boundary: ")
            l_spin_mois_low.config(font=("Courier", 14))
            l_spin_mois_low.grid(row=5, column=0)
            l_spin_mois_high = tk.Label(controller_window, text="Choose higher moisture boundary: ")
            l_spin_mois_high.config(font=("Courier", 14))
            l_spin_mois_high.grid(row=6, column=0)

            l_spin_mois_low = tk.Spinbox(controller_window, from_=0, to=10)
            l_spin_mois_low.grid(row=5, column=1)
            l_spin_mois_high = tk.Spinbox(controller_window, from_=0, to=10)
            l_spin_mois_high.grid(row=6, column=1)

            l_condition_sentence = tk.Label(controller_window)
            l_condition_sentence.config(
                text="If the room moisture is lower than " + "0" + " % then turn on the humidifier;;\n"
                     + "if the moisture is higher than " + "0" + " % then turn on the fans to high speed.")
            l_condition_sentence.grid(row=4, column=1)

        # widgets of ventilation system
        if controller == "VentilationSystem":
            l_fans_switch = tk.Label(controller_window, text="Fans Switch")
            l_fans_switch.config(font=("Courier", 14))
            l_fans_switch.grid(row=0, column=0)
            btn_fans_switch = tk.Button(controller_window, text="Off", bd=0,
                                        command=lambda: switch(btn_fans_switch.cget('text'), btn_fans_switch,
                                                               l_switch_fans_status))
            btn_fans_switch.config(fg="grey")
            btn_fans_switch.grid(row=0, column=1)

            l_switch_fans_status = tk.Label(controller_window, text="Off")
            l_switch_fans_status.config(font=("Courier", 14))
            l_switch_fans_status.grid(row=0, column=2)
            v1 = tk.DoubleVar()
            slider_fans = tk.Scale(controller_window, variable=v1,
                                   from_=1, to=100,
                                   orient=HORIZONTAL)
            slider_fans.grid(row=2)