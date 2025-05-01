import tkinter as tk
from tkinter import ttk
from tkinter import RIGHT
from databaseOperations import dbMethods

# Global variable to store alarm text
alarmText = ""

# Function to determine the status based on current value and thresholds
def currentStatus(current, veryLow, low, middle, high, type):
    global alarmText
    if current > high:
        result = "very high"
        if type in {"MoistureLevel", "pHLevel", "RoomTemperature", "WaterTemperature", "NutritionLevel"}:
            alarmText = alarmText + type + " is too high, you need to check it right now!\n"
    if current <= high:
        result = "high"
    if current <= middle:
        result = "medium"
    if current <= low:
        result = "low"
    if current <= veryLow:
        result = "very low"
        if type in {"MoistureLevel", "WaterLevel", "pHLevel", "RoomTemperature", "WaterTemperature", "NutritionLevel",
                    "OxygenLevel"}:
            alarmText = alarmText + type + " is too low! Check it right now!\n"
    # print("test alarm text: " + alarmText)
    return result

def update_result_text(window,result_text):
    rows = dbMethods.query_data('HydroponicDB.db', 'pot')
    result_text.delete(1.0, tk.END)
    for row in rows:
        result_text.insert(tk.END, f"PotID: {row[0]}, Date: {row[1]}, pHlevel: {row[2]}\n")
    window.after(1800000, update_result_text)

def set_latest_data_into_report(system_id, columns):
    list_value = [i[0] for i in dbMethods.get_lastest_column('HydroponicDB.db', 'pot', system_id, columns)]

    if list_value:  # Check if list_value is not empty
        value = list_value[0]
    else:
        value = 0  # or any other default value you prefer

    return value

def gui_report(tab1):
    # Create the upper canvas
    upper_canvas = tk.Canvas(tab1)
    upper_canvas.grid(row=0, column=0)
    l_system_id = tk.Label(upper_canvas, text="ID of the system: ")
    l_system_id.config(font=("Courier", 14))
    l_system_id.grid(row=0, column=0)
    spin_system_id = tk.Spinbox(upper_canvas, from_=1, to=10, textvariable=1)
    spin_system_id.grid(row=0, column=1)
    btn_load = tk.Button(upper_canvas, text="Load/update")
    btn_load.grid(row=0, column=2)

    seperator_canvas_1 = tk.Canvas(tab1)
    seperator_canvas_1.grid(row=1, column=0)
    # Seperator 1
    l_seperator_1 = tk.Label(seperator_canvas_1, text="*-*-*-*-*-*-*-*-*-*")
    l_seperator_1.config(font=("Courier", 14))
    l_seperator_1.grid(row=0, column=0)
    # Create the middle canvas
    middle_canvas = tk.Canvas(tab1)
    middle_canvas.grid(row=2, column=0)
    seperator_canvas_2 = tk.Canvas(tab1)
    seperator_canvas_2.grid(row=3, column=0)
    # Seperator 2
    l_seperator_2 = tk.Label(seperator_canvas_2, text="*-*-*-*-*-*-*-*-*-*")
    l_seperator_2.config(font=("Courier", 14))
    l_seperator_2.grid(row=0, column=0)
    # Create the regular canvas
    regular_canvas = tk.Canvas(tab1)
    regular_canvas.grid(row=4, column=0)

    # Set the default pot_id to 1
    default_pot_id = 1

    # Load the default pot_id data
    load_data(tab1, upper_canvas, middle_canvas, regular_canvas, default_pot_id)

    def loadButtonListener(event):
        print("Testing Load Button Listener...")
        system_id = spin_system_id.get()
        load_data(tab1, upper_canvas, middle_canvas, regular_canvas, system_id)

    btn_load.bind("<Button-1>", loadButtonListener)

def load_data(tab1, upper_canvas, middle_canvas, regular_canvas, system_id):
    # # Hide the load button
    # Create label and text widget for alarms
    l_alarm = tk.Label(upper_canvas, text="Alarms!")
    l_alarm.config(font=("Courier", 14))
    l_alarm.grid(row=1, column=0)
    t_alarm = tk.Text(upper_canvas, height=5, width=52)
    alarm_text = alarmText
    t_alarm.insert(tk.END, alarm_text)
    t_alarm.grid(row=1, column=1)

    # Load data for middle and regular canvases
    load_middle_data(middle_canvas, system_id)
    load_regular_data(regular_canvas, system_id)

