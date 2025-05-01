"""""
This script provides functionality for user login and GUI initialization. 

Functions:
- login(): Handles user login functionality by checking the provided username and password against the database. 
  It displays appropriate messages based on the login result and redirects to the corresponding GUI for super admin 
  or normal admin.
- guestIntro(): Redirects the user to the guest GUI.
- __main__(): Initializes the application by creating database tables, generating mock data, starting a separate thread 
  for automatic data recording, and setting up the login GUI.

Dependencies:
- tkinter: GUI library for Python.
- messagebox: A sub-module of tkinter for displaying messages.
- Recorder: Class for automatic data recording.
- dbMethods: Module containing database operation methods.
- dbTables: Module containing methods for creating database tables.
- mockDataGenerator: Module for generating mock data.
- guiDesign: Module containing GUI design functions.
"""""
import tkinter as tk
from tkinter import messagebox
from autoRecord import Recorder
from databaseOperations import dbMethods
from databaseOperations import dbTables
import mockDataGenerator
import guiDesign


def login():
    """Handles user login functionality."""
    username = username_entry.get()
    password = password_entry.get()

    # Check Username and Password
    res = dbMethods.is_user(username, password)

    if res:
        messagebox.showinfo("Login succeed!", "Welcome, " + username + "!")
        window.destroy()
        # 1 represents super admin, other numbers represent normal admin in database logic
        if res[0][1] == '1':
            guiDesign.superAdminGUI()
        else:
            guiDesign.normalGUI()
    else:
        messagebox.showerror("Failed to login", "User name or Password are wrong!")
        password_entry.delete(0, tk.END)

def guestIntro():
    """Redirects the user to the guest GUI."""
    window.destroy()
    guiDesign.guestGUI()


if __name__ == '__main__':
    # Connect or create the database
    print("Programming start...")
    dbTables.create_dbTables()
    mockDataGenerator.generateMockData(10, 10)
    # Threading
    print("Thread start...")
    thread1 = Recorder()
    thread1.start()

    # Login
    print("Login start...")
    window = tk.Tk()
    window.title("User Login")

    # Setting window position
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    dialog_width = 300
    dialog_height = 200

    x = int((screen_width / 2) - (dialog_width / 2))
    y = int((screen_height / 2) - (dialog_height / 2))
    window.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

    username_label = tk.Label(window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    password_label = tk.Label(window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    login_button = tk.Button(window, text="Login", command=login)
    login_button.pack()

    register_button = tk.Button(window, text="Guest user", command=guestIntro)
    register_button.pack()

    window.mainloop()
