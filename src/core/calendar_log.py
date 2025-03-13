import pandas as pd

""" start (dt), ende (dt), ID(kurs/termin),  ID(Mitglied), Status, Kommentar, Zusatzinfo


         start                  end
dt: '2025-03-13 14:00:12', '2025-03-13 14:45:00'
"""
# Mitglieder (first_name.... email)

# 
class CalendarLog:
    data = None
    file = ''

    def __init__(self, file='../../data/calendar_log.json'): #dunder Methode - 'magisch'
        self.file = file
        self.data = pd.read_json(file)


    def append(self, entry:dict):
        self.data.loc[len(self.data)] = entry

    def filter_eq(self, key, value): # prüft auf Gleichheit
        return self.data[self.data[key] == value]

    def filter_between(self, key, frm, until):
        return self.data[
            (self.data[key] >= frm)
            &
            (self.data[key] <= until)
        ]
    
    def show(self):
        print(self.data)

    def save(self):
        self.data.to_json(self.file)



cal = CalendarLog()

new_entry = { 
            'id': 3,
            'start': '2026-04-13 14:00:12',
            'end': '2026-04-13 14:45:12',
            'app_type_id': 999,
            'member_id': 666,
            'status': 'genehmigt',
            'comment': 'Blibb',
            'add_info': 'Heute nicht mehr'

         
        }

cal.append(new_entry)
cal.show()
cal.save()