def load_middle_data(middle_canvas, system_id):
    # Create labels and text widgets for middle canvas
    l_species_of_the_plant = tk.Label(middle_canvas, text="Species of the plant: ", anchor="e", justify=RIGHT)
    l_species_of_the_plant.config(font=("Courier", 14))
    l_species_of_the_plant.grid(row=0, column=0)
    t_species_of_the_plant = tk.Text(middle_canvas, height=1, width=10)
    species_of_the_plant_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', system_id, 'species')
    t_species_of_the_plant.insert(tk.END, species_of_the_plant_text)
    t_species_of_the_plant.grid(row=0, column=1)

    l_variant = tk.Label(middle_canvas, text="Variant of the plant: ", anchor="e", justify=RIGHT)
    l_variant.config(font=("Courier", 14))
    l_variant.grid(row=1, column=0)

    t_variant = tk.Text(middle_canvas, height=1, width=10)
    variant_plant_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', system_id, 'variant')
    t_variant.insert(tk.END, variant_plant_text)
    t_variant.grid(row=1, column=1)

    l_age_of_the_plant = tk.Label(middle_canvas, text="Initial age of the plant: ", anchor="e", justify=RIGHT)
    l_age_of_the_plant.config(font=("Courier", 14))
    l_age_of_the_plant.grid(row=2, column=0)

    t_age_of_the_plant = tk.Text(middle_canvas, height=1, width=10)
    age_of_the_plant_text = str(dbMethods.get_plant('HydroponicDB.db', 'Plant', system_id, 'age')) + " days"
    # Insert The text.
    t_age_of_the_plant.insert(tk.END, age_of_the_plant_text)
    t_age_of_the_plant.grid(row=2, column=1)

    l_init_quantity = tk.Label(middle_canvas, text="Initial Quantity: ", anchor="e", justify=RIGHT)
    l_init_quantity.config(font=("Courier", 14))
    l_init_quantity.grid(row=3, column=0)

    t_init_quantity = tk.Text(middle_canvas, height=1, width=10)
    init_quantity_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', system_id, 'initialQuantity')
    # Insert The text.
    t_init_quantity.insert(tk.END, init_quantity_text)
    t_init_quantity.grid(row=3, column=1)

    l_quantity = tk.Label(middle_canvas, text="Quantity: ", anchor="e", justify=RIGHT)
    l_quantity.config(font=("Courier", 14))
    l_quantity.grid(row=4, column=0)

    t_quantity = tk.Text(middle_canvas, height=1, width=10)
    quantity_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', system_id, 'quantity')
    # Insert The text.
    t_quantity.insert(tk.END, quantity_text)
    t_quantity.grid(row=4, column=1)

    l_growing_stage = tk.Label(middle_canvas, text="Growing stage: ", anchor="e", justify=RIGHT)
    l_growing_stage.config(font=("Courier", 14))
    l_growing_stage.grid(row=5, column=0)

    t_growing_stage = tk.Text(middle_canvas, height=1, width=10)
    growing_stage_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', system_id, 'growingStage')
    # Insert The text.
    t_growing_stage.insert(tk.END, growing_stage_text)
    t_growing_stage.grid(row=5, column=1)

