import tkinter as tk
from tkinter import Menu, ttk
from gui.config import GUIConfig
from tkcalendar import Calendar
from pandastable import Table
from core.customers import Customers
from core.table_helper import TableHelper
from gui.menu_helper import MenuHelper
import pandas as pd
from core.data_provider import DataProvider

class App:
    root = False
    config = False
    role = False
    frame = False

    def __init__(self, root):
        self.root = root
        self.config = GUIConfig()
        self.root.title(self.config.app_title)
        self.debug()
        self.table_helper = TableHelper()
        self.menu_helper = MenuHelper(self.root)

    def set_role(self, role_name='guest'):
        self.role = role_name

    def run(self):
        # self.menu()
        return self.root

    def dispatch_role(self, role_name='guest'):
        self.role = role_name.lower()

        if role_name == 'admin':
            self.admin()

        elif role_name == 'guest':
            self.guest()

        elif role_name == 'staff':
            self.staff()

        elif role_name == 'member':
            self.member()

        self.menu()

    def admin(self):
        self.frame = self.workbench()

        self.table = self.table_helper.get_table(self.frame, 'time_slots')
        self.table.grid(row=1, column=2)
        self.table.show()

    def guest(self): # Pouria
        frame = self.workbench()
        my_cal = Calendar(frame,  selectmode="day")
        my_cal.grid(row=2, column=3)

        tk.Label(frame, text="Wähle einen Kurs:").grid(row=3, column=2)
        tk.Label(frame, text="Wähle eine Uhrzeit:").grid(row=4, column=2)
        tk.Label(frame, text="Wähle einen Trainer:").grid(row=5, column=2)

        df = pd.read_excel('../data/kursplan.xlsx') 
        dp = DataProvider()
        courses = dp.get_data('courses')
        times = df['Uhrzeit'].unique().tolist()
        trainers = df['Trainer'].unique().tolist()

        course_var = tk.StringVar()
        time_var = tk.StringVar()
        trainer_var = tk.StringVar()

        course_var.set(courses[0])
        time_var.set(times[0])
        trainer_var.set(trainers[0])

        tk.OptionMenu(frame, course_var, *courses).grid(row=3, column=3)
        tk.OptionMenu(frame, time_var, *times).grid(row=4, column=3)
        tk.OptionMenu(frame, trainer_var, *trainers).grid(row=5, column=3)

        def book_appointment():
            date = my_cal.get_date()
            course = course_var.get()
            time = time_var.get()
            trainer_name = trainer_var.get()
            tk.messagebox.showinfo("Buchung", f"Termin für {course} am {date} um {time} mit {trainer_name} wurde gebucht!")

        tk.Button(frame, text="Termin buchen", command=book_appointment).grid(row=6, column=3, pady=10)


    def staff(self):
        frame = self.workbench()
        dp = DataProvider()
        data = dp.get_data('trainers')
        print(data)


        exit()

    def member(self):
        frame = self.workbench()
        my_cal = Calendar(frame,  selectmode="day", font=("Arial", 20))
        my_cal.grid(row=0, column=0)

