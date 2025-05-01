# Importing necessary GUI modules
from guiSettings import guiCondition
from guiSettings import guiController
from guiSettings import guiInput
from guiSettings import guiModel
from guiSettings import guiReport
from guiSettings import guiTable
from guiSettings import guiUsers

import tkinter as tk
from tkinter import ttk

# Main GUI for super admin
def superAdminGUI():
    """
    Creates the main GUI window for the super admin with multiple tabs for different functionalities.
    """
    window = tk.Tk()
    window.title("Hydroponic Management System")

    tabControl = ttk.Notebook(window)

    # Define tabs for different functionalities
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6 = ttk.Frame(tabControl)
    tab7 = ttk.Frame(tabControl)

    # Add tabs to the tab control
    tabControl.add(tab1, text='Report')
    tabControl.add(tab2, text='Controller')
    tabControl.add(tab3, text='Model')
    tabControl.add(tab4, text='Table')
    tabControl.add(tab5, text='Input')
    tabControl.add(tab6, text='Users')
    tabControl.add(tab7, text='Condition')
    tabControl.pack(expand=1, fill="both")

    # Load GUI components for each tab
    guiReport.gui_report(tab1)
    guiController.gui_controller(tab2)
    guiModel.draw_gui_model(tab3)
    guiTable.gui_table(tab4)
    guiInput.guiInputSuper(tab5)
    guiUsers.gui_users(tab6)
    guiCondition.gui_condition(tab7)

    window.mainloop()

# Main GUI for normal users
def normalGUI():
    """
    Creates the main GUI window for normal users with limited functionalities.
    """
    window = tk.Tk()
    window.title("Hydroponic Management System")

    tabControl = ttk.Notebook(window)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Report')
    tabControl.add(tab2, text='Controller')
    tabControl.add(tab3, text='Model')
    tabControl.add(tab4, text='Table')
    tabControl.add(tab5, text='Input')
    tabControl.pack(expand=1, fill="both")

    guiReport.gui_report(tab1)
    guiController.gui_controller(tab2)
    guiModel.draw_gui_model(tab3)
    guiTable.gui_table(tab4)
    guiInput.guiInputNormal(tab5)

    window.mainloop()

# Main GUI for guest users
def guestGUI():
    """
    Creates the main GUI window for guest users with limited functionalities.
    """
    window = tk.Tk()
    window.title("Hydroponic Management System")

    tabControl = ttk.Notebook(window)

    tab1 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Report')
    tabControl.add(tab3, text='Model')
    tabControl.add(tab4, text='Table')
    tabControl.pack(expand=1, fill="both")

    guiReport.gui_report(tab1)
    guiModel.draw_gui_model(tab3)
    guiTable.gui_table(tab4)

    window.mainloop()
