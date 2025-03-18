import json
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import os

# Datei für gespeicherte Buchungen
DATEI_NAME = "buchungen.json"
TRAINER = ["Lisa", "Tom", "Anna", "Max"]
KURSE = {
    "Yoga": "Entspannendes Training für Körper und Geist.",
    "Spinning": "Intensives Ausdauertraining auf dem Fahrrad.",
    "Zumba": "Tanzfitness zu lateinamerikanischer Musik.",
    "Pilates": "Kräftigung der Tiefenmuskulatur und Stabilität."
}

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

# Mitgliedsnummer eingeben
tk.Label(root, text="Mitgliedsnummer:").pack()
mitgliedsnummer_entry = tk.Entry(root)
mitgliedsnummer_entry.pack()

# Uhrzeit auswählen
zeiten = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
uhrzeit_var = tk.StringVar(root)
uhrzeit_var.set(zeiten[0])
tk.OptionMenu(root, uhrzeit_var, *zeiten).pack()

# Kursauswahl
kurs_var = tk.StringVar(root)
kurs_var.set(list(KURSE.keys())[0])
kurs_dropdown = tk.OptionMenu(root, kurs_var, *KURSE.keys())
kurs_dropdown.pack()

# Kursbeschreibung
kursbeschreibung_label = tk.Label(root, text="", wraplength=400)
kursbeschreibung_label.pack()

def update_kursbeschreibung(*args):
    kursbeschreibung_label.config(text=KURSE[kurs_var.get()])

kurs_var.trace("w", update_kursbeschreibung)
update_kursbeschreibung()

# Trainerauswahl
trainer_var = tk.StringVar(root)
trainer_var.set(TRAINER[0])
tk.OptionMenu(root, trainer_var, *TRAINER).pack()

# Termin buchen
def termin_buchen():
    datum = cal.get_date()
    uhrzeit = uhrzeit_var.get()
    mitgliedsnummer = mitgliedsnummer_entry.get()
    kurs = kurs_var.get()
    trainer = trainer_var.get()

    if not mitgliedsnummer:
        messagebox.showerror("Fehler", "Bitte Mitgliedsnummer eingeben!")
        return

    # Prüfen, ob der Termin bereits belegt ist
    for buchung in buchungen:
        if buchung["datum"] == datum and buchung["uhrzeit"] == uhrzeit:
            messagebox.showinfo("Warteliste", "Termin belegt! Sie wurden auf die Warteliste gesetzt.")
            buchungen.append({"datum": datum, "uhrzeit": uhrzeit, "mitgliedsnummer": mitgliedsnummer, "kurs": kurs, "trainer": trainer, "status": "Warteliste"})
            speichere_buchungen()
            return

    # Termin buchen
    buchungen.append({"datum": datum, "uhrzeit": uhrzeit, "mitgliedsnummer": mitgliedsnummer, "kurs": kurs, "trainer": trainer, "status": "bestätigt"})
    speichere_buchungen()
    messagebox.showinfo("Erfolg", f"Termin am {datum} um {uhrzeit} gebucht!")

# Buchungsbutton
tk.Button(root, text="Termin buchen", command=termin_buchen).pack(pady=10)

# Alle Buchungen anzeigen
def anzeige_buchungen():
    if not buchungen:
        messagebox.showinfo("Buchungen", "Keine Buchungen vorhanden.")
        return
    buchungen_text = "\n".join([f"Datum: {b['datum']}, Uhrzeit: {b['uhrzeit']}, Mitglied: {b['mitgliedsnummer']}, Kurs: {b['kurs']}, Trainer: {b['trainer']}, Status: {b['status']}" for b in buchungen])
    messagebox.showinfo("Buchungen", buchungen_text)

tk.Button(root, text="Alle Buchungen anzeigen", command=anzeige_buchungen).pack(pady=10)

# Registrierung als Mitglied
def registrieren():
    messagebox.showinfo("Registrierung", "Zur Registrierung wenden Sie sich bitte an die Rezeption.")

tk.Button(root, text="Als Mitglied registrieren", command=registrieren).pack(pady=10)

# Hauptloop starten
root.mainloop()