# Eingabe Mitgliedsnummer (Eingabefeld)                 # Pfadangabe zu Mitglieds ID von Sven eingeben
        mitglnr_label = tk.Label(frame, text="Mitgliedsnummer eingeben:") 
         #(row=0, column=1, padx=10, pady=10, sticky="n")
        mitglnr_eingabe = tk.Entry(frame)
        mitglnr_eingabe.grid(row=0, column=4, padx=10, pady=10, sticky="n", rowspan=12)
        #mitglnr_label.grid (row=0, column=4, padx=10, pady=10, sticky="n")  
        # Auswahl der Uhrzeit (Dropdown-Menü)
        zeiten = ["8:00", "10:00"]                       # Pfadangabe zu time_slot.csv von Sven eingeben
        uhrzeit_label=tk.Label(frame, text="Bitte Uhrzeit auswählen:")
        uhrzeit_label.grid(ipadx=7, ipady=12)
        uhrzeit_dropdown=ttk.Combobox(frame, value=zeiten)
        uhrzeit_dropdown.grid(ipadx=7, ipady=12)

        # Auswahl vom Wochentag (Dropdown-Menü)
        tag = ["Montag", "Dienstag"]
        tag_label = tk.Label(frame, text="Bitte wählen Sie den Wochentag:")
        tag_label.grid(ipadx=7, ipady=12)
        tag_dropdown = ttk.Combobox(frame, value=tag)
        tag_dropdown.grid(ipadx=7, ipady=12)

        # Auswahl der Buchung (Dropdown-Menü) (zugriff auf externe Liste)
        auswahl=["kurs", "Einzeltermin"]                  # Pfadangabe zur kurs.csv von Sven eingeben
        kursauswahl_label = tk.Label(frame, text="Bitte Kurs auswählen:")
        kursauswahl_label.grid(row=2, column= 4, ipadx=7, ipady=12)
        kursauswahl_dropdown = ttk.Combobox(frame, value=auswahl)
        kursauswahl_dropdown.grid(row=3, column= 4, ipadx=7, ipady=12)

        # Trainerauswahl (Dropdown-Menü)
        trainer = ["Pouria", "Tim", "Laura"]
        trainer_label = tk.Label(frame, text="Bitte den Trainer auswählen:")
        trainer_label.grid(row=4, column= 4, ipadx=7, ipady=12)
        trainer_dropdown = ttk.Combobox(frame, value=trainer)
        trainer_dropdown.grid(row=5, column= 4, ipadx=7, ipady=12)

        # Buchung tätigen (Bestätigungsbutton)
        bestaetigung_button = tk.Button(frame, text="Buchung bestätigen", command=lambda: messagebox.showinfo("Bestätigung", "Buchung wurde bestätigt!"))
        bestaetigung_button.grid(row=7, column= 3, ipadx=7, ipady=12)


        # Buchung tätigen
        #buchungen = []




    def menu(self):
        content = {
            'Kalender': self.dispatch_cal,
            'Mitglieder': self.dispatch_memb,
            'Trainer': self.dispatch_tr,
            'Zeiten': self.dispatch_time,
            'Buchungen': self.dispatch_customer_calendar,
        }

        menubar = self.menu_helper.get_menu_by_role(self.role, content)

        # for topic in self.config.menu_topics.keys():

        # curr_mnu = Menu(menubar)

        # menubar.add_cascade(label='Mitglieder', menu='curr_mnu':self.dispatch_menu())

        # for item in self.config.menu_topics[topic]:
        #     curr_mnu.add_command(label=item:self.dispatch_menu(item))

    def debug(self):
        import os

        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)

    def workbench(self):
        ''' “Arbeitstisch„  je Rolle'''

        design = self.config.design_by_role[self.role]

        # nur zum Entwickeln
        frame = tk.Frame(self.root, bg=design[0])
        frame.place(relwidth=1, relheight=1)
        print(self.role.capitalize())
        lbl = tk.Label(frame, text=self.role)
        lbl.grid(row=0, column=0)
        return frame

    def handle_frame(self):
        if self.frame != False:
            self.frame.destroy()
        design = self.config.design_by_role[self.role]
        frame = tk.Frame(self.root, bg=design[0])
        frame.place(relwidth=1, relheight=1)
        return frame

    def dispatch_cal(self):
        print('cal')
        self.frame = self.handle_frame()
        my_cal = Calendar(self.frame, selectmode='day')
        my_cal.grid(row=1, column=1)

    def dispatch_tr(self):
        self.show_objects('trainers')

    def dispatch_time(self):
        self.show_objects('time_slots')
        
    def dispatch_memb(self):
        self.show_objects('customers')
        
    def dispatch_customer_calendar(self):
         self.show_objects('customer_calendar')

    def show_objects(self, topic):
        frame = self.handle_frame()
        print('Topic aus show_objects: ' + topic)
        self.table = self.table_helper.get_table(frame, topic)
        self.table.grid(row=1, column=2)
        self.table.show()
