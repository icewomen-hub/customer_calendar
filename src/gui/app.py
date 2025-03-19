import tkinter as tk
from tkinter import Menu
from gui.config import GUIConfig
from core.state import State
from tkcalendar import Calendar
from pandastable import Table
from core.customers import Customers
from core.table_helper import TableHelper

class App:
    root = False
    config = False
    role = False

    def __init__(self, root):
        self.root = root
        self.config = GUIConfig()
        self.root.title(self.config.app_title)
        self.debug()
        self.table_helper = TableHelper()

    def set_role(self, role_name="guest"):
        self.role = role_name

    def run(self):
        # self.menu()
        return self.root

    def dispatch_role(self, role_name="guest"):
        self.role = role_name.lower()

        if role_name == "admin":
            self.admin()

        elif role_name == "guest":
            self.guest()

        elif role_name == "staff":
            self.staff()

        elif role_name == "member":
            self.member()

        self.menu()

    def admin(self):
        frame = self.workbench()
        # my_cal = Calendar(frame, selectmode="day")
        # my_cal.grid(row=1, column=1)
        # customers = Customers()
        # my_data = customers.get_data()

        self.table = self.table_helper.get_table(frame, 'trainers')
        self.table.grid(row=1, column=2)
        self.table.show()

    def guest(self): # Pouria
        frame = self.workbench()
        my_cal = Calendar(frame,  selectmode="day")
        my_cal.grid(row=2, column=3)



    def staff(self):
        frame = self.workbench()

    def member(self): # Christine
        frame = self.workbench()
        my_cal = Calendar(frame,  selectmode="day")
        my_cal.grid(row=2, column=3)

    def menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        for topic in self.config.menu_topics.keys():

            curr_mnu = Menu(menubar)
            menubar.add_cascade(label=topic, menu=curr_mnu)
            for item in self.config.menu_topics[topic]:
                curr_mnu.add_command(label=item, command=self.root.destroy)

    def debug(self):
        import os

        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)

    def workbench(self):
        """“Arbeitstisch„  je Rolle"""

        design = self.config.design_by_role[self.role]

        # nur zum Entwickeln
        frame = tk.Frame(self.root, bg=design[0])
        frame.place(relwidth=1, relheight=1)
        print(self.role.capitalize())
        lbl = tk.Label(frame, text=self.role)
        lbl.grid(row=0, column=0)
        return frame
