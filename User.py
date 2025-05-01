from tkinter import ttk, simpledialog, messagebox
import tkinter as tk
from databaseOperations import dbMethods

"""
This script defines functions for creating GUI windows to perform various admin operations and displaying user data. 
"""
def change_admin_name_window():
    """Creates a window to change the name of an admin."""
    user_id = simpledialog.askinteger("Change Admin Name", "Enter user ID of the admin:")
    if user_id:
        new_name = simpledialog.askstring("Change Admin Name", "Enter new admin name:")
        if new_name:
            dbMethods.change_admin_name(user_id, new_name)
            messagebox.showinfo("Success", "Admin name changed successfully")

def change_admin_password_window():
    """Creates a window to change the password of an admin."""
    user_id = simpledialog.askinteger("Change Admin Password", "Enter user ID of the admin:")
    if user_id:
        new_password = simpledialog.askstring("Change Admin Password", "Enter new admin password:")
        if new_password:
            dbMethods.change_admin_password(user_id, new_password)
            messagebox.showinfo("Success", "Admin password changed successfully")

def add_new_admin_window():
    """Creates a window to add a new admin."""
    username = simpledialog.askstring("Add New Admin", "Enter username for new admin:")
    if username:
        password = simpledialog.askstring("Add New Admin", "Enter password for new admin:")
        if password:
            dbMethods.insert_new_admin(username, password)
            messagebox.showinfo("Success", "New admin added successfully")

def delete_admin_window():
    """Creates a window to delete an admin."""
    username = simpledialog.askstring("Delete Admin", "Enter username of admin to delete:")
    if username:
        confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to delete admin '{username}'?")
        if confirmation:
            dbMethods.delete_admin(username)
            messagebox.showinfo("Success", "Admin deleted successfully")

def create_gui_user(window, columns):
    """
    Creates a GUI window to display user data.

    Args:
    - window: Parent window for the GUI table.
    - columns: Columns to display in the table.

    Returns:
    - table: The created GUI table.
    """
    # Get user data from the database
    dbMethods.get_column_user('HydroponicDB.db', 'user', columns)
    total_rows = dbMethods.get_number_of_rows_user('HydroponicDB.db', 'user', columns)[0]
    total_rows = [*total_rows][0]
    total_columns = 4

    # Create a scrollable window
    table_window = tk.Toplevel(window)
    table_window.geometry("750x250")
    table_window.title("User List (pot id, username, password, level)")

    main_frame = tk.Frame(table_window)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = tk.Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # Get user data from the database
    lst = dbMethods.get_column_user('HydroponicDB.db', 'user', columns)

    # Populate the table
    for i in range(total_rows):
        for j in range(total_columns):
            table = tk.Entry(second_frame, width=20, fg='blue', font=('Arial', 16, 'bold'))
            table.grid(row=i, column=j)
            table.insert(tk.END, lst[i][j])

    return table
