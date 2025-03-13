import pandas as pd

dta = pd.read_json('data/customers_database.json')
#print(dta[dta['first_name']=='Karolina'])


print(dta[dta['country']=='China'].value_counts())

print(dta[dta['first_name'].str.startswith('A')])


def search(k, v):

    return dta[dta[k].str.starts(v)]

# print(search('first_name', 'C'))

print(dta.dtypes) 

(stammdaten[key] >= von) & (stammdaten[key] <= bis) 