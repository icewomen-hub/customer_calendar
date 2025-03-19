import tkinter as tk
from tkinter import Menu
from gui.config import GUIConfig
from tkinter import messagebox, ttk
from tkcalendar import Calendar

class App:
    root = False
    config = False
    role = False
    
    def __init__(self, root):
        self.root = root
        self.config = GUIConfig()
        self.root.title(self.config.app_title)
        self.debug()

    def set_role(self, role_name='guest'):
        self.role = role_name
        
    def run(self):
        #self.menu()
        return self.root
    
    def dispatch_role(self, role_name='guest'):
        self.role = role_name.lower()
        
        if role_name == 'admin':
            self.admin() 
            
        elif role_name  == 'guest':
            self.guest() 
            
        elif role_name == 'staff':
            self.staff() 
        
        elif role_name  == 'member':
            self.member() 
        
        
        
        self.menu()
   
   
    def admin(self): # Sven
        frame = self.workbench()
        entry = tk.Label(self.root, text='Dies ist ein label')
        entry.grid(row=1, column=1)
    
    def guest(self): # Pouria
        frame = self.workbench()

    
    def staff(self): # Aleksej
        frame = self.workbench()

    def member(self):  # Christine        
        frame = self.workbench()

        calendar = Calendar(frame, selectmode="day", date_pattern="yyyy-mm-dd")  # erzeugt die Anzeige des Kalenders im Fenster
        calendar.pack(pady=20)      # platziert den Kalender im Fenster

        # Auswahl der Uhrzeit (Dropdown-Menü)
        zeiten = ["8:00", "10:00"]                       # Pfadangabe zu time_slot.csv von Sven eingeben
        uhrzeit_label=tk.Label(frame, text="Bitte Uhrzeit auswählen:")
        uhrzeit_label.pack()
        uhrzeit_dropdown=ttk.Combobox(frame, value=zeiten)
        uhrzeit_dropdown.pack()

        # Auswahl der Buchung (zugriff auf externe Liste)
        auswahl=["kurs", "Einzeltermin"]                  # Pfadangabe zur kurs.csv von Sven eingeben
        kursauswahl_label = tk.Label(frame, text="Kurs auswählen:")
        kursauswahl_label.pack()
        kursauswahl_dropdown = ttk.Combobox(frame, value=auswahl)
        kursauswahl_dropdown.pack()

        # Trainerauswahl
        trainer = ["Pouria", "Tim", "Laura"]
        trainer_label = tk.Label(frame, text="Bitte den Trainer auswählen:")
        trainer_label.pack()
        trainer_dropdown = ttk.Combobox(frame, value=trainer)
        trainer_dropdown.pack()

        # Auswahl vom Wochentag
        tag = ["Montag", "Dienstag"]
        tag_label = tk.Label(frame, text="Bitte wählen Sie den Wochentag:")
        tag_label.pack()
        tag_dropdown = ttk.Combobox(frame, value=tag)
        tag_dropdown.pack()

        # Buchung tätigen
        buchungen = []

        def buchung_hinzufuegen():
            buchungen.append("Buchung bestätigt")
            with open(dateipfad, "w") as file:
                json.dump(buchungen, file)
                
                buchungen_label.config(text=f"Buchungen: {', '.join(buchungen)}")

        bestaetigungs_button = tk.Button(frame, text="Buchung bestätigen", command=buchung_hinzufuegen)
        bestaetigungs_button.pack()


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
        """ “Arbeitstisch„  je Rolle """
        
        design = self.config.design_by_role[self.role]
        
        # nur zum Entwickeln
        frame = tk.Frame(self.root, bg=design[0])
        frame.place(relwidth=1, relheight=1)
        print(self.role.capitalize())
        lbl = tk.Label(frame, text=self.role)
        lbl.grid(row=0, column=0)
        return frame
   
        
        