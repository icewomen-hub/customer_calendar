import tkinter as tk
from tkinter import Menu
from gui.config import GUIConfig
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

# Auswahl der Uhrzeit (Dropdown-Menü)
        zeiten = ["8:00", "10:00"]                       # Pfadangabe zu time_slot.csv von Sven eingeben
        uhrzeit_label=tk.Label(frame, text="Bitte Uhrzeit auswählen:")
        uhrzeit_label.grid(ipadx=7, ipady=12)
        uhrzeit_dropdown=ttk.Combobox(frame, value=zeiten)
        uhrzeit_dropdown.grid(ipadx=7, ipady=12)

        # Auswahl vom Wochentag
        tag = ["Montag", "Dienstag"]
        tag_label = tk.Label(frame, text="Bitte wählen Sie den Wochentag:")
        tag_label.grid(ipadx=7, ipady=12)
        tag_dropdown = ttk.Combobox(frame, value=tag)
        tag_dropdown.grid(ipadx=7, ipady=12)

        # Auswahl der Buchung (zugriff auf externe Liste)
        auswahl=["kurs", "Einzeltermin"]                  # Pfadangabe zur kurs.csv von Sven eingeben
        kursauswahl_label = tk.Label(frame, text="Bitte Kurs auswählen:")
        kursauswahl_label.grid(row=2, column= 4, ipadx=7, ipady=12)
        kursauswahl_dropdown = ttk.Combobox(frame, value=auswahl)
        kursauswahl_dropdown.grid(row=3, column= 4, ipadx=7, ipady=12)

        # Trainerauswahl
        trainer = ["Pouria", "Tim", "Laura"]
        trainer_label = tk.Label(frame, text="Bitte den Trainer auswählen:")
        trainer_label.grid(row=4, column= 4, ipadx=7, ipady=12)
        trainer_dropdown = ttk.Combobox(frame, value=trainer)
        trainer_dropdown.grid(row=5, column= 4, ipadx=7, ipady=12)

        # Buchung tätigen
        bestaetigung_button = tk.Button(frame, text="Buchung bestätigen", command=lambda: messagebox.showinfo("Bestätigung", "Buchung wurde bestätigt!"))
        bestaetigung_button.grid(row=7, column= 3, ipadx=7, ipady=12)


        # Buchung tätigen
        buchungen = []



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
