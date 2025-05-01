import tkinter as tk
from tkinter import ttk
from databaseOperations import dbMethods
"""
This script defines a function for creating a GUI table using tkinter. 
"""
def create_gui_table(window, columns):
    """Creates a GUI table using tkinter."""
    # Find the total number of pots
    max_Potid = dbMethods.query_max_Potid('HydroponicDB.db')
    max_Potid = [i[0] for i in max_Potid]
    int_max_Potid = max_Potid[0]

    # Get all column names
    dbMethods.get_all_column('HydroponicDB.db', 'pot', columns)

    # Get total number of rows
    total_rows = dbMethods.get_all_number_of_rows('HydroponicDB.db', 'pot', columns)[0]
    total_rows = [*total_rows][0]
    total_columns = 3

    # Create table window
    table_window = tk.Toplevel(window)
    table_window.geometry("750x250")
    table_window.title(columns)

    # Create main frame
    main_frame = tk.Frame(table_window)
    main_frame.pack(fill=tk.BOTH, expand=1)

    # Create canvas
    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Create vertical scrollbar
    my_scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # Get data from database
    lst = dbMethods.get_all_column('HydroponicDB.db', 'pot', columns)

    # Populate table
    for i in range(total_rows):
        for j in range(total_columns):
            table = tk.Entry(second_frame, width=20, fg='blue', font=('Arial', 16, 'bold'))
            table.grid(row=i, column=j)
            table.insert(tk.END, lst[i][j])

    return table
