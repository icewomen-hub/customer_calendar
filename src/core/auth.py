import pandas as pd

class Authenticator:
    data = None
    
    def __init__(self, file='../../data/passwd.csv'):
        self.data = pd.read_csv(file)
        print(self.data.head(11))
        

foo = Authenticator()