import time
from datetime import datetime
import random
import threading
from tkinter import ttk
from databaseOperations import dbMethods
from guiSettings import guiReport

'''
Custom thread class for generating new mock factors data at regular intervals, thus enabling the program to simulate
retrieving result from the Arduino sensors. 
'''

def task():
    """
    Task function for updating GUI components with the latest data.
    """
    l_value_water_level = ttk.Label(guiReport.regular_canvas, text=str(dbMethods.set_latest_data_into_report('WaterLevel')) + "%")
    l_value_water_level.grid(row=6, column=3)
    p_water_level = ttk.Progressbar(guiReport.regular_canvas, orient=tk.HORIZONTAL,
                                    length=100, value=dbMethods.set_latest_data_into_report('WaterLevel'))
    p_water_level.grid(row=6, column=2)

class Recorder(threading.Thread):
    """
    Custom thread class for recording data at regular intervals.
    """
    def record(self):
        """
        Method for recording data and inserting it into the database.
        """
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d-%H:%M")

        for i in range(1, 11):
            print("Testing the i index value: " + str(i))
            # Generate random data
            water_level = round(random.uniform(0, 100), 1)
            room_temperature = round(random.uniform(0, 50), 1)
            water_temperature = round(random.uniform(0, 50), 1)
            oxygen_level = round(random.uniform(0, 20), 1)
            pH_level = round(random.uniform(1, 14), 1)
            nutrition_level = round(random.uniform(0, 4000), 1)
            moisture_level = round(random.uniform(0, 100), 1)
            values = (i, formatted_time, water_level, room_temperature, water_temperature, oxygen_level, pH_level,
                      nutrition_level, moisture_level)

            # Insert data into the database
            dbMethods.insert_factors('HydroponicDB.db', 'pot', 'Potid', 'Date', 'WaterLevel', 'RoomTemperature',
                                     'WaterTemperature',
                                     'OxygenLevel', 'pHLevel', 'NutritionLevel', 'MoistureLevel', values)
            print("Testing the inserting value to factors: " + str(values))

    def run(self):
        """
        Method to run the recording thread.
        """
        while True:
            current_minute = datetime.now().minute
            if current_minute % 5 == 0:  # Record data every 5 minutes
                print("New data received:", datetime.now())
                self.record()
            time.sleep(60)  # Pause for 60 seconds before checking again