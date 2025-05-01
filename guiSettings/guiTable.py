from Table import create_gui_table
from __init__ import *

def gui_table(tab4):
    """""
    This function creates a GUI for displaying tables of different parameters. 
    """""
    label = tk.Label(tab4, text='Select the table you want to check: ', anchor=tk.NW)
    label.pack()

    # Button widgets for different tables
    btn_water_level = tk.Button(tab4, text="Water Level", command=lambda: create_gui_table(tab4, 'WaterLevel'))
    btn_water_level.pack()
    btn_ph_level = tk.Button(tab4, text="pH Level", command=lambda: create_gui_table(tab4,'pHLevel'))
    btn_ph_level.pack()
    btn_room_temperature = tk.Button(tab4, text="Room Temperature", command=lambda: create_gui_table(tab4,'RoomTemperature'))
    btn_room_temperature.pack()
    btn_nutrition_level = tk.Button(tab4, text="Nutrition Level", command=lambda: create_gui_table(tab4,'NutritionLevel'))
    btn_nutrition_level.pack()
    btn_water_temperature = tk.Button(tab4, text="Water Temperature", command=lambda: create_gui_table(tab4,'WaterTemperature'))
    btn_water_temperature.pack()
    btn_moisture_level = tk.Button(tab4, text="Moisture Level", command=lambda: create_gui_table(tab4,'MoistureLevel'))
    btn_moisture_level.pack()
    btn_oxygen_level = tk.Button(tab4, text="Oxygen Level", command=lambda: create_gui_table(tab4,'OxygenLevel'))
    btn_oxygen_level.pack()