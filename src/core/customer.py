<<<<<<< HEAD
import pandas as pd

class Customer:
    data=None
    def __init__(self, file = "..\..\data\customers_new.json"):
        # Beispiel-Daten für Kunden
        self.data = pd.read_json(file)
    
    def filter_between(self, key, frm, until):
        """
        Filtert die Kunden im DataFrame basierend auf einem Bereich (von 'frm' bis 'until') für eine bestimmte Spalte ('key').
        
        Parameters:
        key (str): Der Name der Spalte, die gefiltert werden soll (z.B. 'Alter' oder 'Ausgaben').
        frm (int/float): Der untere Grenzwert des Bereichs.
        until (int/float): Der obere Grenzwert des Bereichs.
        
        Returns:
        pd.DataFrame: Ein DataFrame mit den gefilterten Kunden.
        """
        return self.data[(self.data[key] >= frm) & (self.data[key] <= until)]

# Erstellen eines Customer-Objekts
kunde = Customer()
print(kunde)
           
# Zum Beispiel: Filtere Kunden, deren ID zwischen 1 und 10 liegt
#filtered_customers = kunde.filter_between('id', 1, 10)
#print(filtered_customers)
