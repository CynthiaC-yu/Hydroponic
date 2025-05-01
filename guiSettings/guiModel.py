from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox

from Model import *
from tkcalendar import Calendar
from datetime import datetime


def draw_gui_model(tab3):
    """
    Function to draw GUI elements for selecting variables and plotting graphs.
    """
    # Select the type of value
    # label text for title
    Label(tab3, text="Select the variable:").grid(row=0, column=0, padx=20, pady=50)
    # Combobox creation
    current_var = tk.StringVar()
    value_chosen = Combobox(tab3, width=27, textvariable=current_var)
    value_chosen.grid(row=0, column=1)
    # Adding combobox drop down list
    value_chosen['values'] = (' Water Level',
                              ' Room Temperature',
                              ' Water Temperature',
                              ' Oxygen Level',
                              ' pH Level',
                              ' Nutrition Level',
                              ' Moisture Level'
                              )
    value_chosen.current()

    # Select the type of graph
    # label text for title
    Label(tab3, text="Select the type of graph:").grid(row=1, column=0, padx=20, pady=50)
    # Combobox creation
    n = tk.StringVar()
    graph_chosen = Combobox(tab3, width=27, textvariable=n)
    graph_chosen.grid(row=1, column=1)
    # Adding combobox drop down list
    graph_chosen['values'] = (' Scatter Plot',
                              ' Bar Graph'
                              )
    graph_chosen.current()

    # Spinner for selecting pot ID
    Label(tab3, text="Select the Pot ID:").grid(row=2, column=0, padx=20, pady=50)
    pot_id_spinner = Spinbox(tab3, from_=1, to=10)  # Update the 'to' value based on your requirement
    pot_id_spinner.grid(row=2, column=1)

    # Calendar
    # label text for title
    Label(tab3, text="Select time you want to check:").grid(row=3, column=0, padx=20, pady=50)
    cal_start = Calendar(tab3, selectmode='day')
    cal_start.grid(row=3, column=1)
    cal_end = Calendar(tab3, selectmode='day')
    cal_end.grid(row=3, column=2)

    def get_selected_date():
        """
        Function to get the selected start and end dates and trigger graph plotting.
        """
        cal_start1 = cal_start.get_date()
        cal_end1 = cal_end.get_date()
        print("Selected date_start:", cal_start1)
        print("Selected date_end:", cal_end1)

        cal_start1 = datetime.strptime(cal_start1, "%m/%d/%y").strftime("%Y-%m-%d")
        cal_end1 = datetime.strptime(cal_end1, "%m/%d/%y").strftime("%Y-%m-%d")

        value_type = value_chosen.get().replace(' ', '')
        selected_pot_id = int(pot_id_spinner.get())  # Get the selected pot ID from the spinner

        print("Value Type:", value_type)
        print("Selected Pot ID:", selected_pot_id)

        test_draw_diagram(value_type, cal_start1, cal_end1, selected_pot_id)

    Button(tab3, text="Get Selected Date", command=get_selected_date).grid(row=4, column=0, padx=20, pady=50)