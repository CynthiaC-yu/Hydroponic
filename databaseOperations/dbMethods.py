import sqlite3


'''
this library defines all the database operations may be used in the hydroponic system
'''
# --------------------------------------------------------------
def create_database(database_name):
    conn = sqlite3.connect(database_name)
    conn.close()
def create_table(database_name, table_name, columns):
    """
    Creates a new table in the specified database.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # Construct a SQLite sentence to create the table
    sql = f"CREATE TABLE IF NOT EXISTS {table_name} {columns}"
    print("Generated SQL statement:", sql)  # Debugging statement
    try:
        cursor.execute(sql)
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # Optionally, you can print the full traceback for more information
        # import traceback
        # traceback.print_exc()
    conn.commit()
    conn.close()
# --------------------------------------------------------------
# method related to conditions and the data monitored
def insert_factors(database_name, table_name, column1, column2, column3, column4, column5, column6, column7, column8,
                   column9, values):
    """
    Inserts factors into the specified table.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    sql = f"INSERT INTO {table_name} ({column1}, {column2}, {column3},{column4},{column5},{column6},{column7},{column8},{column9}) VALUES {values}"
    cursor.execute(sql)

    conn.commit()
    conn.close()
# --------------------------------------------------------------
# Method that works for all queries
def insert_data(database_name, table_name, column1, column2, column3, column4, column5, column6, column7, column8,
                   column9, values):
    """
    Inserts data into the specified table.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Construct a SQLite sentence that insert values
    sql = f"INSERT INTO {table_name} ({column1}, {column2}, {column3},{column4},{column5},{column6},{column7},{column8},{column9}) VALUES {values}"
    cursor.execute(sql)

    conn.commit()
    conn.close()

def delete_data(database_name, table_name, data_id):
    """
    Deletes data from the specified table based on the given ID.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (data_id,))
    conn.commit()
    conn.close()
def query_data(database_name, table_name):
    """
    Retrieves data from the specified table.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    conn.close()
    return rows

#following two methods are mainly used to output the data stored in the database.
def query_max_Potid(database_name):
    """
    Retrieves the largest pot id. It can be used in future to further improve the code. Enable the user to add new
    pot to the program.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT MAX([Potid]) FROM pot LIMIT 1;")
    result = cursor.fetchall()
    conn.close()
    return result
def query_data_between_two_dates(database_name, table_name, columns, cal_start1, cal_end1, pot_id):
    """
    Retrieves data from the specified columns of a table between two given dates for a specific pot ID.
    """
    print(cal_end1)
    print(cal_start1)
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT {columns} FROM {table_name} WHERE Date BETWEEN '{cal_start1}' AND '{cal_end1}' AND Potid ='{pot_id}';")
    value_row = cursor.fetchall()
    conn.close()
    return value_row
def get_date_between_two_dates(database_name, table_name, cal_start1, cal_end1, pot_id):
    """
    Retrieves only the dates from the specified table between two given dates for a specific pot ID.
    """
    print(cal_end1)
    print(cal_start1)
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT Date FROM {table_name} WHERE Date BETWEEN '{cal_start1}' AND '{cal_end1}' AND Potid ='{pot_id}';")
    date_row = cursor.fetchall()
    conn.close()
    return date_row
def get_table_names(database_name):
    """
    Retrieves the names of all tables in the specified database.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    cursor.close()
    conn.close()
    return [table[0] for table in table_names]
def get_column(database_name, table_name, pot_id, columns):
    """
    Retrieves specific columns along with dates from a table for a specific pot ID.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT {columns}, Date FROM {table_name} WHERE Potid='{pot_id}';")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def get_all_column(database_name, table_name, columns):
    """
    Retrieves all columns along with dates and pot IDs from a table.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT {columns}, Date, Potid FROM {table_name} ;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def get_lastest_column(database_name, table_name, pot_ids, columns):
    """
    Retrieves the latest data for specified columns from the table for the given pot IDs.
    """
    # Ensure pot_ids is iterable (e.g., list, tuple)
    if not isinstance(pot_ids, (list, tuple)):
        pot_ids = [pot_ids]
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # Create a string of pot_ids to use in the WHERE clause
    pot_id_string = ','.join(str(pot_id) for pot_id in pot_ids)
    # Construct the SQL query
    sql = f"""
        SELECT {columns}
        FROM {table_name}
        WHERE Potid IN ({pot_id_string}) 
        AND [Date] IN (
            SELECT MAX([Date]) 
            FROM {table_name} 
            WHERE Potid IN ({pot_id_string}) 
            GROUP BY Potid
        )
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def get_number_of_rows(database_name, table_name, pot_id, columns):
    """
    Retrieves the count of rows for specified columns from the table for a specific pot ID.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT({columns}) FROM {table_name} WHERE Potid='{pot_id}';")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def get_all_number_of_rows(database_name, table_name, columns):
    """
    Retrieves the count of all rows for specified columns from the table.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT({columns}) FROM {table_name} ;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# --------------------------------------------------------------
