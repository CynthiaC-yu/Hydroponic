# This file is used to initialize the database and create tables inside it.
from databaseOperations import dbMethods


def create_dbTables():
    # Create database
    dbMethods.create_database('HydroponicDB.db')

    # Define table names and column structures
    pot = 'Pot'
    potColumns = '''
        (
         Potid INTEGER,
         Date text NOT NULL,
         WaterLevel REAL,
         RoomTemperature REAL,
         WaterTemperature REAL,
         OxygenLevel REAL,
         pHLevel REAL,
         NutritionLevel REAL,
         MoistureLevel REAL
         )
    '''

    plant = 'Plant'
    plantColumns = '''
        (Potid INTEGER, 
         species text,
         variant text,
         age INTEGER, 
         initialQuantity INTEGER, 
         quantity INTEGER,
         growingStage text
         )
    '''

    condition = 'Condition'
    conditionColumns = '''
        (Potid INTEGER,
         veryLow REAL,
         low REAL,
         medium REAL, 
         high REAL, 
         tag text
         )
    '''

    user = 'user'
    userColumns = '''
    (
        userid INTEGER PRIMARY KEY,
        userName text not null,
        pwd      text not null,
        level    text not null

    )
    '''

    # Create tables
    dbMethods.create_table('HydroponicDB.db', pot, potColumns)
    dbMethods.create_table('HydroponicDB.db', plant, plantColumns)
    print("Plant table is created")
    dbMethods.create_table('HydroponicDB.db', condition, conditionColumns)
    dbMethods.create_table('HydroponicDB.db', user, userColumns)