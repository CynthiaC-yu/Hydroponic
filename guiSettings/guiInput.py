import tkinter as tk
from tkinter import ttk, END
from databaseOperations import dbMethods


'''
This code defines two functions, guiInputSuper and guiInputNormal, to create GUI input elements for different 
types of systems.
'''

def guiInputSuper(tab5):
    """
    Function to create GUI input for super admin
    """
    print("Super Input")
    # Labels and widgets for system ID
    l_system_id = tk.Label(tab5, text="ID of the system!")
    l_system_id.config(font=("Courier", 14))
    l_system_id.grid(row=1, column=0)

    var_system_id = tk.IntVar()
    var_system_id.set(1)
    spin_system_id = tk.Spinbox(tab5, from_=1, to=10, textvariable=var_system_id)
    spin_system_id.grid(row=1, column=1)

    # Labels and widgets for species
    l_species = tk.Label(tab5, text="Species: ")
    l_species.config(font=("Courier", 14))
    l_species.grid(row=2, column=0)

    t_species = tk.Text(tab5, height=1, width=20)
    species_text = ""
    t_species.insert(tk.END, species_text)
    t_species.grid(row=2, column=1)

    # Labels and widgets for variant
    l_variant = tk.Label(tab5, text="Variant: ")
    l_variant.config(font=("Courier", 14))
    l_variant.grid(row=3, column=0)

    t_variant = tk.Text(tab5, height=1, width=20)
    variant_text = ""
    t_variant.insert(tk.END, variant_text)
    t_variant.grid(row=3, column=1)

    # Labels and widgets for initial age
    l_initial_age = tk.Label(tab5, text="The age of plant when plant it on the system: ")
    l_initial_age.config(font=("Courier", 14))
    l_initial_age.grid(row=4, column=0)

    var_init_age = tk.IntVar()
    var_init_age.set(0)
    spin_initial_age = tk.Spinbox(tab5, from_=0, to=100, textvariable=var_init_age)
    spin_initial_age.grid(row=4, column=1)

    # Labels and widgets for initial quantity
    l_initial_quantity = tk.Label(tab5, text="Initial quantity: ")
    l_initial_quantity.config(font=("Courier", 14))
    l_initial_quantity.grid(row=5, column=0)

    var_init_qty = tk.IntVar()
    var_init_qty.set(0)
    spin_initial_qty = tk.Spinbox(tab5, from_=0, to=100, textvariable=var_init_qty)
    spin_initial_qty.grid(row=5, column=1)

    # Labels and widgets for quantity
    l_qty = tk.Label(tab5, text="Quantity: ")
    l_qty.config(font=("Courier", 14))
    l_qty.grid(row=6, column=0)

    t_qty = tk.Text(tab5, height=1, width=10)
    qty_text = ""
    t_qty.insert(tk.END, qty_text)
    t_qty.grid(row=6, column=1)

    # Labels and widgets for growing stage
    l_growing_stage = tk.Label(tab5, text="Growing stage: ")
    l_growing_stage.config(font=("Courier", 14))
    l_growing_stage.grid(row=7, column=0)

    t_growing_stage = tk.Text(tab5, height=1, width=10)
    growing_stage_text = ""
    t_growing_stage.insert(tk.END, growing_stage_text)
    t_growing_stage.grid(row=7, column=1)

    # Function to load data based on system ID
    def load_data(pot_id):
        species_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'species')
        t_species.delete('1.0', END)
        t_species.insert(tk.END, species_text)

        variant_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'variant')
        t_variant.delete('1.0', END)
        t_variant.insert(tk.END, variant_text)

        var_init_age.set(dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'age'))

        var_init_qty.set(dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'initialQuantity'))

        qty_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'quantity')
        t_qty.delete('1.0', END)
        t_qty.insert(tk.END, qty_text)

        growing_stage_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'growingStage')
        t_growing_stage.delete('1.0', END)
        t_growing_stage.insert(tk.END, growing_stage_text)

    # Load data for default ID
    load_data(1)

    # Function to handle loading data on button click
    def loadButtonListener(event):
        system_id = spin_system_id.get()
        load_data(system_id)

    # Button to load data
    btn_load = tk.Button(tab5, text="Load")
    btn_load.grid(row=0, column=0)
    btn_load.bind("<Button-1>", loadButtonListener)

    # Function to handle updating data on button click
    def updateButtonListener(event):
        system_id = int(spin_system_id.get())
        species = t_species.get("1.0", "end-1c")
        variant = t_variant.get("1.0", "end-1c")
        age = var_init_age.get()
        init_qty = var_init_qty.get()
        values = (species, variant, age, init_qty)
        print("update***" * 20)
        print(values)
        dbMethods.set_plant_super('HydroponicDB.db', 'Plant', system_id, values)

    # Button to update data
    btn_update = tk.Button(tab5, text="Update")
    btn_update.grid(row=0, column=1)
    btn_update.bind("<Button-1>", updateButtonListener)