# user related operations
def is_user(userName, password):
    conn = sqlite3.connect('HydroponicDB.db')
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT username,level FROM user WHERE username = '{userName}' and pwd = '{password}';")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    if result:
        print(result)
    return result
def check_user(userName, password):
    if is_user(userName, password):
        return True
    return False
def insert_new_user(userName, password, level):
    if not check_user(userName, password):
        values = (userName, password, level)
        conn = sqlite3.connect('HydroponicDB.db')
        cursor = conn.cursor()
        sql = f"INSERT INTO user (userName, pwd, level) VALUES {values}"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        print("new user assigned")
def get_column_user(database_name, table_name, columns):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT {columns}, userName, pwd, level FROM {table_name};")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def get_number_of_rows_user(database_name, table_name, columns):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT({columns}) FROM {table_name};")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def change_admin_name(userid, new_name):
    conn = sqlite3.connect('HydroponicDB.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE user SET userName = '{new_name}' WHERE userid = '{userid}'")
    conn.commit()
    conn.close()
def change_admin_password(userid, new_password):
    conn = sqlite3.connect('HydroponicDB.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE user SET pwd = '{new_password}' WHERE userid = '{userid}'")
    conn.commit()
    conn.close()
def insert_new_admin(username, password):
    conn = sqlite3.connect('HydroponicDB.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user (userName, pwd, level) VALUES (?, ?, '2')", (username, password))
    conn.commit()
    conn.close()
def delete_admin(username):
    conn = sqlite3.connect('HydroponicDB.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user WHERE userName = ? AND level = '2'", (username,))
    conn.commit()
    conn.close()
# --------------------------------------------------------------
# Condition related operations
def insert_conditions(database_name, table_name, pot_id, very_low, low, medium, high, tag, values):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # 构建插入数据的 SQL 语句
    sql = f"INSERT INTO {table_name} ({pot_id}, {very_low}, {low}, {medium},{high},{tag}) VALUES {values}"
    cursor.execute(sql)
    conn.commit()
    conn.close()
def get_conditions(database_name, table_name, pot_id, threshold, tag):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT {threshold} FROM {table_name} WHERE tag='{tag}' and Potid='{pot_id}'")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result[0][0]


def set_conditions(database_name, table_name, pot_id, values):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # cursor.execute(f"DELETE FROM {table_name} WHERE tag='{tag}' and Potid='{pot_id}'")
    cursor.execute(f"UPDATE {table_name} SET veryLow='{values[0]}', low='{values[1]}', medium='{values[2]}', high='{values[3]}' "
                   f"WHERE tag='{values[4]}' and Potid='{pot_id}'")

    # sql = f"INSERT INTO {table_name} ({pot_id}, {very_low}, {low}, {medium},{high},{tag}) VALUES {values}"
    print("testing set condition...")
    # cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

# --------------------------------------------------------------
# Plant related operations
def insert_plant(database_name, table_name, pot_id, species, variant, age, initialQuantity, quantity, growingStage, values):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # 构建插入数据的 SQL 语句
    sql = f"INSERT INTO {table_name} ({pot_id}, {species}, {variant}, {age},{initialQuantity},{quantity}, {growingStage}) VALUES {values}"
    cursor.execute(sql)
    conn.commit()
    conn.close()
def get_plant(database_name, table_name, pot_id, data):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT {data} FROM {table_name} WHERE Potid='{pot_id}'")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result[0][0]
def set_plant_super(database_name, table_name, pot_id, values):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # cursor.execute(f"DELETE FROM {table_name} WHERE tag='{tag}' and Potid='{pot_id}'")
    cursor.execute(f"UPDATE {table_name} SET species='{values[0]}', variant='{values[1]}', age='{values[2]}', "
                   f"initialQuantity='{values[3]}' "
                   f"WHERE Potid='{pot_id}'")

    # sql = f"INSERT INTO {table_name} ({pot_id}, {very_low}, {low}, {medium},{high},{tag}) VALUES {values}"
    print("testing set condition...")
    # cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()
def set_plant_regular(database_name, table_name, pot_id, values):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # cursor.execute(f"DELETE FROM {table_name} WHERE tag='{tag}' and Potid='{pot_id}'")
    cursor.execute(f"UPDATE {table_name} SET "
                   f"quantity='{values[0]}', growingStage='{values[1]}'"
                   f"WHERE Potid='{pot_id}'")

    # sql = f"INSERT INTO {table_name} ({pot_id}, {very_low}, {low}, {medium},{high},{tag}) VALUES {values}"
    print("testing set condition...")
    # cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()
