import pandas as pd
from pandastable import Table

class Customers:
    data_file = '../data/customers_database.json'
    
    def __init__(self):
        self.data   = pd.read_json(self.data_file)
        print(self.data.head())
    
    def edit(self, id, mode):
        pass
    
    def new(self, data):
        pass
    
    def delete(self, data):
        pass
    
    def save():
        pass
    
    def get_data(self, topic):
        self.topic = topic
        return self.data
    

