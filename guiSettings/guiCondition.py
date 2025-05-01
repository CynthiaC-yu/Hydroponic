import tkinter as tk
from databaseOperations import dbMethods

def gui_condition(tab7):
    """
    Function to create a GUI for setting up conditions in a hydroponic system.
    """
    l_system_id = tk.Label(tab7, text="ID of the system: ")
    l_system_id.config(font=("Courier", 14))
    l_system_id.grid(row=0, column=0)

    var_system_id = tk.IntVar()
    var_system_id.set("1")
    spin_system_id = tk.Spinbox(tab7, from_=1, to=10, textvariable=var_system_id)
    spin_system_id.grid(row=0, column=1)
    global count
    count = 0

    def loadButtonListener(event):
        """
        Event listener for loading conditions based on system ID.
        """
        global count
        print("Testing Load Button Listener...")
        system_id = spin_system_id.get()
        count = dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'veryLow', 'WaterLevel')
        # Retrieving conditions from the database
        # Setting values for various condition levels
        # NOTE: The actual database retrieval and setting of values are done here
        var_water_level_very_low.set(str(count))
        var_water_level_very_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'veryLow', 'WaterLevel')))
        var_water_level_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'low', 'WaterLevel')))
        var_water_level_middle.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'medium', 'WaterLevel')))
        var_water_level_high.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'high', 'WaterLevel')))

        var_moisture_level_very_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'veryLow', 'MoistureLevel')))
        var_moisture_level_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'low', 'MoistureLevel')))
        var_moisture_level_middle.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'medium', 'MoistureLevel')))
        var_moisture_level_high.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'high', 'MoistureLevel')))

        var_oxygen_level_very_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'veryLow', 'OxygenLevel')))
        var_oxygen_level_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'low', 'OxygenLevel')))
        var_oxygen_level_middle.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'medium', 'OxygenLevel')))
        var_oxygen_level_high.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'high', 'OxygenLevel')))

        var_room_temperature_very_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'veryLow', 'RoomTemperature')))
        var_room_temperature_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'low', 'RoomTemperature')))
        var_room_temperature_middle.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'medium', 'RoomTemperature')))
        var_room_temperature_high.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'high', 'RoomTemperature')))

        var_water_temperature_very_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'veryLow', 'WaterTemperature')))
        var_water_temperature_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'low', 'WaterTemperature')))
        var_water_temperature_middle.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'medium', 'WaterTemperature')))
        var_water_temperature_high.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'high', 'WaterTemperature')))

        var_pH_level_very_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'veryLow', 'pHLevel')))
        var_pH_level_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'low', 'pHLevel')))
        var_pH_level_middle.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'medium', 'pHLevel')))
        var_pH_level_high.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'high', 'pHLevel')))

        var_nutrition_level_very_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'veryLow', 'NutritionLevel')))
        var_nutrition_level_low.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'low', 'NutritionLevel')))
        var_nutrition_level_middle.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'medium', 'NutritionLevel')))
        var_nutrition_level_high.set(str(dbMethods.get_conditions('HydroponicDB.db', 'Condition', str(system_id), 'high', 'NutritionLevel')))

    # Define labels and Spinboxes for different condition levels
    l_very_low = tk.Label(tab7, text="Very Low")
    l_very_low.config(font=("Courier", 14))
    l_very_low.grid(row=1, column=1)

    l_low = tk.Label(tab7, text="Low")
    l_low.config(font=("Courier", 14))
    l_low.grid(row=1, column=2)

    l_middle = tk.Label(tab7, text="Middle")
    l_middle.config(font=("Courier", 14))
    l_middle.grid(row=1, column=3)

    l_high = tk.Label(tab7, text="High")
    l_high.config(font=("Courier", 14))
    l_high.grid(row=1, column=4)

    l_water_level = tk.Label(tab7, text="Water Level")
    l_water_level.config(font=("Courier", 14))
    l_water_level.grid(row=2, column=0)

    btn_load = tk.Button(tab7, text="Load")
    btn_load.grid(row=0, column=2)

    btn_load.bind("<Button-1>", loadButtonListener)

    #---------------------------------------------------------------------
    #Water level entry
    var_water_level_very_low = tk.IntVar()
    Spin_water_level_very_low = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_water_level_very_low)
    Spin_water_level_very_low.grid(row=2, column=1)

    var_water_level_low = tk.IntVar()
    Spin_water_level_low = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_water_level_low)
    Spin_water_level_low.grid(row=2, column=2)

    var_water_level_middle = tk.IntVar()
    Spin_water_level_middle = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_water_level_middle)
    Spin_water_level_middle.grid(row=2, column=3)

    var_water_level_high = tk.IntVar()
    Spin_water_level_high = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_water_level_high)
    Spin_water_level_high.grid(row=2, column=4)

    btn_water_level = tk.Button(tab7, text="Enter")
    btn_water_level.grid(row=2, column=6)

    def btn_water_level_enter_listener(event):
        print("testing btn_water_level_enter_listener....")
        pot_id = spin_system_id.get()
        very_low = Spin_water_level_very_low.get()
        low = Spin_water_level_low.get()
        medium = Spin_water_level_middle.get()
        high = Spin_water_level_high.get()
        tag = "WaterLevel"
        values = (very_low, low, medium, high, tag)
        print(values)
        dbMethods.set_conditions('HydroponicDB.db', 'condition', pot_id, values)

    btn_water_level.bind("<Button-1>", btn_water_level_enter_listener)

    #---------------------------------------------------------------------
    #Moisture level entry
    l_moisture_level = tk.Label(tab7, text="Moisture Level")
    l_moisture_level.config(font=("Courier", 14))
    l_moisture_level.grid(row=3, column=0)

    var_moisture_level_very_low = tk.IntVar()
    Spin_moisture_level_very_low = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_moisture_level_very_low)
    Spin_moisture_level_very_low.grid(row=3, column=1)

    var_moisture_level_low = tk.IntVar()
    Spin_moisture_level_low = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_moisture_level_low)
    Spin_moisture_level_low.grid(row=3, column=2)

    var_moisture_level_middle = tk.IntVar()
    Spin_moisture_level_middle = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_moisture_level_middle)
    Spin_moisture_level_middle.grid(row=3, column=3)

    var_moisture_level_high = tk.IntVar()
    Spin_moisture_level_high = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_moisture_level_high)
    Spin_moisture_level_high.grid(row=3, column=4)

    btn_moisture_level = tk.Button(tab7, text="Enter")
    btn_moisture_level.grid(row=3, column=6)

    def btn_moisture_level_enter_listener(event):
        print("testing btn_moisture_level_enter_listener....")
        pot_id = spin_system_id.get()
        very_low = Spin_moisture_level_very_low.get()
        low = Spin_moisture_level_low.get()
        medium = Spin_moisture_level_middle.get()
        high = Spin_moisture_level_high.get()
        tag = "MoistureLevel"
        values = (very_low, low, medium, high, tag)
        print(values)
        dbMethods.set_conditions('HydroponicDB.db', 'condition', pot_id, values)

    btn_moisture_level.bind("<Button-1>", btn_moisture_level_enter_listener)

    #---------------------------------------------------------------------
    #Oxygen level entry
    l_oxygen_level = tk.Label(tab7, text="Oxygen Level")
    l_oxygen_level.config(font=("Courier", 14))
    l_oxygen_level.grid(row=4, column=0)

    var_oxygen_level_very_low = tk.IntVar()
    Spin_oxygen_level_very_low = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_oxygen_level_very_low)
    Spin_oxygen_level_very_low.grid(row=4, column=1)

    var_oxygen_level_low = tk.IntVar()
    Spin_oxygen_level_low = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_oxygen_level_low)
    Spin_oxygen_level_low.grid(row=4, column=2)

    var_oxygen_level_middle = tk.IntVar()
    Spin_oxygen_level_middle = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_oxygen_level_middle)
    Spin_oxygen_level_middle.grid(row=4, column=3)

    var_oxygen_level_high = tk.IntVar()
    Spin_oxygen_level_high = tk.Spinbox(tab7, from_=0, to=100, textvariable=var_oxygen_level_high)
    Spin_oxygen_level_high.grid(row=4, column=4)

    btn_oxygen_level = tk.Button(tab7, text="Enter")
    btn_oxygen_level.grid(row=4, column=6)

    def btn_oxygen_level_enter_listener(event):
        print("testing btn_oxygen_level_enter_listener....")
        pot_id = spin_system_id.get()
        very_low = Spin_oxygen_level_very_low.get()
        low = Spin_oxygen_level_low.get()
        medium = Spin_oxygen_level_middle.get()
        high = Spin_oxygen_level_high.get()
        tag = "OxygenLevel"
        values = (very_low, low, medium, high, tag)
        print(values)
        dbMethods.set_conditions('HydroponicDB.db', 'condition', pot_id, values)

    btn_oxygen_level.bind("<Button-1>", btn_oxygen_level_enter_listener)

    #---------------------------------------------------------------------
    #Room temperature entry
    l_room_temperature = tk.Label(tab7, text="Room Temperature")
    l_room_temperature.config(font=("Courier", 14))
    l_room_temperature.grid(row=5, column=0)

    var_room_temperature_very_low = tk.IntVar()
    Spin_room_temperature_very_low = tk.Spinbox(tab7, from_=0, to=50, textvariable=var_room_temperature_very_low)
    Spin_room_temperature_very_low.grid(row=5, column=1)

    var_room_temperature_low = tk.IntVar()
    Spin_room_temperature_low = tk.Spinbox(tab7, from_=0, to=50, textvariable=var_room_temperature_low)
    Spin_room_temperature_low.grid(row=5, column=2)

    var_room_temperature_middle = tk.IntVar()
    Spin_room_temperature_middle = tk.Spinbox(tab7, from_=0, to=50, textvariable=var_room_temperature_middle)
    Spin_room_temperature_middle.grid(row=5, column=3)

    var_room_temperature_high = tk.IntVar()
    Spin_room_temperature_high = tk.Spinbox(tab7, from_=0, to=50, textvariable=var_room_temperature_high)
    Spin_room_temperature_high.grid(row=5, column=4)

    btn_room_temperature = tk.Button(tab7, text="Enter")
    btn_room_temperature.grid(row=5, column=6)

    def btn_room_temperature_enter_listener(event):
        print("testing room_temperature_enter_listener....")
        pot_id = spin_system_id.get()
        very_low = Spin_room_temperature_very_low.get()
        low = Spin_room_temperature_low.get()
        medium = Spin_room_temperature_middle.get()
        high = Spin_room_temperature_high.get()
        tag = "RoomTemperature"
        values = (very_low, low, medium, high, tag)
        print(values)
        dbMethods.set_conditions('HydroponicDB.db', 'condition', pot_id, values)

    btn_room_temperature.bind("<Button-1>", btn_room_temperature_enter_listener)

    #---------------------------------------------------------------------
    #Water temperature entry
    l_water_temperature = tk.Label(tab7, text="Water Temperature")
    l_water_temperature.config(font=("Courier", 14))
    l_water_temperature.grid(row=6, column=0)

    var_water_temperature_very_low = tk.IntVar()
    Spin_water_temperature_very_low = tk.Spinbox(tab7, from_=0, to=50, textvariable=var_water_temperature_very_low)
    Spin_water_temperature_very_low.grid(row=6, column=1)

    var_water_temperature_low = tk.IntVar()
    Spin_water_temperature_low = tk.Spinbox(tab7, from_=0, to=50, textvariable=var_water_temperature_low)
    Spin_water_temperature_low.grid(row=6, column=2)

    var_water_temperature_middle = tk.IntVar()
    Spin_water_temperature_middle = tk.Spinbox(tab7, from_=0, to=50, textvariable=var_water_temperature_middle)
    Spin_water_temperature_middle.grid(row=6, column=3)

    var_water_temperature_high = tk.IntVar()
    Spin_water_temperature_high = tk.Spinbox(tab7, from_=0, to=50, textvariable=var_water_temperature_high)
    Spin_water_temperature_high.grid(row=6, column=4)

    btn_water_temperature = tk.Button(tab7, text="Enter")
    btn_water_temperature.grid(row=6, column=6)

    def btn_water_temperature_enter_listener(event):
        print("testing water_temperature_enter_listener....")
        pot_id = spin_system_id.get()
        very_low = Spin_water_temperature_very_low.get()
        low = Spin_water_temperature_low.get()
        medium = Spin_water_temperature_middle.get()
        high = Spin_water_temperature_high.get()
        tag = "WaterTemperature"
        values = (very_low, low, medium, high, tag)
        print(values)
        dbMethods.set_conditions('HydroponicDB.db', 'condition', pot_id, values)

    btn_water_temperature.bind("<Button-1>", btn_water_temperature_enter_listener)

    #---------------------------------------------------------------------
    #pH level entry
    l_pH_level = tk.Label(tab7, text="pH Level")
    l_pH_level.config(font=("Courier", 14))
    l_pH_level.grid(row=7, column=0)

    var_pH_level_very_low = tk.IntVar()
    Spin_pH_level_very_low = tk.Spinbox(tab7, from_=0, to=14, textvariable=var_pH_level_very_low)
    Spin_pH_level_very_low.grid(row=7, column=1)

    var_pH_level_low = tk.IntVar()
    Spin_pH_level_low = tk.Spinbox(tab7, from_=0, to=14, textvariable=var_pH_level_low)
    Spin_pH_level_low.grid(row=7, column=2)

    var_pH_level_middle = tk.IntVar()
    Spin_pH_level_middle = tk.Spinbox(tab7, from_=0, to=14, textvariable=var_pH_level_middle)
    Spin_pH_level_middle.grid(row=7, column=3)

    var_pH_level_high = tk.IntVar()
    Spin_pH_level_high = tk.Spinbox(tab7, from_=0, to=14, textvariable=var_pH_level_high)
    Spin_pH_level_high.grid(row=7, column=4)

    btn_pH_level = tk.Button(tab7, text="Enter")
    btn_pH_level.grid(row=7, column=6)

    def btn_pH_level_enter_listener(event):
        print("testing PH level _enter_listener....")
        pot_id = spin_system_id.get()
        very_low = Spin_pH_level_very_low.get()
        low = Spin_pH_level_low.get()
        medium = Spin_pH_level_middle.get()
        high = Spin_pH_level_high.get()
        tag = "pHLevel"
        values = (very_low, low, medium, high, tag)
        print(values)
        dbMethods.set_conditions('HydroponicDB.db', 'condition', pot_id, values)

    btn_pH_level.bind("<Button-1>", btn_pH_level_enter_listener)

    #---------------------------------------------------------------------
    #Nutrition level entry
    l_nutrition_Level = tk.Label(tab7, text="Nutrition Level")
    l_nutrition_Level.config(font=("Courier", 14))
    l_nutrition_Level.grid(row=8, column=0)

    var_nutrition_level_very_low = tk.IntVar()
    Spin_nutrition_Level_very_low = tk.Spinbox(tab7, from_=0, to=3500, textvariable=var_nutrition_level_very_low)
    Spin_nutrition_Level_very_low.grid(row=8, column=1)

    var_nutrition_level_low = tk.IntVar()
    Spin_nutrition_Level_low = tk.Spinbox(tab7, from_=0, to=3500, textvariable=var_nutrition_level_low)
    Spin_nutrition_Level_low.grid(row=8, column=2)

    var_nutrition_level_middle = tk.IntVar()
    Spin_nutrition_Level_middle = tk.Spinbox(tab7, from_=0, to=3500, textvariable=var_nutrition_level_middle)
    Spin_nutrition_Level_middle.grid(row=8, column=3)

    var_nutrition_level_high = tk.IntVar()
    Spin_nutrition_Level_high = tk.Spinbox(tab7, from_=0, to=3500, textvariable=var_nutrition_level_high)
    Spin_nutrition_Level_high.grid(row=8, column=4)

    btn_nutrition_Level = tk.Button(tab7, text="Enter")
    btn_nutrition_Level.grid(row=8, column=6)

    def btn_nutrition_level_enter_listener(event):
        print("testing nutrition level _enter_listener....")
        pot_id = spin_system_id.get()
        very_low = Spin_nutrition_Level_very_low.get()
        low = Spin_nutrition_Level_low.get()
        medium = Spin_nutrition_Level_middle.get()
        high = Spin_nutrition_Level_high.get()
        tag = "NutritionLevel"
        values = (very_low, low, medium, high, tag)
        print(values)
        dbMethods.set_conditions('HydroponicDB.db', 'condition', pot_id, values)

    btn_nutrition_Level.bind("<Button-1>", btn_nutrition_level_enter_listener)