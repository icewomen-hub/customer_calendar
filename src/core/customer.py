import pandas as pd
 

class Customer:
    data = None

    def __init__(self, file='../../data/customers_new.json'): #dunder Methode - 'magisch'
        self.data = pd.read_json(file)

    def filter_eq(self, key, value): # prüft auf Gleichheit
        return self.data[self.data[key] == value]

    def filter_between(self, key, frm, until):
        return self.data[
            (self.data[key] >= frm)
            &
            (self.data[key] <= until)
        ]
    
# ...
kunde = Customer()

# al = kunde.filter_eq('first_name', 'Anny')


id_spanne = kunde.filter_between('id', 55, 66)
print(id_spanne)