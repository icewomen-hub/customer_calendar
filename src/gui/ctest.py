import tkinter as tk
from tkcalendar import Calendar # type: ignore


def buchen():                           
    datum = calendar.selection_get()     # 
    print(datum)


# Erstellen des Ausgangsfensters
work_root = tk.Tk()      # Code-Name für das Fenster das ich kreire
work_root.title("Fitnesskalender") # Titel für das Fenster
work_root.geometry("500x500")      # Größe für das Fenster

calendar = Calendar(work_root, selectmode="day", date_pattern="yyyy-mm-dd")  # erzeugt die Anzeige des Kalenders im Fenster
calendar.pack(pady=20)      # platziert den Kalender im Fenster

# Eingabefeld für Mitgliedsnummer
tk.Label(work_root, text="Mitgliedsnummer:").pack() # erzeugt Text
mitgliedsnummer_entry = tk.Entry(work_root)         # erzeugt ein Eingabefenster
mitgliedsnummer_entry.pack()                        # zeigt das Eingabefenster im work_root an

# Auswahl der Uhrzeit (Dropdown-Menü)
zeiten = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
uhrzeit_var = tk.StringVar(work_root)
uhrzeit_var.set(zeiten[0])  # Standardwert setzen
tk.OptionMenu(work_root, uhrzeit_var, *zeiten).pack()

# Buchungsbutton erzeugen
buchung_btn = tk.Button(work_root, text="Datum wählen", command=buchen)
buchung_btn.pack()
# Sven_
work_root.mainloop()