def load_regular_data(regular_canvas, system_id):
    l_water_level = tk.Label(regular_canvas, text="Water level: ")
    l_water_level.config(font=("Courier", 14))
    l_water_level.grid(row=6, column=0)
    t_water_level = tk.Text(regular_canvas, height=1, width=10)
    water_level_text = currentStatus(set_latest_data_into_report(system_id, 'WaterLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'veryLow', 'WaterLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'low', 'WaterLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'medium', 'WaterLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'high', 'WaterLevel'),
                                     "WaterLevel")
    t_water_level.insert(tk.END, water_level_text)
    t_water_level.grid(row=6, column=1)

    # Update with actual data using set_latest_data_into_report
    l_value_water_level = ttk.Label(regular_canvas, text=str(set_latest_data_into_report(system_id, 'WaterLevel')) + "%")
    l_value_water_level.grid(row=6, column=3)
    p_water_level = ttk.Progressbar(regular_canvas, orient=tk.HORIZONTAL,
                                    length=100, value=set_latest_data_into_report(system_id, 'WaterLevel'))
    p_water_level.grid(row=6, column=2)

    l_moisture_level = tk.Label(regular_canvas, text="Moisture level: ")
    l_moisture_level.config(font=("Courier", 14))
    l_moisture_level.grid(row=7, column=0)

    t_moisture_level = tk.Text(regular_canvas, height=1, width=10)
    moisture_level_text = currentStatus(set_latest_data_into_report(system_id, 'MoistureLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'veryLow', 'MoistureLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'low', 'MoistureLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'medium', 'MoistureLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'high', 'MoistureLevel'),
                                        "MoistureLevel")
    # Insert The text.
    t_moisture_level.insert(tk.END, moisture_level_text)
    t_moisture_level.grid(row=7, column=1)

    l_moisture_level = ttk.Label(regular_canvas,
                                 text=str(set_latest_data_into_report(system_id, 'MoistureLevel')) + "%")
    l_moisture_level.grid(row=7, column=3)

    p_moisture_level = ttk.Progressbar(regular_canvas, orient=tk.HORIZONTAL,
                                       length=100, value=set_latest_data_into_report(system_id, 'MoistureLevel'))
    p_moisture_level.grid(row=7, column=2)

    l_oxygen_level = tk.Label(regular_canvas, text="Oxygen level: ")
    l_oxygen_level.config(font=("Courier", 14))
    l_oxygen_level.grid(row=8, column=0)

    t_oxygen_level = tk.Text(regular_canvas, height=1, width=10)
    oxygen_level_text = currentStatus(set_latest_data_into_report(system_id, 'OxygenLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'veryLow', 'OxygenLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'low', 'OxygenLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'medium', 'OxygenLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'high', 'OxygenLevel'),
                                      "OxygenLevel")

    # Insert The text.
    t_oxygen_level.insert(tk.END, oxygen_level_text)
    t_oxygen_level.grid(row=8, column=1)
    v_oxygen_level = tk.DoubleVar()
    s_oxygen_level = tk.Scale(regular_canvas, variable=v_oxygen_level,
                              from_=1, to=100,
                              orient=tk.HORIZONTAL)
    s_oxygen_level.set(set_latest_data_into_report(system_id, 'OxygenLevel'))
    s_oxygen_level.grid(row=8, column=2)

    # roomTemperature
    l_room_temperature = tk.Label(regular_canvas, text="Room Temperature: ")
    l_room_temperature.config(font=("Courier", 14))
    l_room_temperature.grid(row=9, column=0)

    t_room_temperature = tk.Text(regular_canvas, height=1, width=10)
    room_temperature_text = currentStatus(set_latest_data_into_report(system_id, 'RoomTemperature'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'veryLow', 'RoomTemperature'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'low', 'RoomTemperature'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'medium', 'RoomTemperature'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'high', 'RoomTemperature'),
                                          "RoomTemperature")


    # Insert The text.
    t_room_temperature.insert(tk.END, room_temperature_text)
    t_room_temperature.grid(row=9, column=1)
    v_room_temperature = tk.DoubleVar()
    s_room_temperature = tk.Scale(regular_canvas, variable=v_room_temperature,
                                  from_=1, to=45,
                                  orient=tk.HORIZONTAL)
    s_room_temperature.set(set_latest_data_into_report(system_id, 'RoomTemperature'))
    s_room_temperature.grid(row=9, column=2)

    # Water Temperature
    l_water_temperature = tk.Label(regular_canvas, text="Water Temperature: ")
    l_water_temperature.config(font=("Courier", 14))
    l_water_temperature.grid(row=10, column=0)

    t_water_temperature = tk.Text(regular_canvas, height=1, width=10)
    water_temperature_text = currentStatus(set_latest_data_into_report(system_id, 'WaterTemperature'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'veryLow', 'WaterTemperature'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'low', 'WaterTemperature'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'medium', 'WaterTemperature'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'high', 'WaterTemperature'),
                                           "WaterTemperature")

    # Insert The text.
    t_water_temperature.insert(tk.END, water_temperature_text)
    t_water_temperature.grid(row=10, column=1)
    v_water_temperature = tk.DoubleVar()
    s_water_temperature = tk.Scale(regular_canvas, variable=v_water_temperature,
                                   from_=1, to=45,
                                   orient=tk.HORIZONTAL)
    s_water_temperature.set(set_latest_data_into_report(system_id, 'WaterTemperature'))
    s_water_temperature.grid(row=10, column=2)

    # pH Level
    l_pH_level = tk.Label(regular_canvas, text="pH Level: ")
    l_pH_level.config(font=("Courier", 14))
    l_pH_level.grid(row=11, column=0)

    t_pH_level = tk.Text(regular_canvas, height=1, width=10)
    pH_level_text = currentStatus(set_latest_data_into_report(system_id, 'pHLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'veryLow', 'pHLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'low', 'pHLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'medium', 'pHLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'high', 'pHLevel'),
                                  "pHLevel")

    # Insert The text.
    t_pH_level.insert(tk.END, pH_level_text)
    t_pH_level.grid(row=11, column=1)
    v_pH_level = tk.DoubleVar()
    s_pH_level = tk.Scale(regular_canvas, variable=v_pH_level,
                          from_=1, to=14,
                          orient=tk.HORIZONTAL)
    s_pH_level.set(set_latest_data_into_report(system_id, 'pHLevel'))
    s_pH_level.grid(row=11, column=2)

    # Nutrition Level
    l_nutrition_level = tk.Label(regular_canvas, text="Nutrition Level: ")
    l_nutrition_level.config(font=("Courier", 14))
    l_nutrition_level.grid(row=12, column=0)

    t_nutrition_level = tk.Text(regular_canvas, height=1, width=10)
    nutrition_level_text = currentStatus(set_latest_data_into_report(system_id, 'NutritionLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'veryLow', 'NutritionLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'low', 'NutritionLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'medium', 'NutritionLevel'),
                                            dbMethods.get_conditions('HydroponicDB.db', 'Condition', system_id, 'high', 'NutritionLevel'),
                                         "NutritionLevel")

    # Insert The text.
    t_nutrition_level.insert(tk.END, nutrition_level_text)
    t_nutrition_level.grid(row=12, column=1)
    v_nutrition_level = tk.DoubleVar()
    s_nutrition_level = tk.Scale(regular_canvas, variable=v_nutrition_level,
                                 from_=1, to=4000,
                                 orient=tk.HORIZONTAL)
    s_nutrition_level.set(set_latest_data_into_report(system_id, 'NutritionLevel'))
    s_nutrition_level.grid(row=12, column=2)