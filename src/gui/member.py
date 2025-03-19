import tkinter as tk

from tkinter import messagebox, ttk     # ttk beinhaltet erweiterte optionen der messagebox
from tkcalendar import Calendar
#from core.data_provider import DataProvider     # dieser Import ließt die Dateien (kurs, time_slot etc.) und stellt die Daten als
                                                # pandas DataFrames zur Verfügung (Es werden die hier hinterlegten Methoden benutzt
                                                # für alle Funktionalitäten, die ich als Anwender nutzen möchte.)

'''
dp = DataProvider()
ts = dp.time_slot_per_day("Samstag")


ts2 = ts = dp.time_slots_per_course('Yoga')

print(ts)
exit()

def buchen():                           
    datum = calendar.selction_get()     # 
    print(datum)
'''

# Erstellen des Ausgangsfensters
work_root = tk.Tk()      # Code-Name für das Fenster das ich kreire
work_root.title("Fitnesskalender") # Titel für das Fenster
work_root.geometry("500x800")      # Größe für das Fenster

calendar = Calendar(work_root, selectmode="day", date_pattern="yyyy-mm-dd")  # erzeugt die Anzeige des Kalenders im Fenster
calendar.pack(pady=20)      # platziert den Kalender im Fenster

# Auswahl der Uhrzeit (Dropdown-Menü)
zeiten = ["8:00", "10:00"]                       # Pfadangabe zu time_slot.csv von Sven eingeben
uhrzeit_label=tk.Label(work_root, text="Bitte Uhrzeit auswählen:")
uhrzeit_label.pack()
uhrzeit_dropdown=ttk.Combobox(work_root, value=zeiten)
uhrzeit_dropdown.pack()

# Auswahl der Buchung (zugriff auf externe Liste)
auswahl=["kurs", "Einzeltermin"]                                            # Pfadangabe zur kurs.csv von Sven eingeben
kursauswahl_label = tk.Label(work_root, text="Kurs auswählen:")
kursauswahl_label.pack()
kursauswahl_dropdown = ttk.Combobox(work_root, value=auswahl)
kursauswahl_dropdown.pack()

# Trainerauswahl
trainer = ["Pouria", "Tim", "Laura"]
trainer_label = tk.Label(work_root, text="Bitte den Trainer auswählen:")
trainer_label.pack()
trainer_dropdown = ttk.Combobox(work_root, value=trainer)
trainer_dropdown.pack()

# Auswahl vom Wochentag
tag = ["Montag", "Dienstag"]
tag_label = tk.Label(work_root, text="Bitte wählen Sie den Wochentag:")
tag_label.pack()
tag_dropdown = ttk.Combobox(work_root, value=tag)
tag_dropdown.pack()

# Buchung tätigen
buchungen = []

def buchung_hinzufuegen():
    buchungen.append("Buchung bestätigt")

    with open(dateipfad, "w") as file:
        json.dump(buchungen, file)

    buchungen_label.config(text=f"Buchungen: {', '.join(buchungen)}")

bestaetigungs_button = tk.Button(work_root, text="Buchung bestätigen", command=buchung_hinzufuegen)
bestaetigungs_button.pack()


# Buchung tätigen und Buchung in Kundenstammdaten abspeichern



work_root.mainloop()
