
from User import *

def gui_users(tab6):
    """""
    This function creates a GUI for managing user-related operations. It imports a function `create_gui_user` from a module called `User`, and imports everything from the same module.
    """""

    label = tk.Label(tab6, text='Select the following buttons: ', anchor=tk.NW)
    label.pack()

    # Button widgets for user operations
    btn_admin_list = tk.Button(tab6, text="Admin List", command=lambda: create_gui_user(tab6, 'userid'))
    btn_admin_list.pack()

    btn_change_admin_name = tk.Button(tab6, text="Change Admin Name", command=change_admin_name_window)
    btn_change_admin_name.pack()

    btn_change_admin_pw = tk.Button(tab6, text="Change Admin Password", command=change_admin_password_window)
    btn_change_admin_pw.pack()

    btn_add_new_admin = tk.Button(tab6, text="Add New Admin", command=add_new_admin_window)
    btn_add_new_admin.pack()

    btn_delete_admin = tk.Button(tab6, text="Delete Admin", command=delete_admin_window)
    btn_delete_admin.pack()
