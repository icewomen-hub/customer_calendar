import pandas as pd
from pandastable import Table
from core.customers import Customers
from core.data_provider import DataProvider

class TableHelper():
    
    valid_topics = ['courses', 'trainers','time_slots', 'roles']
    
    def __init__(self):
        pass
    
    def get_table(self, context, topic = 'customers'):
        
        my_data = self.read_data(topic)
        
        return Table(
            context, dataframe=my_data, showtoolbar=True, showstatusbar=True
        )
        
    def read_data(sel, topic):
        if topic == 'customers':
            data_source =  Customers()
        else:
            data_source =  DataProvider()
            
        return data_source.get_data(topic)