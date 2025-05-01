from datetime import datetime, timedelta
import random
from databaseOperations import dbMethods


def generateMockData(number_of_pots, number_of_data_for_each_factor):
    print("Inserting mock data session...")
    for i in range(1, number_of_pots + 1):
        value = 0
        print(f"Inserting factors for pot {i}  out of total {number_of_pots} pots...")
        for j in range(number_of_data_for_each_factor):
            current_time = datetime.now()
            print(current_time)
            value -= 30
            minutes = timedelta(minutes=value)
            new_time = current_time - minutes

            # formatting the time
            formatted_time = new_time.strftime("%Y-%m-%d-%H:%M")

            # Generating a random number
            print("Factors insertion process (1/7): Inserting water level...")
            water_level = round(random.uniform(0, 100), 1)
            print("Factors insertion process (2/7) Inserting room temperature...")
            room_temperature = round(random.uniform(0, 50), 1)
            print("Factors insertion process (3/7) Inserting water temperature...")
            water_temperature = round(random.uniform(0, 50), 1)
            print("Factors insertion process (4/7) Inserting oxygen level...")
            oxygen_level = round(random.uniform(0, 20), 1)
            print("Factors insertion process (5/7) Inserting pH level...")
            pH_level = round(random.uniform(1, 14), 1)
            print("Factors insertion process (6/7) Inserting nutrition level...")
            nutrition_level = round(random.uniform(0, 4000), 1)
            print("Factors insertion process (7/7) Inserting moisture level...")
            moisture_level = round(random.uniform(0, 100), 1)

            values = (i, formatted_time, water_level, room_temperature, water_temperature, oxygen_level, pH_level,
                      nutrition_level, moisture_level)

            dbMethods.insert_factors('HydroponicDB.db', 'pot', 'Potid', 'Date', 'WaterLevel', 'RoomTemperature',
                                  'WaterTemperature',
                                  'OxygenLevel', 'pHLevel', 'NutritionLevel', 'MoistureLevel', values)

            valueNameList = ["Pot ID: ", "Insertion Time: ", "Water Level: ", "Room Temperature: ",
                             "Water Temperature: "
                , "Oxygen Level: ", "pH Level: ", "Nutrition Level: ", "Moisture Level: "]
            print("New factors inserted: ")
            for k in range(9):
                print(str(valueNameList[k]) + str(values[k]))
            print("-----" * 10)

    print("\n" + "***** new session *****" * 10 + "\n")

    # sample super admin
    print("Inserting New user session...")
    dbMethods.insert_new_user('s', 's', '1')

    # sample admin
    dbMethods.insert_new_user('admin2', '666666', '2')

    # Sample Admin
    dbMethods.insert_new_user('admin3', '777777', '2')

    print("\n" + "***** new session *****" * 10 + "\n")

    # Insert New Conditions
    for i in range (1, number_of_pots+1):
        value1 = (i, 10, 30, 50, 70, 'WaterLevel')
        value2 = (i, 20, 25, 30, 35, 'RoomTemperature')
        value3 = (i, 18, 22, 27, 33, 'WaterTemperature')
        value4 = (i, 5, 10, 15, 18, 'OxygenLevel')
        value5 = (i, 5, 7, 8, 9, 'pHLevel')
        value6 = (i, 1700, 2000, 2500, 3000, 'NutritionLevel')
        value7 = (i, 20, 38, 40, 50, 'MoistureLevel')

        dbMethods.insert_conditions('HydroponicDB.db', 'condition', 'Potid', 'veryLow', 'low', 'medium', 'high', 'tag',
                                    value1)
        dbMethods.insert_conditions('HydroponicDB.db', 'condition', 'Potid', 'veryLow', 'low', 'medium', 'high', 'tag',
                                    value2)
        dbMethods.insert_conditions('HydroponicDB.db', 'condition', 'Potid', 'veryLow', 'low', 'medium', 'high', 'tag',
                                    value3)
        dbMethods.insert_conditions('HydroponicDB.db', 'condition', 'Potid', 'veryLow', 'low', 'medium', 'high', 'tag',
                                    value4)
        dbMethods.insert_conditions('HydroponicDB.db', 'condition', 'Potid', 'veryLow', 'low', 'medium', 'high', 'tag',
                                    value5)
        dbMethods.insert_conditions('HydroponicDB.db', 'condition', 'Potid', 'veryLow', 'low', 'medium', 'high', 'tag',
                                    value6)
        dbMethods.insert_conditions('HydroponicDB.db', 'condition', 'Potid', 'veryLow', 'low', 'medium', 'high', 'tag',
                                    value7)
        print("Testing inserting conditions...")
        print(value1)
        print(value2)
        print(value3)
        print(value4)
        print(value5)
        print(value6)
        print(value7)
        print("\n" + "***** new session *****" * 10 + "\n")

    print("Testing inserting plants...")
    value1_plant = (1, 'Lettuce', 'Iceberg', '10', '39', '37', 'Stage I')
    print("Plant i: " + str(value1_plant))
    value2_plant = (2, 'Carrot', 'BabyCarrot', '5', '8', '8', 'Stage III')
    print("Plant 2: " + str(value2_plant))

    dbMethods.insert_plant('HydroponicDB.db', 'Plant', 'Potid', 'species', 'variant', 'age', 'initialQuantity',
                           'quantity', 'growingStage', value1_plant)
    dbMethods.insert_plant('HydroponicDB.db', 'Plant', 'Potid', 'species', 'variant', 'age', 'initialQuantity',
                           'quantity', 'growingStage', value2_plant)

    for i in range (3, number_of_pots+1):
        value2_plant = (i, 'Carrot', 'BabyCarrot', '5', '8', '8', 'Stage III')
        print(f"Plant {i}: " + str(value2_plant))
        dbMethods.insert_plant('HydroponicDB.db', 'Plant', 'Potid', 'species', 'variant', 'age', 'initialQuantity',
                               'quantity', 'growingStage', value2_plant)


