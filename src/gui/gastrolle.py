import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import json
import os

# Datei für gespeicherte Buchungen
DATEI_NAME = "buchungen.json"

# Verfügbare Zeiten, Trainer und Kurse
zeiten = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
trainer = ["Trainer A", "Trainer B", "Trainer C"]
kurse = {
    "Yoga": "Entspannendes Yoga für Anfänger und Fortgeschrittene.",
    "Spinning": "Intensives Fahrradtraining zur Fettverbrennung.",
    "Zumba": "Tanzfitness mit lateinamerikanischer Musik.",
    "Pilates": "Ganzkörpertraining für Kraft und Beweglichkeit."}


# Buchungen aus Datei laden
def lade_buchungen():
    try:
        with open(DATEI_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Buchungen in Datei speichern
def speichere_buchungen():
    with open(DATEI_NAME, "w") as file:
        json.dump(buchungen, file, indent=4)

# Buchungs-Datensatz laden
buchungen = lade_buchungen()

# Hauptfenster erstellen
root = tk.Tk()
root.title("Fitnesskalender")
root.geometry("500x600")

# Kalender-Widget
cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
cal.pack(pady=10)

# Eingabefeld für Mitgliedsnummer
tk.Label(root, text="Mitgliedsnummer:").pack()
mitgliedsnummer_entry = tk.Entry(root)
mitgliedsnummer_entry.pack()

# Auswahl der Uhrzeit
uhrzeit_var = tk.StringVar(root)
uhrzeit_var.set(zeiten[0])
tk.Label(root, text="Uhrzeit auswählen:").pack()
tk.OptionMenu(root, uhrzeit_var, *zeiten).pack()

# Auswahl des Trainers
trainer_var = tk.StringVar(root)
trainer_var.set(trainer[0])
tk.Label(root, text="Trainer auswählen:").pack()
tk.OptionMenu(root, trainer_var, *trainer).pack()

# Auswahl des Kurses
kurs_var = tk.StringVar(root)
kurs_var.set(list(kurse.keys())[0])
tk.Label(root, text="Kurs auswählen:").pack()
kurs_dropdown = tk.OptionMenu(root, kurs_var, *kurse.keys())
kurs_dropdown.pack()

# Anzeige der Kursbeschreibung
kursbeschreibung_label = tk.Label(root, text="")
kursbeschreibung_label.pack()

def update_kursbeschreibung(*args):
    kursbeschreibung_label.config(text=kurse[kurs_var.get()])
kurs_var.trace("w", update_kursbeschreibung)
update_kursbeschreibung()

# Funktion zum Buchen eines Termins
def termin_buchen():
    datum = cal.get_date()
    uhrzeit = uhrzeit_var.get()
    trainer = trainer_var.get()
    kurs = kurs_var.get()
    mitgliedsnummer = mitgliedsnummer_entry.get()
    
    if not mitgliedsnummer:
        messagebox.showerror("Fehler", "Bitte Mitgliedsnummer eingeben!")
        return

    # Prüfen, ob der Termin bereits belegt ist
    for buchung in buchungen:
        if buchung["datum"] == datum and buchung["uhrzeit"] == uhrzeit:
            messagebox.showinfo("Warteliste", f"Der Termin am {datum} um {uhrzeit} ist bereits belegt. Sie wurden auf die Warteliste gesetzt.")
            buchungen.append({"datum": datum, "uhrzeit": uhrzeit, "mitgliedsnummer": mitgliedsnummer, "trainer": trainer, "kurs": kurs, "status": "Warteliste"})
            speichere_buchungen()
            return
    
    # Termin bestätigen
    buchungen.append({"datum": datum, "uhrzeit": uhrzeit, "mitgliedsnummer": mitgliedsnummer, "trainer": trainer, "kurs": kurs, "status": "bestätigt"})
    speichere_buchungen()
    messagebox.showinfo("Erfolg", f"Termin am {datum} um {uhrzeit} mit {trainer} für {kurs} wurde erfolgreich gebucht!")

# Buchungsbutton
tk.Button(root, text="Termin buchen", command=termin_buchen).pack(pady=10)

# Anzeige der bestehenden Buchungen
def anzeige_buchungen():
    buchungen_text = "\n".join([f"Datum: {b['datum']}, Uhrzeit: {b['uhrzeit']}, Mitglied: {b['mitgliedsnummer']}, Kurs: {b['kurs']}, Trainer: {b['trainer']}, Status: {b['status']}" for b in buchungen])
    messagebox.showinfo("Buchungen", buchungen_text)

# Button für Buchungsanzeige
tk.Button(root, text="Alle Buchungen anzeigen", command=anzeige_buchungen).pack(pady=10)

# Funktion zur Mitgliedsregistrierung
def registrieren():
    messagebox.showinfo("Registrierung", "Weiterleitung zur Mitgliedsregistrierung...")

# Button zur Mitgliedsregistrierung
tk.Button(root, text="Als Mitglied registrieren", command=registrieren).pack(pady=10)

# Hauptloop starten
root.mainloop()