# Function to create GUI input for normal system
def guiInputNormal(tab5):
    """
    Function to create GUI input for normal admins
    """
    print("Normal Input")
    # Labels and widgets for system ID
    l_system_id = tk.Label(tab5, text="ID of the system!")
    l_system_id.config(font=("Courier", 14))
    l_system_id.grid(row=1, column=0)

    var_system_id = tk.IntVar()
    var_system_id.set(1)
    spin_system_id = tk.Spinbox(tab5, from_=1, to=10, textvariable=var_system_id)
    spin_system_id.grid(row=1, column=1)

    # Labels and widgets for species
    l_species = tk.Label(tab5, text="Species: ")
    l_species.config(font=("Courier", 14))
    l_species.grid(row=2, column=0)

    t_species = tk.Text(tab5, height=1, width=20)
    species_text = ""
    t_species.insert(tk.END, species_text)
    t_species.grid(row=2, column=1)

    # Labels and widgets for variant
    l_variant = tk.Label(tab5, text="Variant    : ")
    l_variant.config(font=("Courier", 14))
    l_variant.grid(row=3, column=0)

    t_variant = tk.Text(tab5, height=1, width=20)
    variant_text = ""
    t_variant.insert(tk.END, variant_text)
    t_variant.grid(row=3, column=1)

    # Labels and widgets for initial age
    l_initial_age = tk.Label(tab5, text="The age of plant when plant it on the system: ")
    l_initial_age.config(font=("Courier", 14))
    l_initial_age.grid(row=4, column=0)

    var_init_age = tk.IntVar()
    var_init_age.set(0)
    spin_initial_age = tk.Spinbox(tab5, from_=0, to=100, textvariable=var_init_age)
    spin_initial_age.grid(row=4, column=1)

    # Labels and widgets for initial quantity
    l_initial_quantity = tk.Label(tab5, text="Initial quantity: ")
    l_initial_quantity.config(font=("Courier", 14))
    l_initial_quantity.grid(row=5, column=0)

    var_init_qty = tk.IntVar()
    var_init_qty.set(0)
    spin_initial_qty = tk.Spinbox(tab5, from_=0, to=100, textvariable=var_init_qty)
    spin_initial_qty.grid(row=5, column=1)

    # Labels and widgets for quantity
    l_qty = tk.Label(tab5, text="Quantity: ")
    l_qty.config(font=("Courier", 14))
    l_qty.grid(row=6, column=0)

    var_qty = tk.IntVar()
    var_qty.set(0)
    spin_qty = tk.Spinbox(tab5, from_=0, to=100, textvariable=var_init_qty)
    spin_qty.grid(row=6, column=1)

    # Labels and widgets for growing stage
    l_growing_stage = tk.Label(tab5, text="Growing stage: ")
    l_growing_stage.config(font=("Courier", 14))
    l_growing_stage.grid(row=7, column=0)

    t_growing_stage = tk.Text(tab5, height=1, width=10)
    growing_stage_text = ""
    t_growing_stage.insert(tk.END, growing_stage_text)
    t_growing_stage.grid(row=7, column=1)

    # Function to load data based on system ID
    def load_data(pot_id):
        species_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'species')
        t_species.delete('1.0', END)
        t_species.insert(tk.END, species_text)

        variant_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'variant')
        t_variant.delete('1.0', END)
        t_variant.insert(tk.END, variant_text)

        var_init_age.set(dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'age'))

        var_init_qty.set(dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'initialQuantity'))

        var_qty.set(dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'quantity'))

        growing_stage_text = dbMethods.get_plant('HydroponicDB.db', 'Plant', pot_id, 'growingStage')
        t_growing_stage.delete('1.0', END)
        t_growing_stage.insert(tk.END, growing_stage_text)

    # Function to handle loading data on button click
    def loadButtonListener(event):
        system_id = spin_system_id.get()
        load_data(system_id)

    # Button to load data
    btn_load = tk.Button(tab5, text="Load")
    btn_load.grid(row=0, column=0)
    btn_load.bind("<Button-1>", loadButtonListener)

    # Function to handle updating data on button click
    def updateButtonListener(event):
        system_id = int(spin_system_id.get())
        qty = var_qty.get()
        growingStage = t_growing_stage.get("1.0", "end-1c")
        values = (qty, growingStage)
        print("update***" * 20)
        print(values)
        dbMethods.set_plant_regular('HydroponicDB.db', 'Plant', system_id, values)

    # Button to update data
    btn_update = tk.Button(tab5, text="Update")
    btn_update.grid(row=0, column=1)
    btn_update.bind("<Button-1>", updateButtonListener)