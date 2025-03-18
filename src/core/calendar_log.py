import pandas as pd                   #panda wird verwendet um mit den Daten zu arbeiten,und die Datatime mit Datum und Uhrzeit arbeiten

""" start (dt), ende (dt), ID(kurs/termin),  ID(Mitglied), Status, Kommentar, Zusatzinfo


         start                  end
dt: '2025-03-13 14:00:12', '2025-03-13 14:45:00'
"""
# Mitglieder (first_name.... email)

# 
class CalendarLog:           #die klasse hat hat data (die Kalenderdatei) und file (der Pfad zur Datei, in der die Daten gespeichert sind)
    data = None
    file = ''

    def __init__(self, file='../../data/calendar_log.json'): #init Wird aufgerufen, wenn ein neues CalendarLog-Objekt erstellt wird. 
        self.file = file                                      #Hier wird der Standardpfad für die Datei gesetzt und die Daten werden geladen.
        self.data = pd.read_json(file)


    def append(self, entry:dict):                      # Fügt einen neuen Eintrag hinzu: Konvertiert die start und end Zeiten 
        self.data.loc[len(self.data)] = entry          #des neuen Eintrags in Datumswerte und fügt ihn der Tabelle hinzu

    def filter_eq(self, key, value): # Filtern nach einem bestimmten Wert(gleichheit): Diese Methode filtert die Daten,
        return self.data[self.data[key] == value] #um nur die Zeilen zu zeigen, die in der angegebenen Spalte (key) den angegebenen Wert (value) haben

    def filter_between(self, key, frm, until): #filtert die Daten und zeigt nur die Zeilen an,
        return self.data[                      #bei denen der Wert in der angegebenen Spalte (key) im angegebenen Zeitraum (frm bis until) liegt
            (self.data[key] >= frm)
            &
            (self.data[key] <= until)
        ]
    
    def show(self):      #Gibt die gesamte Tabelle (die Kalenderdaten) auf der Konsole aus
        print(self.data)

    def save(self):              
        self.data.to_json(self.file)         



cal = CalendarLog()       #die Instanz des Kalenders, die mit der Datei calendar_log.json arbeitet.

new_entry = { 
            'id': 3,
            'start': '2026-04-13 14:00:12',
            'end': '2026-04-13 14:45:12',             #Ein neues Dictionary, das die Details eines neuen Termins enthält, wie z.B. die ID des Mitglieds
            'app_type_id': 999,
            'member_id': 666,
            'status': 'genehmigt',
            'comment': 'Blibb',
            'add_info': 'Heute nicht mehr'

         
        }

cal.append(new_entry)     #Ruft die append-Methode auf, um den neuen Eintrag zu der Tabelle hinzuzufügen.
cal.show()                #Gibt die Tabelle mit den aktuellen Kalenderdaten aus.
cal.save()                #Speichert die Daten wieder in der Datei, um die Änderungen zu speichern.